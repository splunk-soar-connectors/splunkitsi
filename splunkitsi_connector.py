# File: splunkitsi_connector.py
#
# Copyright (c) 2020-2022 Splunk Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under
# the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific language governing permissions
# and limitations under the License.
#
#
# Phantom sample App Connector python file
# Phantom App imports
import json
# Need some time
import time

import phantom.app as phantom
import requests
import xmltodict
from bs4 import BeautifulSoup
from phantom.action_result import ActionResult
from phantom.base_connector import BaseConnector

from splunkitsi_consts import *


class RetVal(tuple):
    def __new__(cls, val1, val2=None):
        return tuple.__new__(RetVal, (val1, val2))


class SplunkItServiceIntelligenceConnector(BaseConnector):

    def __init__(self):

        # Call the BaseConnectors init first
        super(SplunkItServiceIntelligenceConnector, self).__init__()

        self._state = None

        # Variable to hold a base_url in case the app makes REST calls
        # Do note that the app json defines the asset config, so please
        # modify this as you deem fit.
        self._base_url = None
        self._username = None
        self._password = None
        self._port = None
        self._token = None

        # Define dictionary constants
        self.itsi_episode_severity_values = { 'Info': '1', 'Normal': '2', 'Low': '3', 'Medium': '4', 'High': '5', 'Critical': '6' }
        self.itsi_episode_status_values = { 'Unassigned': '0', 'New': '1', 'In Progress': '2', 'Pending': '3', 'Resolved': '4', 'Closed': '5' }
        self.object_status_values = { 'Disabled': 0, 'Enabled': 1 }
        self.relative_time_values = { '15 min': '15m', '60 mins': '60m', '4 hours': '4h', '24 hours': '24h', '7 days': '7d', '30 days': '30d' }

    def _validate_integer(self, action_result, parameter, key):
        if parameter is not None:
            try:
                if not float(parameter).is_integer():
                    return action_result.set_status(phantom.APP_ERROR, VALID_INTEGER_MSG.format(key=key)), None

                parameter = int(parameter)
            except Exception:
                return action_result.set_status(phantom.APP_ERROR, VALID_INTEGER_MSG.format(key=key)), None

            if parameter < 0:
                return action_result.set_status(phantom.APP_ERROR, NON_NEGATIVE_INTEGER_MSG.format(key=key)), None

        return phantom.APP_SUCCESS, parameter

    def _get_error_message_from_exception(self, e):
        """ This method is used to get appropriate error message from the exception.
        :param e: Exception object
        :return: error message
        """
        error_code = None
        error_msg = ERROR_MSG_UNAVAILABLE

        try:
            if hasattr(e, "args"):
                if len(e.args) > 1:
                    error_code = e.args[0]
                    error_msg = e.args[1]
                elif len(e.args) == 1:
                    error_msg = e.args[0]
        except Exception:
            pass

        if not error_code:
            error_text = "Error Message: {}".format(error_msg)
        else:
            error_text = "Error Code: {}. Error Message: {}".format(error_code, error_msg)

        return error_text

    def _process_empty_response(self, response, action_result):

        if response.status_code == 200:
            return RetVal(phantom.APP_SUCCESS, {})

        return RetVal(action_result.set_status(
            phantom.APP_ERROR, "Status code: {0}. Empty response and no information in the header".format(response.status_code)), None)

    def _process_html_response(self, response, action_result):

        # An html response, treat it like an error
        status_code = response.status_code

        try:
            soup = BeautifulSoup(response.text, "html.parser")
            # Remove the script, style, footer and navigation part from the HTML message
            for element in soup(["script", "style", "footer", "nav"]):
               element.extract()
            error_text = soup.text
            split_lines = error_text.split('\n')
            split_lines = [x.strip() for x in split_lines if x.strip()]
            error_text = '\n'.join(split_lines)
        except Exception:
            error_text = "Cannot parse error details"

        message = "Status Code: {0}. Data from server:\n{1}\n".format(status_code, error_text)
        message = message.replace('{', '{{').replace('}', '}}')

        if len(message) > 500:
            message = 'Error occurred while connecting to the Splunk ITSI server'

        return RetVal(action_result.set_status(phantom.APP_ERROR, message), None)

    def _process_json_response(self, r, action_result):

        # Try a json parse
        try:
            resp_json = r.json()
        except Exception as e:
            err = self._get_error_message_from_exception(e)
            return RetVal(action_result.set_status(phantom.APP_ERROR, "Unable to parse JSON response. Error: {0}".format(err)), None)

        # Please specify the status codes here
        if 200 <= r.status_code < 400:
            return RetVal(phantom.APP_SUCCESS, resp_json)

        # You should process the error returned in the json
        error_message = r.text.replace('{', '{{').replace('}', '}}')
        message = "Error from server. Status Code: {0} Data from server: {1}".format(
                r.status_code, error_message)

        return RetVal(action_result.set_status(phantom.APP_ERROR, message), None)

    def _process_multiple_json_response(self, r, action_result):

        # Try a json parse
        try:
            response_text = r.text.splitlines()
        except Exception as e:
            err = self._get_error_message_from_exception(e)
            return RetVal(action_result.set_status(phantom.APP_ERROR, "Unable to parse the response. Error: {0}".format(err)), None)

        response_list = []
        for line in response_text:
            try:
                response_dict = json.loads(line)
            except Exception as e:
                err = self._get_error_message_from_exception(e)
                self.debug_print("Failed to parse line {0}. Error {1}".format(line, err))
                continue
            response_list.append(response_dict)

        # Please specify the status codes here
        if 200 <= r.status_code < 400:
            return RetVal(phantom.APP_SUCCESS, response_list)

        # You should process the error returned in the json
        error_message = r.text.replace('{', '{{').replace('}', '}}')
        message = "Error from server. Status Code: {0} Data from server: {1}".format(
                r.status_code, error_message)

        return RetVal(action_result.set_status(phantom.APP_ERROR, message), None)

    def _process_xml_response(self, r, action_result):

        resp_json = None
        try:
            if r.text:
                resp_json = xmltodict.parse(r.text)
        except Exception as e:
            error_message = self._get_error_message_from_exception(e)
            return RetVal(action_result.set_status(phantom.APP_ERROR, "Unable to parse XML response. Error: {0}".format(error_message)))

        if 200 <= r.status_code < 400:
            return RetVal(phantom.APP_SUCCESS, resp_json)

        error_type = resp_json.get('response', {}).get('messages', {}).get('msg', {}).get('@type')
        error_message = resp_json.get('response', {}).get('messages', {}).get('msg', {}).get('#text')

        if error_type or error_message:
            error = 'ErrorType: {} ErrorMessage: {}'.format(error_type, error_message)
        else:
            error = 'Unable to parse xml response'

        message = "Error from server. Status Code: {0} Data from server: {1}".format(
                r.status_code, error)

        return RetVal(action_result.set_status(phantom.APP_ERROR, message), resp_json)

    def _process_response(self, r, action_result):

        # store the r_text in debug data, it will get dumped in the logs if the action fails
        if hasattr(action_result, 'add_debug_data'):
            action_result.add_debug_data({'r_status_code': r.status_code})
            action_result.add_debug_data({'r_text': r.text})
            action_result.add_debug_data({'r_headers': r.headers})

        # Process each 'Content-Type' of response separately

        # Process a json response
        if 'json' in r.headers.get('Content-Type', '') and self.get_action_identifier() == 'get_episode_events':
            return self._process_multiple_json_response(r, action_result)

        # Process a json response
        if 'json' in r.headers.get('Content-Type', ''):
            return self._process_json_response(r, action_result)

        # Process an HTML response, Do this no matter what the api talks.
        # There is a high chance of a PROXY in between phantom and the rest of
        # world, in case of errors, PROXY's return HTML, this function parses
        # the error and adds it to the action_result.
        if 'html' in r.headers.get('Content-Type', ''):
            return self._process_html_response(r, action_result)

        if 'xml' in r.headers.get('Content-Type', ''):
            return self._process_xml_response(r, action_result)

        # it's not content-type that is to be parsed, handle an empty response
        if not r.text:
            return self._process_empty_response(r, action_result)

        # Looks like Splunk ITSI 4.2.x does not send Content-Type response headers.
        # Therefore, based on status code we return success,
        if 200 <= r.status_code < 400:
            return RetVal(phantom.APP_SUCCESS, {})

        # everything else is actually an error at this point
        message = "Can't process response from server. Status Code: {0} Data from server: {1}".format(
            r.status_code, r.text.replace('{', '{{').replace('}', '}}'))
        return RetVal(action_result.set_status(phantom.APP_ERROR, message), None)

    def _make_rest_call(self, endpoint, action_result, method="get", **kwargs):
        # **kwargs can be any additional parameters that requests.request accepts

        config = self.get_config()
        resp_json = None

        try:
            request_func = getattr(requests, method)
        except AttributeError:
            return RetVal(action_result.set_status(phantom.APP_ERROR, "Invalid method: {0}".format(method)), resp_json)

        # Create a URL to connect to
        url = '{}:{}{}'.format(self._base_url, self._port, endpoint)

        try:
            r = request_func(
                url,
                auth=self._auth,
                verify=config.get('verify_server_cert', False),
                **kwargs)
        except requests.exceptions.ConnectionError:
            error_message = 'Error Details: Connection Refused from the Server'
            return RetVal(action_result.set_status(phantom.APP_ERROR, error_message), resp_json)
        except Exception as e:
            err = self._get_error_message_from_exception(e)
            return RetVal(action_result.set_status(phantom.APP_ERROR, "Error Connecting to server. Details: {0}".format(err)), resp_json)
        return self._process_response(r, action_result)

    def _handle_test_connectivity(self, param):

        # Add an action result object to self (BaseConnector) to represent the action for this param
        action_result = self.add_action_result(ActionResult(dict(param)))

        # NOTE: test connectivity does _NOT_ take any parameters
        # i.e. the param dictionary passed to this handler will be empty.
        # Also typically it does not add any data into an action_result either.
        # The status and progress messages are more important.

        self.save_progress("Connecting to endpoint")
        # make rest call
        ret_val, response = self._make_rest_call('/servicesNS/nobody/SA-ITOA/itoa_interface/get_supported_object_types/',
            action_result,
            params=None,
            headers=self._headers)

        if (phantom.is_fail(ret_val)):
            # the call to the 3rd party device or service failed, action result should contain all the error details
            self.save_progress("Test Connectivity Failed")
            return action_result.get_status()

        # For now return Error with a message, in case of success we don't set the message, but use the summary
        self.save_progress("Test Connectivity Passed")
        return action_result.set_status(phantom.APP_SUCCESS)

    def _handle_get_episode(self, param):

        # Implement the handler here
        # use self.save_progress(...) to send progress messages back to the platform
        self.save_progress("In action handler for: {0}".format(self.get_action_identifier()))

        # Add an action result object to self (BaseConnector) to represent the action for this param
        action_result = self.add_action_result(ActionResult(dict(param)))

        # Required values can be accessed directly
        itsi_group_id = param['itsi_group_id']

        ret_val = self._check_episode_status(itsi_group_id, param, action_result)

        if (phantom.is_fail(ret_val)):
            return action_result.get_status()

        summary = action_result.update_summary({})
        summary['status'] = "Successfully retrieved the episode"

        return action_result.set_status(phantom.APP_SUCCESS)

    def _check_episode_status(self, itsi_group_id, param, action_result):

        action_id = self.get_action_identifier()

        # make rest call
        ret_val, response = self._make_rest_call(
            '/servicesNS/nobody/SA-ITOA/event_management_interface/notable_event_group/{0}'.format(itsi_group_id),
            action_result,
            method="get",
            params=None,
            headers=self._headers)

        if (phantom.is_fail(ret_val)):
            return action_result.get_status()

        if not response:
            return action_result.set_status(phantom.APP_ERROR, "Invalid itsi group id provided")

        if action_id == "get_episode":
            # Add the response into the data section
            action_result.add_data(response)

        return action_result.set_status(phantom.APP_SUCCESS)

    def _handle_update_episode(self, param):

        # Implement the handler here
        # use self.save_progress(...) to send progress messages back to the platform
        self.save_progress("In action handler for: {0}".format(self.get_action_identifier()))

        # Add an action result object to self (BaseConnector) to represent the action for this param
        action_result = self.add_action_result(ActionResult(dict(param)))
        ret_val = self._handle_update_episode_helper(param, action_result)

        if phantom.is_fail(ret_val):
            return action_result.get_status()

        summary = action_result.update_summary({})
        summary['status'] = "Successfully updated the episode"

        return action_result.set_status(phantom.APP_SUCCESS)

    def _handle_update_episode_helper(self, param, action_result):
        """Helper function for update episode"""
        # Access action parameters passed in the 'param' dictionary

        # Required values can be accessed directly
        itsi_group_id = param['itsi_group_id']

        # Optional values should use the .get() function
        status = param.get('status', None)
        severity = param.get('severity', None)
        owner = param.get('owner', None)

        if status is None and severity is None and owner is None:
            return(action_result.set_status(phantom.APP_ERROR, "Either status or severity or owner should be provided as parameters"))

        # Create payload for POST request
        payload = dict()
        if owner:
            payload['owner'] = owner
        if severity:
            payload['severity'] = self.itsi_episode_severity_values.get(severity, '1')
        if status:
            payload['status'] = self.itsi_episode_status_values.get(status, '1')

        # Create params for POST request
        q_params = { 'is_partial_data': '1' }

        # make rest call
        ret_val, response = self._make_rest_call(
            '/servicesNS/nobody/SA-ITOA/event_management_interface/notable_event_group/{0}'.format(itsi_group_id),
            action_result,
            method="put",
            params=q_params,
            headers=self._headers,
            json=payload)

        if (phantom.is_fail(ret_val)):
            return action_result.get_status()

        # Add the response into the data section
        action_result.add_data(response)

        return action_result.set_status(phantom.APP_SUCCESS)

    def _handle_break_episode(self, param):

        # Implement the handler here
        # use self.save_progress(...) to send progress messages back to the platform
        self.save_progress("In action handler for: {0}".format(self.get_action_identifier()))

        # Add an action result object to self (BaseConnector) to represent the action for this param
        action_result = self.add_action_result(ActionResult(dict(param)))
        ret_val = self._handle_break_episode_helper(param, action_result)

        if phantom.is_fail(ret_val):
            return action_result.get_status()

        summary = action_result.update_summary({})
        summary['status'] = "Successfully broke the episode"

        return action_result.set_status(phantom.APP_SUCCESS)

    def _handle_break_episode_helper(self, param, action_result):
        """Helper function for break episode"""

        # Required values can be accessed directly
        itsi_group_id = param['itsi_group_id']
        itsi_policy_id = param['itsi_policy_id']
        status = param['status']
        title = param['title']
        description = param['description']
        severity = param['severity']
        owner = param['owner']

        # Create payload for POST request
        payload = {
            '_key': itsi_group_id,
            'status': status,
            'title': title,
            'description': description,
            'severity': severity,
            'owner': owner
        }

        # Create params for POST request
        q_params = {
            'break_group_policy_id': itsi_policy_id
        }

        # make rest call
        ret_val, response = self._make_rest_call('/servicesNS/nobody/SA-ITOA/event_management_interface/notable_event_group',
            action_result,
            method="post",
            params=q_params,
            headers=self._headers,
            json=payload)

        if (phantom.is_fail(ret_val)):
            return action_result.get_status()

        return action_result.set_status(phantom.APP_SUCCESS)

    def _handle_close_episode(self, param):

        # Implement the handler here
        # use self.save_progress(...) to send progress messages back to the platform
        self.save_progress("In action handler for: {0}".format(self.get_action_identifier()))

        # Add an action result object to self (BaseConnector) to represent the action for this param
        action_result = self.add_action_result(ActionResult(dict(param)))

        # Optional values should use the .get() function
        break_episode = param.get('break_episode', True)
        itsi_policy_id = param.get('itsi_policy_id', None)

        if ((break_episode) and (itsi_policy_id is None)):
            return action_result.set_status(phantom.APP_ERROR, "Missing notable event aggregation policy id")

        if (break_episode):
            ret_val = self._handle_break_episode_helper(param, action_result)
            if (phantom.is_fail(ret_val)):
                return action_result.get_status()

        # Set episode status to Closed and call update episode handler
        param['status'] = 'Closed'

        ret_val = self._handle_update_episode_helper(param, action_result)

        if (phantom.is_fail(ret_val)):
            return action_result.get_status()

        summary = action_result.update_summary({})
        summary['status'] = "Successfully closed the episode"

        return action_result.set_status(phantom.APP_SUCCESS)

    def _handle_add_episode_comment(self, param):

        # Implement the handler here
        # use self.save_progress(...) to send progress messages back to the platform
        self.save_progress("In action handler for: {0}".format(self.get_action_identifier()))

        # Add an action result object to self (BaseConnector) to represent the action for this param
        action_result = self.add_action_result(ActionResult(dict(param)))

        # Required values can be accessed directly
        itsi_group_id = param['itsi_group_id']
        comment = param['comment']

        # Check if itsi group id is valid or not
        ret_val = self._check_episode_status(itsi_group_id, param, action_result)

        if (phantom.is_fail(ret_val)):
            return action_result.get_status()

        # Create payload for POST request
        payload = dict()
        payload['event_id'] = itsi_group_id
        payload['comment'] = comment

        # make rest call
        ret_val, response = self._make_rest_call('/servicesNS/nobody/SA-ITOA/event_management_interface/notable_event_comment',
            action_result,
            method="post",
            params=None,
            headers=self._headers,
            json=payload)

        if (phantom.is_fail(ret_val)):
            return action_result.get_status()

        # Add the response into the data section
        action_result.add_data(response)

        # Add a dictionary that is made up of the most important values from data into the summary
        summary = action_result.update_summary({ 'itsi_group_id': itsi_group_id})
        try:
            summary['comment_id'] = response['comment_id']
        except Exception:
            return action_result.set_status(phantom.APP_ERROR, "Error while parsing API response to get the Comment ID")

        return action_result.set_status(phantom.APP_SUCCESS)

    def _handle_get_episode_events(self, param):

        # Implement the handler here
        # use self.save_progress(...) to send progress messages back to the platform
        self.save_progress("In action handler for: {0}".format(self.get_action_identifier()))

        # Add an action result object to self (BaseConnector) to represent the action for this param
        action_result = self.add_action_result(ActionResult(dict(param)))

        # Required values can be accessed directly
        itsi_group_id = param['itsi_group_id']

        # Optional values should use the .get() function
        earliest_time = param.get('earliest_time', '60 mins')
        max_results = param.get('max_results', '1')

        # Check if itsi group id is valid or not
        ret_val = self._check_episode_status(itsi_group_id, param, action_result)

        if (phantom.is_fail(ret_val)):
            return action_result.get_status()

        # Create params for GET request
        earliest_time = '-' + self.relative_time_values.get(earliest_time, earliest_time)
        search_string = ('search index=itsi_grouped_alerts sourcetype=itsi_notable:group NOT source=itsi@internal@group_closing_event '
                         'itsi_group_id="' + itsi_group_id + '"'
                         ' | eval itsi_service_ids = split(itsi_service_ids,",") | '
                         'mvexpand itsi_service_ids | dedup event_id | head ' + max_results)
        q_params = {
                    'search': search_string,
                    'earliest_time': earliest_time,
                    'latest_time': 'now',
                    'label': 'phantom_itsi_app_get_episode_events',
                    'auto_cancel': '60',
                    'output_mode': 'json'
                   }

        # make rest call
        ret_val, response = self._make_rest_call('/servicesNS/nobody/itsi/search/jobs/export',
            action_result,
            method="get",
            params=q_params,
            headers=self._headers)

        if (phantom.is_fail(ret_val)):
            return action_result.get_status()

        for event in response:
            if event.get('result'):
                action_result.add_data(event['result'])

        summary = action_result.update_summary({})
        summary['total_episode_events'] = action_result.get_data_size()

        return action_result.set_status(phantom.APP_SUCCESS)

    def _handle_add_episode_ticket(self, param):

        # Implement the handler here
        # use self.save_progress(...) to send progress messages back to the platform
        self.save_progress("In action handler for: {0}".format(self.get_action_identifier()))

        # Add an action result object to self (BaseConnector) to represent the action for this param
        action_result = self.add_action_result(ActionResult(dict(param)))

        # Required values can be accessed directly
        itsi_group_id = param['itsi_group_id']
        ticket_system = param['ticket_system']
        ticket_id = param['ticket_id']

        # Optional values should use the .get() function
        ticket_url = param.get('ticket_url', '')

        # Check if itsi group id is valid or not
        ret_val = self._check_episode_status(itsi_group_id, param, action_result)

        if (phantom.is_fail(ret_val)):
            return action_result.get_status()

        # Create payload for POST request
        payload = dict()
        payload['ids'] = [itsi_group_id]
        payload['ticket_system'] = ticket_system
        payload['ticket_id'] = ticket_id
        payload['ticket_url'] = ticket_url

        # make rest call
        ret_val, response = self._make_rest_call('/servicesNS/nobody/SA-ITOA/event_management_interface/ticketing',
            action_result,
            method="post",
            params=None,
            headers=self._headers,
            json=payload)

        if (phantom.is_fail(ret_val)):
            return action_result.get_status()

        # Add the response into the data section
        action_result.add_data(response)

        summary = action_result.update_summary({})
        summary['status'] = "Successfully added episode ticket"

        return action_result.set_status(phantom.APP_SUCCESS)

    def _handle_get_episode_tickets(self, param):

        # Implement the handler here
        # use self.save_progress(...) to send progress messages back to the platform
        self.save_progress("In action handler for: {0}".format(self.get_action_identifier()))

        # Add an action result object to self (BaseConnector) to represent the action for this param
        action_result = self.add_action_result(ActionResult(dict(param)))

        # Required values can be accessed directly
        itsi_group_id = param['itsi_group_id']

        # Check if itsi group id is valid or not
        ret_val = self._check_episode_status(itsi_group_id, param, action_result)

        if (phantom.is_fail(ret_val)):
            return action_result.get_status()

        # make rest call
        ret_val, response = self._make_rest_call('/servicesNS/nobody/SA-ITOA/event_management_interface/ticketing/{0}'.format(itsi_group_id),
            action_result,
            method="get",
            params=None,
            headers=self._headers)

        if (phantom.is_fail(ret_val)):
            return action_result.get_status()

        # Add the response into the data section
        if not response:
            return action_result.set_status(phantom.APP_SUCCESS, "No data found")

        action_result.add_data(response)

        number_of_tickets = 0
        for ticket_object in response:
            number_of_tickets += len(ticket_object.get('tickets', []))

        summary = action_result.update_summary({})
        summary['total_episode_tickets'] = number_of_tickets

        return action_result.set_status(phantom.APP_SUCCESS)

    def _handle_get_service(self, param):

        # Implement the handler here
        # use self.save_progress(...) to send progress messages back to the platform
        self.save_progress("In action handler for: {0}".format(self.get_action_identifier()))

        # Add an action result object to self (BaseConnector) to represent the action for this param
        action_result = self.add_action_result(ActionResult(dict(param)))

        # Required values can be accessed directly
        itsi_service_id = param['itsi_service_id']

        # Check if itsi service id is valid or not
        ret_val = self._check_service_status(itsi_service_id, param, action_result)

        if (phantom.is_fail(ret_val)):
            return action_result.get_status()

        summary = action_result.update_summary({})
        summary['status'] = "Successfully retrieved the service"

        return action_result.set_status(phantom.APP_SUCCESS)

    def _check_service_status(self, itsi_service_id, param, action_result):

        action_id = self.get_action_identifier()

        # make rest call
        ret_val, response = self._make_rest_call('/servicesNS/nobody/SA-ITOA/itoa_interface/service/{0}'.format(itsi_service_id),
            action_result,
            method="get",
            params=None,
            headers=self._headers)

        if (phantom.is_fail(ret_val)):
            return action_result.get_status()

        if action_id == 'get_service':
            # Add the response into the data section
            if response.get('_key'):
                response['key'] = response.pop('_key')
            action_result.add_data(response)

        return action_result.set_status(phantom.APP_SUCCESS)

    def _handle_get_service_entities(self, param):

        # Implement the handler here
        # use self.save_progress(...) to send progress messages back to the platform
        self.save_progress("In action handler for: {0}".format(self.get_action_identifier()))

        # Add an action result object to self (BaseConnector) to represent the action for this param
        action_result = self.add_action_result(ActionResult(dict(param)))

        # Required values can be accessed directly
        itsi_service_id = param['itsi_service_id']

        # Check if itsi service id is valid or not
        ret_val = self._check_service_status(itsi_service_id, param, action_result)

        if (phantom.is_fail(ret_val)):
            return action_result.get_status()

        # Create params for GET request
        q_params = {'filter': json.dumps({ 'services._key': itsi_service_id })}

        # make rest call
        ret_val, response = self._make_rest_call('/servicesNS/nobody/SA-ITOA/itoa_interface/entity',
            action_result,
            method="get",
            params=q_params,
            headers=self._headers)

        if (phantom.is_fail(ret_val)):
            return action_result.get_status()

        action_result.add_data(response)

        summary = action_result.update_summary({})
        summary['status'] = "Successfully retrieved the service entities"

        return action_result.set_status(phantom.APP_SUCCESS)

    def _handle_update_service_status(self, param):

        # Implement the handler here
        # use self.save_progress(...) to send progress messages back to the platform
        self.save_progress("In action handler for: {0}".format(self.get_action_identifier()))

        # Add an action result object to self (BaseConnector) to represent the action for this param
        action_result = self.add_action_result(ActionResult(dict(param)))

        # Required values can be accessed directly
        itsi_service_id = param['itsi_service_id']
        service_status = param['service_status']

        # Check if itsi service id is valid or not
        ret_val = self._check_service_status(itsi_service_id, param, action_result)

        if (phantom.is_fail(ret_val)):
            return action_result.get_status()

        # Create payload for POST request
        payload = dict()
        payload['enabled'] = self.object_status_values.get(service_status, 1)

        # Create params for POST request
        params = { 'is_partial_data': '1' }

        # make rest call
        ret_val, response = self._make_rest_call('/servicesNS/nobody/SA-ITOA/itoa_interface/service/{0}'.format(itsi_service_id),
            action_result,
            method="put",
            params=params,
            headers=self._headers,
            json=payload)

        if (phantom.is_fail(ret_val)):
            return action_result.get_status()

        # Add the response into the data section
        action_result.add_data(response)

        summary = action_result.update_summary({})
        summary['status'] = "Successfully updated the service status"

        return action_result.set_status(phantom.APP_SUCCESS)

    def _handle_get_entity(self, param):

        # Implement the handler here
        # use self.save_progress(...) to send progress messages back to the platform
        self.save_progress("In action handler for: {0}".format(self.get_action_identifier()))

        # Add an action result object to self (BaseConnector) to represent the action for this param
        action_result = self.add_action_result(ActionResult(dict(param)))

        # Required values can be accessed directly
        itsi_entity_id = param['itsi_entity_id']

        # make rest call
        ret_val, response = self._make_rest_call('/servicesNS/nobody/SA-ITOA/itoa_interface/entity/{0}'.format(itsi_entity_id),
            action_result,
            method="get",
            params=None,
            headers=self._headers)

        if (phantom.is_fail(ret_val)):
            return action_result.get_status()

        # Add the response into the data section
        action_result.add_data(response)

        summary = action_result.update_summary({})
        summary['status'] = "Successfully retrieved the entity"

        return action_result.set_status(phantom.APP_SUCCESS)

    def _handle_get_maintenance_window(self, param):

        # Implement the handler here
        # use self.save_progress(...) to send progress messages back to the platform
        self.save_progress("In action handler for: {0}".format(self.get_action_identifier()))

        # Add an action result object to self (BaseConnector) to represent the action for this param
        action_result = self.add_action_result(ActionResult(dict(param)))

        # Required values can be accessed directly
        maintenance_window_id = param['maintenance_window_id']

        ret_val = self._check_maintenance_window_status(maintenance_window_id, param, action_result)

        if (phantom.is_fail(ret_val)):
            return action_result.get_status()

        summary = action_result.update_summary({})
        summary['status'] = "Successfully retrieved maintenance window"

        return action_result.set_status(phantom.APP_SUCCESS)

    def _check_maintenance_window_status(self, maintenance_window_id, param, action_result):

        action_id = self.get_action_identifier()

        # make rest call
        ret_val, response = self._make_rest_call(
            '/servicesNS/nobody/SA-ITOA/maintenance_services_interface/maintenance_calendar/{0}'.format(maintenance_window_id),
            action_result,
            method="get",
            params=None,
            headers=self._headers)

        if (phantom.is_fail(ret_val)):
            return action_result.get_status()

        if action_id == 'get_maintenance_window':
            # Add the response into the data section
            action_result.add_data(response)

        if action_id == 'end_maintenance_window':
            maintenance_window_end_time = response.get('end_time')
            maintenance_window_start_time = response.get('start_time')
            if maintenance_window_end_time and maintenance_window_end_time < time.time():
                return(action_result.set_status(phantom.APP_ERROR, "Maintenance window is already ended"))
            if maintenance_window_start_time and maintenance_window_start_time > time.time():
                return(action_result.set_status(phantom.APP_ERROR, "Maintenance window is not started yet"))

        return action_result.set_status(phantom.APP_SUCCESS)

    def _handle_add_maintenance_window(self, param):

        # Implement the handler here
        # use self.save_progress(...) to send progress messages back to the platform
        self.save_progress("In action handler for: {0}".format(self.get_action_identifier()))

        # Add an action result object to self (BaseConnector) to represent the action for this param
        action_result = self.add_action_result(ActionResult(dict(param)))

        # Required values can be accessed directly
        title = param['title']

        # Optional values should use the .get() function
        start_time = param.get('start_time', None)
        # Integer validation for 'start_time' parameter
        ret_val, start_time = self._validate_integer(action_result, start_time, "'start_time' action parameter")
        if phantom.is_fail(ret_val):
            return action_result.get_status()

        end_time = param.get('end_time', None)
        # Integer validation for 'end_time' parameter
        ret_val, end_time = self._validate_integer(action_result, end_time, "'end_time' action parameter")
        if phantom.is_fail(ret_val):
            return action_result.get_status()

        relative_start_time = param.get('relative_start_time', 0)
        # Integer validation for 'relative_start_time' parameter
        ret_val, relative_start_time = self._validate_integer(action_result, relative_start_time, "'relative_start_time' action parameter")
        if phantom.is_fail(ret_val):
            return action_result.get_status()

        relative_end_time = param.get('relative_end_time', 300)
        # Integer validation for 'relative_end_time' parameter
        ret_val, relative_end_time = self._validate_integer(action_result, relative_end_time, "'relative_end_time' action parameter")
        if phantom.is_fail(ret_val):
            return action_result.get_status()

        object_type = param.get('object_type', None)
        object_ids = param.get('object_ids', None)
        if object_ids:
            object_ids = [object_id.strip() for object_id in object_ids.split(",")]
            object_ids = list(filter(None, object_ids))
            object_ids = ", ".join(object_ids)

        comment = param.get('comment', None)

        # start_time and end_time are expected to be defined in seconds since the epoch.
        # The input type is numeric. Check whether we are within the limits, that is
        # 0 <= t <= 2147483647
        if ((start_time is not None) and ((start_time < 0) or (start_time > 2147483647))):
            return action_result.set_status(phantom.APP_ERROR, "start_time out of range")
        if ((end_time is not None) and ((end_time < 0) or (end_time > 2147483647))):
            return action_result.set_status(phantom.APP_ERROR, "end_time out of range")

        start_time_val = start_time if start_time is not None else time.time() + relative_start_time
        end_time_val = end_time if end_time is not None else time.time() + relative_end_time

        objects = None
        # object_type and object_ids are mandatory.
        # object_ids is a comma separated list of values. Split it and remove whitespace.
        if ((object_ids is None) or (object_type is None)):
            return action_result.set_status(phantom.APP_ERROR, "Missing object information")
        object_id_list = [ x.strip() for x in object_ids.split(',') ]
        objects = [ { '_key': i, 'object_type': object_type } for i in object_id_list ]

        # Create payload for POST request
        payload = { 'title': title }
        payload['start_time'] = start_time_val
        payload['end_time'] = end_time_val
        if objects is not None:
            payload['objects'] = objects
        if comment is not None:
            payload['comment'] = comment

        # Create params for POST request
        params = { 'is_partial_data': '1' }

        # make rest call
        ret_val, response = self._make_rest_call('/servicesNS/nobody/SA-ITOA/maintenance_services_interface/maintenance_calendar',
            action_result,
            method="post",
            params=params,
            headers=self._headers,
            json=payload)

        if (phantom.is_fail(ret_val)):
            return action_result.get_status()

        # Add the response into the data section
        action_result.add_data(response)

        summary = action_result.update_summary({})
        summary['status'] = "Successfully added maintenance window"

        return action_result.set_status(phantom.APP_SUCCESS)

    def _handle_update_maintenance_window(self, param):

        # Implement the handler here
        # use self.save_progress(...) to send progress messages back to the platform
        self.save_progress("In action handler for: {0}".format(self.get_action_identifier()))

        # Add an action result object to self (BaseConnector) to represent the action for this param
        action_result = self.add_action_result(ActionResult(dict(param)))

        # Required values can be accessed directly
        maintenance_window_id = param['maintenance_window_id']

        ret_val = self._check_maintenance_window_status(maintenance_window_id, param, action_result)

        if (phantom.is_fail(ret_val)):
            return action_result.get_status()

        # Optional values should use the .get() function
        title = param.get('title', None)
        start_time = param.get('start_time', None)
        # Integer validation for 'start_time' parameter
        ret_val, start_time = self._validate_integer(action_result, start_time, "'start_time' action parameter")
        if phantom.is_fail(ret_val):
            return action_result.get_status()

        end_time = param.get('end_time', None)
        # Integer validation for 'end_time' parameter
        ret_val, end_time = self._validate_integer(action_result, end_time, "'end_time' action parameter")
        if phantom.is_fail(ret_val):
            return action_result.get_status()

        relative_start_time = param.get('relative_start_time', None)
        # Integer validation for 'relative_start_time' parameter
        ret_val, relative_start_time = self._validate_integer(action_result, relative_start_time, "'relative_start_time' action parameter")
        if phantom.is_fail(ret_val):
            return action_result.get_status()

        relative_end_time = param.get('relative_end_time', None)
        # Integer validation for 'relative_end_time' parameter
        ret_val, relative_end_time = self._validate_integer(action_result, relative_end_time, "'relative_end_time' action parameter")
        if phantom.is_fail(ret_val):
            return action_result.get_status()

        object_type = param.get('object_type', None)
        object_ids = param.get('object_ids', None)
        if object_ids:
            object_ids = [object_id.strip() for object_id in object_ids.split(",")]
            object_ids = list(filter(None, object_ids))
            object_ids = ", ".join(object_ids)

        comment = param.get('comment', None)

        objects = None
        # If we have objects_ids and object_type, create an objects list of dicts
        # object_ids is a comma separated list of values. Split it and remove whitespace.
        # If one of object_ids or object_type is None, ignore.
        if ((object_ids is not None) and (object_type is not None)):
            object_id_list = [ x.strip() for x in object_ids.split(',') ]
            objects = [ { '_key': i, 'object_type': object_type } for i in object_id_list ]

        # start_time and end_time are expected to be defined in seconds since the epoch.
        # The input type is numeric. Check whether we are within the limits, that is
        # 0 <= t <= 2147483647
        if ((start_time is not None) and ((start_time < 0) or (start_time > 2147483647))):
            return action_result.set_status(phantom.APP_ERROR, "start_time out of range")
        if ((end_time is not None) and ((end_time < 0) or (end_time > 2147483647))):
            return action_result.set_status(phantom.APP_ERROR, "end_time out of range")

        start_time_val = start_time if start_time is not None else (
            time.time() + relative_start_time if relative_start_time is not None else None)
        end_time_val = end_time if end_time is not None else (time.time() + relative_end_time if relative_end_time is not None else None)

        # Create payload for POST request
        payload = dict()
        if title is not None:
            payload['title'] = title
        if start_time_val is not None:
            payload['start_time'] = start_time_val
        if end_time_val is not None:
            payload['end_time'] = end_time_val
        if objects is not None:
            payload['objects'] = objects
        if comment is not None:
            payload['comment'] = comment

        # Create params for POST request
        params = { 'is_partial_data': '1' }

        # make rest call
        ret_val, response = self._make_rest_call(
            '/servicesNS/nobody/SA-ITOA/maintenance_services_interface/maintenance_calendar/{0}'.format(maintenance_window_id),
            action_result,
            method="put",
            params=params,
            headers=self._headers,
            json=payload)

        if (phantom.is_fail(ret_val)):
            return action_result.get_status()

        # Add the response into the data section
        action_result.add_data(response)

        summary = action_result.update_summary({})
        summary['status'] = "Successfully updated maintenance window"

        return action_result.set_status(phantom.APP_SUCCESS)

    def _handle_end_maintenance_window(self, param):

        # Implement the handler here
        # use self.save_progress(...) to send progress messages back to the platform
        self.save_progress("In action handler for: {0}".format(self.get_action_identifier()))

        # Add an action result object to self (BaseConnector) to represent the action for this param
        action_result = self.add_action_result(ActionResult(dict(param)))

        # Required values can be accessed directly
        maintenance_window_id = param['maintenance_window_id']
        comment = param['comment']

        ret_val = self._check_maintenance_window_status(maintenance_window_id, param, action_result)

        if (phantom.is_fail(ret_val)):
            return action_result.get_status()

        # Create payload for POST request
        # end_time is now in seconds since the epoch (which mean UTC)
        payload = { 'end_time': time.time() + 1 }
        payload['comment'] = comment

        # Create params for POST request
        params = { 'is_partial_data': '1' }

        # make rest call
        ret_val, response = self._make_rest_call(
            '/servicesNS/nobody/SA-ITOA/maintenance_services_interface/maintenance_calendar/{0}'.format(maintenance_window_id),
            action_result,
            method="post",
            params=params,
            headers=self._headers,
            json=payload)

        if (phantom.is_fail(ret_val)):
            return action_result.get_status()

        # Add the response into the data section
        action_result.add_data(response)

        summary = action_result.update_summary({})
        summary['status'] = "Successfully ended maintenance window"

        return action_result.set_status(phantom.APP_SUCCESS)

    def handle_action(self, param):

        ret_val = phantom.APP_SUCCESS

        # Get the action that we are supposed to execute for this App Run
        action_id = self.get_action_identifier()

        self.debug_print("action_id", self.get_action_identifier())

        if action_id == 'test_connectivity':
            ret_val = self._handle_test_connectivity(param)

        elif action_id == 'get_episode':
            ret_val = self._handle_get_episode(param)

        elif action_id == 'update_episode':
            ret_val = self._handle_update_episode(param)

        elif action_id == 'break_episode':
            ret_val = self._handle_break_episode(param)

        elif action_id == 'close_episode':
            ret_val = self._handle_close_episode(param)

        elif action_id == 'add_episode_comment':
            ret_val = self._handle_add_episode_comment(param)

        elif action_id == 'get_episode_events':
            ret_val = self._handle_get_episode_events(param)

        elif action_id == 'add_episode_ticket':
            ret_val = self._handle_add_episode_ticket(param)

        elif action_id == 'get_episode_tickets':
            ret_val = self._handle_get_episode_tickets(param)

        elif action_id == 'get_service':
            ret_val = self._handle_get_service(param)

        elif action_id == 'get_service_entities':
            ret_val = self._handle_get_service_entities(param)

        elif action_id == 'get_entity':
            ret_val = self._handle_get_entity(param)

        elif action_id == 'update_service_status':
            ret_val = self._handle_update_service_status(param)

        elif action_id == 'get_maintenance_window':
            ret_val = self._handle_get_maintenance_window(param)

        elif action_id == 'add_maintenance_window':
            ret_val = self._handle_add_maintenance_window(param)

        elif action_id == 'update_maintenance_window':
            ret_val = self._handle_update_maintenance_window(param)

        elif action_id == 'end_maintenance_window':
            ret_val = self._handle_end_maintenance_window(param)

        return ret_val

    def initialize(self):

        # Load the state in initialize, use it to store data
        # that needs to be accessed across actions
        self._state = self.load_state()

        # get the asset config
        config = self.get_config()

        self._base_url = config.get('base_url')
        self._port = config.get('port')
        self._username = config.get('username')
        self._password = config.get('password')
        self._token = config.get('token')

        self._headers = { 'Content-Type': 'application/json' }
        # If we have a token defined, use it for authorization,
        # else we use basic authentication with username and password
        if self._token:
            self._headers['Authorization'] = 'Bearer {}'.format(self._token)
            self._auth = None
        else:
            self._auth = (self._username, self._password)

        return phantom.APP_SUCCESS

    def finalize(self):

        # Save the state, this data is saved across actions and app upgrades
        self.save_state(self._state)
        return phantom.APP_SUCCESS


