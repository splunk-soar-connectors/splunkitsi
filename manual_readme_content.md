[comment]: # " File: README.md"
[comment]: # "  Copyright (c) 2020-2022 Splunk Inc."
[comment]: # ""
[comment]: # "Licensed under the Apache License, Version 2.0 (the 'License');"
[comment]: # "you may not use this file except in compliance with the License."
[comment]: # "You may obtain a copy of the License at"
[comment]: # ""
[comment]: # "    http://www.apache.org/licenses/LICENSE-2.0"
[comment]: # ""
[comment]: # "Unless required by applicable law or agreed to in writing, software distributed under"
[comment]: # "the License is distributed on an 'AS IS' BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,"
[comment]: # "either express or implied. See the License for the specific language governing permissions"
[comment]: # "and limitations under the License."
[comment]: # ""
## User Roles

Make sure you have assigned proper roles to a user you are using to perform various actions on
Splunk ITSI. Refer to this Splunk
[Documentation](https://docs.splunk.com/Documentation/ITSI/4.13.0/Configure/UsersRoles) for more
details on configuring users and roles in Splunk ITSI.

## Playbook Backward Compatibility

-   The parameters have been modified in the below-existing action. Hence, it is requested to update
    existing playbooks created in the earlier versions of the app by re-inserting | modifying |
    deleting the corresponding action blocks.

      

    -   Close Episode - Below parameters have been removed. It is advised to use the 'break episode'
        action to break the episode by closing it.

          

        -   break_episode
        -   itsi_policy_id

    -   Add Episode Ticket - Below parameter have been modified.

          

        -   The parameter 'custom_ticketing_system_name' has been added
        -   A new value 'New Custom Ticketing System' has been added in the 'ticket_system'
            parameter to create tickets in the custom ticketing system

## Port Information

The app uses HTTP/ HTTPS protocol for communicating with the Splunk ITSI server. Below are the
default ports used by Splunk SOAR.

| Service Name | Transport Protocol | Port |
|--------------|--------------------|------|
| http         | tcp                | 80   |
| https        | tcp                | 443  |