if __name__ == '__main__':

    import argparse
    import sys

    import pudb

    pudb.set_trace()

    argparser = argparse.ArgumentParser()

    argparser.add_argument('input_test_json', help='Input Test JSON file')
    argparser.add_argument('-u', '--username', help='username', required=False)
    argparser.add_argument('-p', '--password', help='password', required=False)

    args = argparser.parse_args()
    session_id = None

    username = args.username
    password = args.password
    verify = args.verify

    if username is not None and password is None:

        # User specified a username but not a password, so ask
        import getpass
        password = getpass.getpass("Password: ")

    if username and password:
        try:
            login_url = SplunkItServiceIntelligenceConnector._get_phantom_base_url() + '/login'

            print("Accessing the Login page")
            r = requests.get(login_url, verify=verify, timeout=60)
            csrftoken = r.cookies['csrftoken']

            data = dict()
            data['username'] = username
            data['password'] = password
            data['csrfmiddlewaretoken'] = csrftoken

            headers = dict()
            headers['Cookie'] = 'csrftoken=' + csrftoken
            headers['Referer'] = login_url

            print("Logging into Platform to get the session id")
            r2 = requests.post(login_url, verify=verify, data=data, headers=headers, timeout=60)
            session_id = r2.cookies['sessionid']
        except Exception as e:
            print("Unable to get session id from the platform. Error: {0}".format(str(e)))
            sys.exit(1)

    with open(args.input_test_json) as f:
        in_json = f.read()
        in_json = json.loads(in_json)
        print(json.dumps(in_json, indent=4))

        connector = SplunkItServiceIntelligenceConnector()
        connector.print_progress_message = True

        if session_id is not None:
            in_json['user_session_token'] = session_id
            connector._set_csrf_info(csrftoken, headers['Referer'])

        ret_val = connector._handle_action(json.dumps(in_json), None)
        print(json.dumps(json.loads(ret_val), indent=4))

    sys.exit(0)
