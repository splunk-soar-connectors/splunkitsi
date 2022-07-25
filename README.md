[comment]: # "Auto-generated SOAR connector documentation"
# Splunk IT Service Intelligence for SOAR

Publisher: Splunk  
Connector Version: 2\.0\.0  
Product Vendor: Splunk  
Product Name: Splunk ITSI  
Product Version Supported (regex): "\.\*"  
Minimum Product Version: 5\.2\.0  

This app integrates with Splunk IT Service Intelligence to provide operations on Splunk IT Service Intelligence episodes, services, entities, and object maintenance

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
    existing playbooks created in the earlier versions of the app by re-inserting \| modifying \|
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


### Configuration Variables
The below configuration variables are required for this Connector to operate.  These variables are specified when configuring a Splunk ITSI asset in SOAR.

VARIABLE | REQUIRED | TYPE | DESCRIPTION
-------- | -------- | ---- | -----------
**base\_url** |  required  | string | Splunk ITSI Search Head Base URL
**port** |  required  | numeric | Splunk ITSI Search Head Management Port
**username** |  optional  | string | Splunk ITSI User Name
**password** |  optional  | password | Splunk ITSI Password
**token** |  optional  | password | Splunk ITSI Access Token
**verify\_server\_cert** |  optional  | boolean | Verify Server Certificate

### Supported Actions  
[end maintenance window](#action-end-maintenance-window) - End Splunk ITSI maintenance window  
[update maintenance window](#action-update-maintenance-window) - Update Splunk ITSI maintenance window  
[add maintenance window](#action-add-maintenance-window) - Add Splunk ITSI maintenance window  
[get maintenance window](#action-get-maintenance-window) - Get Splunk ITSI maintenance window information  
[update service status](#action-update-service-status) - Update Splunk ITSI service status  
[get service entities](#action-get-service-entities) - Get entities of a Splunk ITSI service  
[get service](#action-get-service) - Get Splunk ITSI service information  
[get entity](#action-get-entity) - Get Splunk ITSI entity information  
[get episode tickets](#action-get-episode-tickets) - Get ticket information for a Splunk ITSI episode  
[add episode ticket](#action-add-episode-ticket) - Add a ticket to a Splunk ITSI episode  
[get episode events](#action-get-episode-events) - Get latest events for Splunk ITSI episode  
[close episode](#action-close-episode) - Close a Splunk ITSI episode  
[break episode](#action-break-episode) - Break a Splunk ITSI episode  
[add episode comment](#action-add-episode-comment) - Add a comment to a Splunk ITSI episode  
[update episode](#action-update-episode) - Update Splunk ITSI episode status, severity and owner  
[get episode](#action-get-episode) - Get Splunk ITSI episode information  
[test connectivity](#action-test-connectivity) - Validate the asset configuration for connectivity using supplied configuration  

## action: 'end maintenance window'
End Splunk ITSI maintenance window

Type: **generic**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**maintenance\_window\_id** |  required  | Splunk ITSI maintenance window ID | string |  `splunk itsi maintenance window id` 
**comment** |  required  | Comment | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.comment | string | 
action\_result\.parameter\.maintenance\_window\_id | string |  `splunk itsi maintenance window id` 
action\_result\.data | string | 
action\_result\.data\.\*\.\_key | string | 
action\_result\.summary | string | 
action\_result\.summary\.status | string | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'update maintenance window'
Update Splunk ITSI maintenance window

Type: **generic**  
Read only: **False**

If 'start time' and 'relative start time' both will be provided, the 'start time' will be given priority\. Same as if 'end time' and 'relative end time' both will be provided, the 'end time' will be given priority\.

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**maintenance\_window\_id** |  required  | Splunk ITSI maintenance window ID | string |  `splunk itsi maintenance window id` 
**title** |  optional  | Maintenance window title | string | 
**relative\_start\_time** |  optional  | Relative start time in seconds\. To start maintenance window now \- 0, to start maintenance window after 5 mins \- 300, to start maintenance window after 1 hour \- 3600 | numeric | 
**relative\_end\_time** |  optional  | Relative end time in seconds\. To end maintenance window in 1 min from now \- 60, to end maintenance window after 5 mins \- 300, to end maintenance window after 1 hour \- 3600 | numeric | 
**start\_time** |  optional  | Start time \(epochtime in seconds\) | numeric | 
**end\_time** |  optional  | End time \(epochtime in seconds\) | numeric | 
**object\_type** |  optional  | Object type | string | 
**object\_ids** |  optional  | Object IDs \(comma separated list\) | string | 
**comment** |  optional  | Comment | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.comment | string | 
action\_result\.parameter\.end\_time | numeric | 
action\_result\.parameter\.maintenance\_window\_id | string |  `splunk itsi maintenance window id` 
action\_result\.parameter\.object\_ids | string | 
action\_result\.parameter\.object\_type | string | 
action\_result\.parameter\.relative\_end\_time | numeric | 
action\_result\.parameter\.relative\_start\_time | numeric | 
action\_result\.parameter\.start\_time | numeric | 
action\_result\.parameter\.title | string | 
action\_result\.data | string | 
action\_result\.data\.\*\.\_key | string | 
action\_result\.summary | string | 
action\_result\.summary\.status | string | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'add maintenance window'
Add Splunk ITSI maintenance window

Type: **generic**  
Read only: **False**

If 'start time' and 'relative start time' both will be provided, the 'start time' will be given priority\. Same as if 'end time' and 'relative end time' both will be provided, the 'end time' will be given priority\.

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**title** |  required  | Maintenance window title | string | 
**relative\_start\_time** |  optional  | Relative start time in seconds\. To start maintenance window now \- 0, to start maintenance window after 5 mins \- 300, to start maintenance window after 1 hour \- 3600 | numeric | 
**relative\_end\_time** |  optional  | Relative end time in seconds\. To end maintenance window in 1 min from now \- 60, to end maintenance window after 5 mins \- 300, to end maintenance window after 1 hour \- 3600 | numeric | 
**start\_time** |  optional  | Start time \(epochtime in seconds\) | numeric | 
**end\_time** |  optional  | End time \(epochtime in seconds\) | numeric | 
**object\_type** |  required  | Object type | string | 
**object\_ids** |  required  | Object IDs \(comma separated list\) | string | 
**comment** |  optional  | Comment | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.comment | string | 
action\_result\.parameter\.end\_time | numeric | 
action\_result\.parameter\.object\_ids | string | 
action\_result\.parameter\.object\_type | string | 
action\_result\.parameter\.relative\_end\_time | numeric | 
action\_result\.parameter\.relative\_start\_time | numeric | 
action\_result\.parameter\.start\_time | numeric | 
action\_result\.parameter\.title | string | 
action\_result\.data | string | 
action\_result\.data\.\*\.\_key | string |  `splunk itsi maintenance window id` 
action\_result\.summary | string | 
action\_result\.summary\.status | string | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'get maintenance window'
Get Splunk ITSI maintenance window information

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**maintenance\_window\_id** |  required  | Splunk ITSI maintenance window ID | string |  `splunk itsi maintenance window id` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.maintenance\_window\_id | string |  `splunk itsi maintenance window id` 
action\_result\.data | string | 
action\_result\.data\.\*\.\_key | string | 
action\_result\.data\.\*\.\_user | string | 
action\_result\.data\.\*\.\_version | string | 
action\_result\.data\.\*\.can\_edit | boolean | 
action\_result\.data\.\*\.comment | string | 
action\_result\.data\.\*\.end\_time | numeric | 
action\_result\.data\.\*\.identifying\_name | string | 
action\_result\.data\.\*\.mod\_source | string | 
action\_result\.data\.\*\.mod\_timestamp | string | 
action\_result\.data\.\*\.object\_type | string | 
action\_result\.data\.\*\.objects\.\*\.\_key | string | 
action\_result\.data\.\*\.objects\.\*\.object\_type | string | 
action\_result\.data\.\*\.start\_time | numeric | 
action\_result\.data\.\*\.title | string | 
action\_result\.summary | string | 
action\_result\.summary\.status | string | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'update service status'
Update Splunk ITSI service status

Type: **generic**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**itsi\_service\_id** |  required  | Splunk ITSI service ID | string |  `splunk itsi service id` 
**service\_status** |  required  | Update service status | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.itsi\_service\_id | string |  `splunk itsi service id` 
action\_result\.parameter\.service\_status | string | 
action\_result\.data | string | 
action\_result\.data\.\*\.\_key | string | 
action\_result\.summary | string | 
action\_result\.summary\.status | string | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'get service entities'
Get entities of a Splunk ITSI service

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**itsi\_service\_id** |  required  | Splunk ITSI service ID | string |  `splunk itsi service id` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.itsi\_service\_id | string |  `splunk itsi service id` 
action\_result\.data | string | 
action\_result\.data\.\*\.\*\.\_key | string |  `splunk itsi entity id` 
action\_result\.data\.\*\.\*\.\_owner | string | 
action\_result\.data\.\*\.\*\.\_type | string | 
action\_result\.data\.\*\.\*\.\_user | string | 
action\_result\.data\.\*\.\*\.\_version | string | 
action\_result\.data\.\*\.\*\.create\_by | string | 
action\_result\.data\.\*\.\*\.create\_source | string | 
action\_result\.data\.\*\.\*\.create\_time | string | 
action\_result\.data\.\*\.\*\.description | string | 
action\_result\.data\.\*\.\*\.identifying\_name | string | 
action\_result\.data\.\*\.\*\.mod\_source | string | 
action\_result\.data\.\*\.\*\.mod\_time | string | 
action\_result\.data\.\*\.\*\.mod\_timestamp | string | 
action\_result\.data\.\*\.\*\.object\_type | string | 
action\_result\.data\.\*\.\*\.permissions\.delete | boolean | 
action\_result\.data\.\*\.\*\.permissions\.group\.delete | boolean | 
action\_result\.data\.\*\.\*\.permissions\.group\.read | boolean | 
action\_result\.data\.\*\.\*\.permissions\.group\.write | boolean | 
action\_result\.data\.\*\.\*\.permissions\.read | boolean | 
action\_result\.data\.\*\.\*\.permissions\.user | string | 
action\_result\.data\.\*\.\*\.permissions\.write | boolean | 
action\_result\.data\.\*\.\*\.sec\_grp | string | 
action\_result\.data\.\*\.\*\.services\.\*\.\_key | string | 
action\_result\.data\.\*\.\*\.services\.\*\.title | string | 
action\_result\.data\.\*\.\*\.title | string | 
action\_result\.summary | string | 
action\_result\.summary\.status | string | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'get service'
Get Splunk ITSI service information

Type: **investigate**  
Read only: **True**

The KPI count in the output table will always be created KPIs \+ 1 \(inbuilt ServiceHealthScore KPI\)\.

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**itsi\_service\_id** |  required  | Splunk ITSI service ID | string |  `splunk itsi service id` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.itsi\_service\_id | string |  `splunk itsi service id` 
action\_result\.data | string | 
action\_result\.data\.\*\.\_key | string | 
action\_result\.data\.\*\.\_owner | string | 
action\_result\.data\.\*\.\_user | string | 
action\_result\.data\.\*\.\_version | string | 
action\_result\.data\.\*\.algorithms\.GradientBoostingRegressor\.RMSE | numeric | 
action\_result\.data\.\*\.algorithms\.GradientBoostingRegressor\.modelId | string | 
action\_result\.data\.\*\.algorithms\.GradientBoostingRegressor\.rSquared | numeric | 
action\_result\.data\.\*\.algorithms\.GradientBoostingRegressor\.recommended | boolean | 
action\_result\.data\.\*\.algorithms\.LinearRegression\.RMSE | numeric | 
action\_result\.data\.\*\.algorithms\.LinearRegression\.modelId | string | 
action\_result\.data\.\*\.algorithms\.LinearRegression\.rSquared | numeric | 
action\_result\.data\.\*\.algorithms\.LinearRegression\.recommended | boolean | 
action\_result\.data\.\*\.algorithms\.LogisticRegression\.accuracy | numeric | 
action\_result\.data\.\*\.algorithms\.LogisticRegression\.f1\_score | numeric | 
action\_result\.data\.\*\.algorithms\.LogisticRegression\.modelId | string | 
action\_result\.data\.\*\.algorithms\.LogisticRegression\.precision | numeric | 
action\_result\.data\.\*\.algorithms\.LogisticRegression\.recall | numeric | 
action\_result\.data\.\*\.algorithms\.LogisticRegression\.recommended | boolean | 
action\_result\.data\.\*\.algorithms\.RandomForestRegressor\.RMSE | numeric | 
action\_result\.data\.\*\.algorithms\.RandomForestRegressor\.modelId | string | 
action\_result\.data\.\*\.algorithms\.RandomForestRegressor\.rSquared | numeric | 
action\_result\.data\.\*\.algorithms\.RandomForestRegressor\.recommended | boolean | 
action\_result\.data\.\*\.backfill\_enabled | boolean | 
action\_result\.data\.\*\.base\_service\_template\_id | string | 
action\_result\.data\.\*\.description | string | 
action\_result\.data\.\*\.enabled | numeric | 
action\_result\.data\.\*\.entity\_rules\.\*\.rule\_condition | string | 
action\_result\.data\.\*\.entity\_rules\.\*\.rule\_items\.\*\.field | string | 
action\_result\.data\.\*\.entity\_rules\.\*\.rule\_items\.\*\.field\_type | string | 
action\_result\.data\.\*\.entity\_rules\.\*\.rule\_items\.\*\.rule\_type | string | 
action\_result\.data\.\*\.entity\_rules\.\*\.rule\_items\.\*\.value | string | 
action\_result\.data\.\*\.identifying\_name | string | 
action\_result\.data\.\*\.isFirstTimeSaveDone | boolean | 
action\_result\.data\.\*\.is\_healthscore\_calculate\_by\_entity\_enabled | numeric | 
action\_result\.data\.\*\.key | string | 
action\_result\.data\.\*\.kpis\.\*\.\_key | string | 
action\_result\.data\.\*\.kpis\.\*\.\_owner | string | 
action\_result\.data\.\*\.kpis\.\*\.active\_custom\_threshold\_window | string | 
action\_result\.data\.\*\.kpis\.\*\.adaptive\_thresholding\_training\_window | string | 
action\_result\.data\.\*\.kpis\.\*\.adaptive\_thresholds\_is\_enabled | boolean | 
action\_result\.data\.\*\.kpis\.\*\.aggregate\_eval | string | 
action\_result\.data\.\*\.kpis\.\*\.aggregate\_statop | string | 
action\_result\.data\.\*\.kpis\.\*\.aggregate\_thresholds\.baseSeverityColor | string | 
action\_result\.data\.\*\.kpis\.\*\.aggregate\_thresholds\.baseSeverityColorLight | string | 
action\_result\.data\.\*\.kpis\.\*\.aggregate\_thresholds\.baseSeverityLabel | string | 
action\_result\.data\.\*\.kpis\.\*\.aggregate\_thresholds\.baseSeverityValue | numeric | 
action\_result\.data\.\*\.kpis\.\*\.aggregate\_thresholds\.gaugeMax | numeric | 
action\_result\.data\.\*\.kpis\.\*\.aggregate\_thresholds\.gaugeMin | numeric | 
action\_result\.data\.\*\.kpis\.\*\.aggregate\_thresholds\.isMaxStatic | boolean | 
action\_result\.data\.\*\.kpis\.\*\.aggregate\_thresholds\.isMinStatic | boolean | 
action\_result\.data\.\*\.kpis\.\*\.aggregate\_thresholds\.metricField | string | 
action\_result\.data\.\*\.kpis\.\*\.aggregate\_thresholds\.renderBoundaryMax | numeric | 
action\_result\.data\.\*\.kpis\.\*\.aggregate\_thresholds\.renderBoundaryMin | numeric | 
action\_result\.data\.\*\.kpis\.\*\.aggregate\_thresholds\.search | string | 
action\_result\.data\.\*\.kpis\.\*\.aggregate\_thresholds\.thresholdLevels\.\*\.dynamicParam | numeric | 
action\_result\.data\.\*\.kpis\.\*\.aggregate\_thresholds\.thresholdLevels\.\*\.severityColor | string | 
action\_result\.data\.\*\.kpis\.\*\.aggregate\_thresholds\.thresholdLevels\.\*\.severityColorLight | string | 
action\_result\.data\.\*\.kpis\.\*\.aggregate\_thresholds\.thresholdLevels\.\*\.severityLabel | string | 
action\_result\.data\.\*\.kpis\.\*\.aggregate\_thresholds\.thresholdLevels\.\*\.severityValue | numeric | 
action\_result\.data\.\*\.kpis\.\*\.aggregate\_thresholds\.thresholdLevels\.\*\.thresholdValue | numeric | 
action\_result\.data\.\*\.kpis\.\*\.aggregate\_thresholds\_alert\_enabled | boolean | 
action\_result\.data\.\*\.kpis\.\*\.aggregate\_thresholds\_custom\_alert\_enabled | boolean | 
action\_result\.data\.\*\.kpis\.\*\.alert\_eval | string | 
action\_result\.data\.\*\.kpis\.\*\.alert\_lag | string | 
action\_result\.data\.\*\.kpis\.\*\.alert\_on | string | 
action\_result\.data\.\*\.kpis\.\*\.alert\_period | string | 
action\_result\.data\.\*\.kpis\.\*\.anomaly\_detection\_alerting\_enabled | boolean | 
action\_result\.data\.\*\.kpis\.\*\.anomaly\_detection\_is\_enabled | boolean | 
action\_result\.data\.\*\.kpis\.\*\.anomaly\_detection\_sensitivity | numeric | 
action\_result\.data\.\*\.kpis\.\*\.anomaly\_detection\_training\_window | string | 
action\_result\.data\.\*\.kpis\.\*\.appName | string | 
action\_result\.data\.\*\.kpis\.\*\.backfill\_earliest\_time | string | 
action\_result\.data\.\*\.kpis\.\*\.backfill\_enabled | boolean | 
action\_result\.data\.\*\.kpis\.\*\.base\_search | string | 
action\_result\.data\.\*\.kpis\.\*\.base\_search\_id | string | 
action\_result\.data\.\*\.kpis\.\*\.base\_search\_metric | string | 
action\_result\.data\.\*\.kpis\.\*\.cohesive\_ad\.sensitivity | numeric | 
action\_result\.data\.\*\.kpis\.\*\.cohesive\_anomaly\_detection\_is\_enabled | boolean | 
action\_result\.data\.\*\.kpis\.\*\.datamodel\.datamodel | string | 
action\_result\.data\.\*\.kpis\.\*\.datamodel\.field | string | 
action\_result\.data\.\*\.kpis\.\*\.datamodel\.object | string | 
action\_result\.data\.\*\.kpis\.\*\.datamodel\.owner\_field | string | 
action\_result\.data\.\*\.kpis\.\*\.datamodel\_filter\_clauses | string | 
action\_result\.data\.\*\.kpis\.\*\.description | string | 
action\_result\.data\.\*\.kpis\.\*\.enabled | numeric | 
action\_result\.data\.\*\.kpis\.\*\.entity\_alias\_filtering\_fields | string | 
action\_result\.data\.\*\.kpis\.\*\.entity\_breakdown\_id\_fields | string | 
action\_result\.data\.\*\.kpis\.\*\.entity\_id\_fields | string | 
action\_result\.data\.\*\.kpis\.\*\.entity\_statop | string | 
action\_result\.data\.\*\.kpis\.\*\.entity\_thresholds\.baseSeverityColor | string | 
action\_result\.data\.\*\.kpis\.\*\.entity\_thresholds\.baseSeverityColorLight | string | 
action\_result\.data\.\*\.kpis\.\*\.entity\_thresholds\.baseSeverityLabel | string | 
action\_result\.data\.\*\.kpis\.\*\.entity\_thresholds\.baseSeverityValue | numeric | 
action\_result\.data\.\*\.kpis\.\*\.entity\_thresholds\.gaugeMax | numeric | 
action\_result\.data\.\*\.kpis\.\*\.entity\_thresholds\.gaugeMin | numeric | 
action\_result\.data\.\*\.kpis\.\*\.entity\_thresholds\.isMaxStatic | boolean | 
action\_result\.data\.\*\.kpis\.\*\.entity\_thresholds\.isMinStatic | boolean | 
action\_result\.data\.\*\.kpis\.\*\.entity\_thresholds\.metricField | string | 
action\_result\.data\.\*\.kpis\.\*\.entity\_thresholds\.renderBoundaryMax | numeric | 
action\_result\.data\.\*\.kpis\.\*\.entity\_thresholds\.renderBoundaryMin | numeric | 
action\_result\.data\.\*\.kpis\.\*\.entity\_thresholds\.search | string | 
action\_result\.data\.\*\.kpis\.\*\.entity\_thresholds\.thresholdLevels\.\*\.dynamicParam | numeric | 
action\_result\.data\.\*\.kpis\.\*\.entity\_thresholds\.thresholdLevels\.\*\.severityColor | string | 
action\_result\.data\.\*\.kpis\.\*\.entity\_thresholds\.thresholdLevels\.\*\.severityColorLight | string | 
action\_result\.data\.\*\.kpis\.\*\.entity\_thresholds\.thresholdLevels\.\*\.severityLabel | string | 
action\_result\.data\.\*\.kpis\.\*\.entity\_thresholds\.thresholdLevels\.\*\.severityValue | numeric | 
action\_result\.data\.\*\.kpis\.\*\.entity\_thresholds\.thresholdLevels\.\*\.thresholdValue | numeric | 
action\_result\.data\.\*\.kpis\.\*\.eventstatop | string | 
action\_result\.data\.\*\.kpis\.\*\.fill\_gaps | string | 
action\_result\.data\.\*\.kpis\.\*\.gap\_custom\_alert\_value | string | 
action\_result\.data\.\*\.kpis\.\*\.gap\_severity | string | 
action\_result\.data\.\*\.kpis\.\*\.gap\_severity\_color | string | 
action\_result\.data\.\*\.kpis\.\*\.gap\_severity\_color\_light | string | 
action\_result\.data\.\*\.kpis\.\*\.gap\_severity\_value | string | 
action\_result\.data\.\*\.kpis\.\*\.is\_entity\_breakdown | boolean | 
action\_result\.data\.\*\.kpis\.\*\.is\_service\_entity\_filter | boolean | 
action\_result\.data\.\*\.kpis\.\*\.kpi\_base\_search | string | 
action\_result\.data\.\*\.kpis\.\*\.kpi\_template\_kpi\_id | string | 
action\_result\.data\.\*\.kpis\.\*\.kpi\_threshold\_template\_id | string | 
action\_result\.data\.\*\.kpis\.\*\.metric\.metric\_index | string | 
action\_result\.data\.\*\.kpis\.\*\.metric\.metric\_name | string | 
action\_result\.data\.\*\.kpis\.\*\.metric\_qualifier | string | 
action\_result\.data\.\*\.kpis\.\*\.search | string | 
action\_result\.data\.\*\.kpis\.\*\.search\_aggregate | string | 
action\_result\.data\.\*\.kpis\.\*\.search\_alert | string | 
action\_result\.data\.\*\.kpis\.\*\.search\_alert\_earliest | string | 
action\_result\.data\.\*\.kpis\.\*\.search\_alert\_entities | string | 
action\_result\.data\.\*\.kpis\.\*\.search\_buckets | string | 
action\_result\.data\.\*\.kpis\.\*\.search\_entities | string | 
action\_result\.data\.\*\.kpis\.\*\.search\_occurrences | numeric | 
action\_result\.data\.\*\.kpis\.\*\.search\_time\_compare | string | 
action\_result\.data\.\*\.kpis\.\*\.search\_time\_series | string | 
action\_result\.data\.\*\.kpis\.\*\.search\_time\_series\_aggregate | string | 
action\_result\.data\.\*\.kpis\.\*\.search\_time\_series\_entities | string | 
action\_result\.data\.\*\.kpis\.\*\.search\_type | string | 
action\_result\.data\.\*\.kpis\.\*\.sec\_grp | string | 
action\_result\.data\.\*\.kpis\.\*\.service\_id | string | 
action\_result\.data\.\*\.kpis\.\*\.service\_title | string | 
action\_result\.data\.\*\.kpis\.\*\.source | string | 
action\_result\.data\.\*\.kpis\.\*\.target | string | 
action\_result\.data\.\*\.kpis\.\*\.target\_field | string | 
action\_result\.data\.\*\.kpis\.\*\.threshold\_eval | string | 
action\_result\.data\.\*\.kpis\.\*\.threshold\_field | string | 
action\_result\.data\.\*\.kpis\.\*\.time\_variate\_thresholds | boolean | 
action\_result\.data\.\*\.kpis\.\*\.time\_variate\_thresholds\_specification\.policies\.default\_policy\.aggregate\_thresholds\.baseSeverityColor | string | 
action\_result\.data\.\*\.kpis\.\*\.time\_variate\_thresholds\_specification\.policies\.default\_policy\.aggregate\_thresholds\.baseSeverityColorLight | string | 
action\_result\.data\.\*\.kpis\.\*\.time\_variate\_thresholds\_specification\.policies\.default\_policy\.aggregate\_thresholds\.baseSeverityLabel | string | 
action\_result\.data\.\*\.kpis\.\*\.time\_variate\_thresholds\_specification\.policies\.default\_policy\.aggregate\_thresholds\.baseSeverityValue | numeric | 
action\_result\.data\.\*\.kpis\.\*\.time\_variate\_thresholds\_specification\.policies\.default\_policy\.aggregate\_thresholds\.gaugeMax | numeric | 
action\_result\.data\.\*\.kpis\.\*\.time\_variate\_thresholds\_specification\.policies\.default\_policy\.aggregate\_thresholds\.gaugeMin | numeric | 
action\_result\.data\.\*\.kpis\.\*\.time\_variate\_thresholds\_specification\.policies\.default\_policy\.aggregate\_thresholds\.isMaxStatic | boolean | 
action\_result\.data\.\*\.kpis\.\*\.time\_variate\_thresholds\_specification\.policies\.default\_policy\.aggregate\_thresholds\.isMinStatic | boolean | 
action\_result\.data\.\*\.kpis\.\*\.time\_variate\_thresholds\_specification\.policies\.default\_policy\.aggregate\_thresholds\.metricField | string | 
action\_result\.data\.\*\.kpis\.\*\.time\_variate\_thresholds\_specification\.policies\.default\_policy\.aggregate\_thresholds\.renderBoundaryMax | numeric | 
action\_result\.data\.\*\.kpis\.\*\.time\_variate\_thresholds\_specification\.policies\.default\_policy\.aggregate\_thresholds\.renderBoundaryMin | numeric | 
action\_result\.data\.\*\.kpis\.\*\.time\_variate\_thresholds\_specification\.policies\.default\_policy\.aggregate\_thresholds\.search | string | 
action\_result\.data\.\*\.kpis\.\*\.time\_variate\_thresholds\_specification\.policies\.default\_policy\.aggregate\_thresholds\.thresholdLevels\.\*\.dynamicParam | numeric | 
action\_result\.data\.\*\.kpis\.\*\.time\_variate\_thresholds\_specification\.policies\.default\_policy\.aggregate\_thresholds\.thresholdLevels\.\*\.severityColor | string | 
action\_result\.data\.\*\.kpis\.\*\.time\_variate\_thresholds\_specification\.policies\.default\_policy\.aggregate\_thresholds\.thresholdLevels\.\*\.severityColorLight | string | 
action\_result\.data\.\*\.kpis\.\*\.time\_variate\_thresholds\_specification\.policies\.default\_policy\.aggregate\_thresholds\.thresholdLevels\.\*\.severityLabel | string | 
action\_result\.data\.\*\.kpis\.\*\.time\_variate\_thresholds\_specification\.policies\.default\_policy\.aggregate\_thresholds\.thresholdLevels\.\*\.severityValue | numeric | 
action\_result\.data\.\*\.kpis\.\*\.time\_variate\_thresholds\_specification\.policies\.default\_policy\.aggregate\_thresholds\.thresholdLevels\.\*\.thresholdValue | numeric | 
action\_result\.data\.\*\.kpis\.\*\.time\_variate\_thresholds\_specification\.policies\.default\_policy\.entity\_thresholds\.baseSeverityColor | string | 
action\_result\.data\.\*\.kpis\.\*\.time\_variate\_thresholds\_specification\.policies\.default\_policy\.entity\_thresholds\.baseSeverityColorLight | string | 
action\_result\.data\.\*\.kpis\.\*\.time\_variate\_thresholds\_specification\.policies\.default\_policy\.entity\_thresholds\.baseSeverityLabel | string | 
action\_result\.data\.\*\.kpis\.\*\.time\_variate\_thresholds\_specification\.policies\.default\_policy\.entity\_thresholds\.baseSeverityValue | numeric | 
action\_result\.data\.\*\.kpis\.\*\.time\_variate\_thresholds\_specification\.policies\.default\_policy\.entity\_thresholds\.gaugeMax | numeric | 
action\_result\.data\.\*\.kpis\.\*\.time\_variate\_thresholds\_specification\.policies\.default\_policy\.entity\_thresholds\.gaugeMin | numeric | 
action\_result\.data\.\*\.kpis\.\*\.time\_variate\_thresholds\_specification\.policies\.default\_policy\.entity\_thresholds\.isMaxStatic | boolean | 
action\_result\.data\.\*\.kpis\.\*\.time\_variate\_thresholds\_specification\.policies\.default\_policy\.entity\_thresholds\.isMinStatic | boolean | 
action\_result\.data\.\*\.kpis\.\*\.time\_variate\_thresholds\_specification\.policies\.default\_policy\.entity\_thresholds\.metricField | string | 
action\_result\.data\.\*\.kpis\.\*\.time\_variate\_thresholds\_specification\.policies\.default\_policy\.entity\_thresholds\.renderBoundaryMax | numeric | 
action\_result\.data\.\*\.kpis\.\*\.time\_variate\_thresholds\_specification\.policies\.default\_policy\.entity\_thresholds\.renderBoundaryMin | numeric | 
action\_result\.data\.\*\.kpis\.\*\.time\_variate\_thresholds\_specification\.policies\.default\_policy\.entity\_thresholds\.search | string | 
action\_result\.data\.\*\.kpis\.\*\.time\_variate\_thresholds\_specification\.policies\.default\_policy\.policy\_type | string | 
action\_result\.data\.\*\.kpis\.\*\.time\_variate\_thresholds\_specification\.policies\.default\_policy\.title | string | 
action\_result\.data\.\*\.kpis\.\*\.time\_variate\_thresholds\_specification\.time\_blocks\.\*\.policy\_key | string | 
action\_result\.data\.\*\.kpis\.\*\.time\_variate\_thresholds\_specification\.time\_blocks\.\*\.time\_block\_key | string | 
action\_result\.data\.\*\.kpis\.\*\.title | string | 
action\_result\.data\.\*\.kpis\.\*\.trending\_ad\.sensitivity | numeric | 
action\_result\.data\.\*\.kpis\.\*\.type | string | 
action\_result\.data\.\*\.kpis\.\*\.tz\_offset | string | 
action\_result\.data\.\*\.kpis\.\*\.unit | string | 
action\_result\.data\.\*\.kpis\.\*\.urgency | string | 
action\_result\.data\.\*\.mod\_source | string | 
action\_result\.data\.\*\.mod\_time | string | 
action\_result\.data\.\*\.mod\_timestamp | string | 
action\_result\.data\.\*\.object\_type | string | 
action\_result\.data\.\*\.permissions\.delete | boolean | 
action\_result\.data\.\*\.permissions\.group\.delete | boolean | 
action\_result\.data\.\*\.permissions\.group\.read | boolean | 
action\_result\.data\.\*\.permissions\.group\.write | boolean | 
action\_result\.data\.\*\.permissions\.read | boolean | 
action\_result\.data\.\*\.permissions\.user | string | 
action\_result\.data\.\*\.permissions\.write | boolean | 
action\_result\.data\.\*\.sec\_grp | string | 
action\_result\.data\.\*\.serviceTemplateId | string | 
action\_result\.data\.\*\.service\_template\_id | string | 
action\_result\.data\.\*\.title | string | 
action\_result\.summary | string | 
action\_result\.summary\.status | string | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'get entity'
Get Splunk ITSI entity information

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**itsi\_entity\_id** |  required  | Splunk ITSI entity ID | string |  `splunk itsi entity id` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.itsi\_entity\_id | string |  `splunk itsi entity id` 
action\_result\.data | string | 
action\_result\.data\.\*\.\_key | string | 
action\_result\.data\.\*\.\_owner | string | 
action\_result\.data\.\*\.\_type | string | 
action\_result\.data\.\*\.\_user | string | 
action\_result\.data\.\*\.\_version | string | 
action\_result\.data\.\*\.create\_by | string | 
action\_result\.data\.\*\.create\_source | string | 
action\_result\.data\.\*\.create\_time | string | 
action\_result\.data\.\*\.description | string | 
action\_result\.data\.\*\.entity\_type\_ids | string | 
action\_result\.data\.\*\.identifying\_name | string | 
action\_result\.data\.\*\.mod\_source | string | 
action\_result\.data\.\*\.mod\_time | string | 
action\_result\.data\.\*\.mod\_timestamp | string | 
action\_result\.data\.\*\.object\_type | string | 
action\_result\.data\.\*\.permissions\.delete | boolean | 
action\_result\.data\.\*\.permissions\.group\.delete | boolean | 
action\_result\.data\.\*\.permissions\.group\.read | boolean | 
action\_result\.data\.\*\.permissions\.group\.write | boolean | 
action\_result\.data\.\*\.permissions\.read | boolean | 
action\_result\.data\.\*\.permissions\.user | string | 
action\_result\.data\.\*\.permissions\.write | boolean | 
action\_result\.data\.\*\.sec\_grp | string | 
action\_result\.data\.\*\.services\.\*\.\_key | string | 
action\_result\.data\.\*\.services\.\*\.title | string | 
action\_result\.data\.\*\.title | string | 
action\_result\.summary | string | 
action\_result\.summary\.status | string | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'get episode tickets'
Get ticket information for a Splunk ITSI episode

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**itsi\_group\_id** |  required  | Splunk ITSI episode ID | string |  `splunk itsi group id` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.itsi\_group\_id | string |  `splunk itsi group id` 
action\_result\.data | string | 
action\_result\.data\.\*\.\*\.\_key | string | 
action\_result\.data\.\*\.\*\.\_user | string | 
action\_result\.data\.\*\.\*\.create\_time | numeric | 
action\_result\.data\.\*\.\*\.event\_id | string | 
action\_result\.data\.\*\.\*\.itsi\_policy\_id | string | 
action\_result\.data\.\*\.\*\.mod\_time | numeric | 
action\_result\.data\.\*\.\*\.object\_type | string | 
action\_result\.data\.\*\.\*\.ticket\_system | string | 
action\_result\.data\.\*\.\*\.tickets\.\*\.ticket\_id | string | 
action\_result\.data\.\*\.\*\.tickets\.\*\.ticket\_system | string | 
action\_result\.data\.\*\.\*\.tickets\.\*\.ticket\_url | string | 
action\_result\.summary | string | 
action\_result\.summary\.status | string | 
action\_result\.summary\.total\_episode\_tickets | numeric | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'add episode ticket'
Add a ticket to a Splunk ITSI episode

Type: **generic**  
Read only: **False**

Include http\:// or https\:// in the 'ticket url' action parameter\. Otherwise the URL is interpreted as a relative URI\.

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**itsi\_group\_id** |  required  | Splunk ITSI episode ID | string |  `splunk itsi group id` 
**ticket\_system** |  required  | Name of the ticketing system | string | 
**ticket\_id** |  required  | Ticket ID in the ticketing system | string | 
**ticket\_url** |  optional  | Ticket URL in the ticketing system | string | 
**custom\_ticketing\_system\_name** |  optional  | Custom ticketing system name | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.custom\_ticketing\_system\_name | string | 
action\_result\.parameter\.itsi\_group\_id | string |  `splunk itsi group id` 
action\_result\.parameter\.ticket\_id | string | 
action\_result\.parameter\.ticket\_system | string | 
action\_result\.parameter\.ticket\_url | string | 
action\_result\.data | string | 
action\_result\.summary | string | 
action\_result\.summary\.status | string | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'get episode events'
Get latest events for Splunk ITSI episode

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**itsi\_group\_id** |  required  | Splunk ITSI episode ID | string |  `splunk itsi group id` 
**earliest\_time** |  required  | Earliest time to search\. Select from the drop down or enter relative time modifiers \- \-60m for 60 minutes ago, \-24h for 24 hours ago\. Ref\: https\://docs\.splunk\.com/Documentation/Splunk/8\.0\.1/Search/Specifytimemodifiersinyoursearch | string | 
**max\_results** |  required  | Max results retrieved by the search | numeric | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.earliest\_time | string | 
action\_result\.parameter\.itsi\_group\_id | string |  `splunk itsi group id` 
action\_result\.parameter\.max\_results | numeric | 
action\_result\.data | string | 
action\_result\.data\.\*\.\_bkt | string | 
action\_result\.data\.\*\.\_cd | string | 
action\_result\.data\.\*\.\_indextime | string | 
action\_result\.data\.\*\.\_mkv\_child | string | 
action\_result\.data\.\*\.\_raw | string | 
action\_result\.data\.\*\.\_serial | string | 
action\_result\.data\.\*\.\_sourcetype | string | 
action\_result\.data\.\*\.\_subsecond | string | 
action\_result\.data\.\*\.\_time | string | 
action\_result\.data\.\*\.alert\_type | string | 
action\_result\.data\.\*\.all\_service\_kpi\_ids | string | 
action\_result\.data\.\*\.description | string | 
action\_result\.data\.\*\.drilldown\_search\_earliest\_offset | string | 
action\_result\.data\.\*\.drilldown\_search\_latest\_offset | string | 
action\_result\.data\.\*\.drilldown\_search\_search | string | 
action\_result\.data\.\*\.drilldown\_search\_title | string | 
action\_result\.data\.\*\.event\_id | string | 
action\_result\.data\.\*\.event\_identifier\_fields | string | 
action\_result\.data\.\*\.event\_identifier\_hash | string | 
action\_result\.data\.\*\.event\_identifier\_string | string | 
action\_result\.data\.\*\.host | string | 
action\_result\.data\.\*\.index | string | 
action\_result\.data\.\*\.itsiAlert | string | 
action\_result\.data\.\*\.itsiInstance | string | 
action\_result\.data\.\*\.itsiSeverity | string | 
action\_result\.data\.\*\.itsiSubInstance | string | 
action\_result\.data\.\*\.itsi\_action\_rule\_keys | string | 
action\_result\.data\.\*\.itsi\_earliest\_event\_time | string | 
action\_result\.data\.\*\.itsi\_first\_event\_id | string | 
action\_result\.data\.\*\.itsi\_first\_event\_time | string | 
action\_result\.data\.\*\.itsi\_group\_assignee | string | 
action\_result\.data\.\*\.itsi\_group\_count | string | 
action\_result\.data\.\*\.itsi\_group\_description | string | 
action\_result\.data\.\*\.itsi\_group\_id | string | 
action\_result\.data\.\*\.itsi\_group\_instruction | string | 
action\_result\.data\.\*\.itsi\_group\_severity | string | 
action\_result\.data\.\*\.itsi\_group\_status | string | 
action\_result\.data\.\*\.itsi\_group\_title | string | 
action\_result\.data\.\*\.itsi\_is\_first\_event | string | 
action\_result\.data\.\*\.itsi\_is\_last\_event | string | 
action\_result\.data\.\*\.itsi\_last\_event\_time | string | 
action\_result\.data\.\*\.itsi\_parent\_group\_id | string | 
action\_result\.data\.\*\.itsi\_policy\_id | string | 
action\_result\.data\.\*\.itsi\_service\_ids | string | 
action\_result\.data\.\*\.itsi\_split\_by\_hash | string | 
action\_result\.data\.\*\.kpi\_title | string | 
action\_result\.data\.\*\.kpiid | string | 
action\_result\.data\.\*\.linecount | string | 
action\_result\.data\.\*\.mod\_time | string | 
action\_result\.data\.\*\.orig\_raw | string | 
action\_result\.data\.\*\.orig\_time | string | 
action\_result\.data\.\*\.owner | string | 
action\_result\.data\.\*\.punct | string | 
action\_result\.data\.\*\.service\_title | string | 
action\_result\.data\.\*\.severity | string | 
action\_result\.data\.\*\.source | string | 
action\_result\.data\.\*\.sourcetype | string | 
action\_result\.data\.\*\.splunk\_server | string | 
action\_result\.data\.\*\.status | string | 
action\_result\.data\.\*\.title | string | 
action\_result\.summary | string | 
action\_result\.summary\.status | string | 
action\_result\.summary\.total\_episode\_events | numeric | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'close episode'
Close a Splunk ITSI episode

Type: **generic**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**itsi\_group\_id** |  required  | Splunk ITSI episode ID | string |  `splunk itsi group id` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.itsi\_group\_id | string |  `splunk itsi group id` 
action\_result\.data | string | 
action\_result\.data\.\*\.\_key | string | 
action\_result\.summary | string | 
action\_result\.summary\.status | string | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'break episode'
Break a Splunk ITSI episode

Type: **generic**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**itsi\_group\_id** |  required  | Splunk ITSI episode ID | string |  `splunk itsi group id` 
**itsi\_policy\_id** |  required  | Splunk ITSI notable event aggregation policy ID | string |  `splunk itsi policy id` 
**status** |  required  | Episode status | string | 
**title** |  required  | Episode title | string | 
**description** |  required  | Episode descripton | string | 
**severity** |  required  | Episode severity | string | 
**owner** |  required  | Episode owner | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.description | string | 
action\_result\.parameter\.itsi\_group\_id | string |  `splunk itsi group id` 
action\_result\.parameter\.itsi\_policy\_id | string |  `splunk itsi policy id` 
action\_result\.parameter\.owner | string | 
action\_result\.parameter\.severity | string | 
action\_result\.parameter\.status | string | 
action\_result\.parameter\.title | string | 
action\_result\.data | string | 
action\_result\.summary | string | 
action\_result\.summary\.status | string | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'add episode comment'
Add a comment to a Splunk ITSI episode

Type: **generic**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**itsi\_group\_id** |  required  | Splunk ITSI episode ID | string |  `splunk itsi group id` 
**comment** |  required  | Comment to add | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.comment | string | 
action\_result\.parameter\.itsi\_group\_id | string |  `splunk itsi group id` 
action\_result\.data | string | 
action\_result\.data\.\*\.comment | string | 
action\_result\.data\.\*\.comment\_id | string | 
action\_result\.data\.\*\.create\_time | string | 
action\_result\.data\.\*\.itsi\_policy\_id | string | 
action\_result\.data\.\*\.mod\_time | string | 
action\_result\.data\.\*\.owner | string | 
action\_result\.data\.\*\.user | string | 
action\_result\.summary | string | 
action\_result\.summary\.comment\_id | string | 
action\_result\.summary\.itsi\_group\_id | string | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'update episode'
Update Splunk ITSI episode status, severity and owner

Type: **generic**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**itsi\_group\_id** |  required  | Splunk ITSI episode ID | string |  `splunk itsi group id` 
**status** |  optional  | Episode status | string | 
**severity** |  optional  | Episode severity | string | 
**owner** |  optional  | Episode owner | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.itsi\_group\_id | string |  `splunk itsi group id` 
action\_result\.parameter\.owner | string | 
action\_result\.parameter\.severity | string | 
action\_result\.parameter\.status | string | 
action\_result\.data | string | 
action\_result\.data\.\*\.\_key | string | 
action\_result\.summary | string | 
action\_result\.summary\.status | string | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'get episode'
Get Splunk ITSI episode information

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**itsi\_group\_id** |  required  | Splunk ITSI episode ID | string |  `splunk itsi group id` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.itsi\_group\_id | string |  `splunk itsi group id` 
action\_result\.data | string | 
action\_result\.data\.\*\.\_key | string | 
action\_result\.data\.\*\.\_user | string | 
action\_result\.data\.\*\.description | string | 
action\_result\.data\.\*\.earliest\_time | string | 
action\_result\.data\.\*\.event\_identifier\_hash | string | 
action\_result\.data\.\*\.instruction | string | 
action\_result\.data\.\*\.is\_partial\_data | string | 
action\_result\.data\.\*\.itsi\_policy\_id | string |  `splunk itsi policy id` 
action\_result\.data\.\*\.latest\_time | string | 
action\_result\.data\.\*\.mod\_time | numeric | 
action\_result\.data\.\*\.object\_type | string | 
action\_result\.data\.\*\.owner | string | 
action\_result\.data\.\*\.severity | string | 
action\_result\.data\.\*\.status | string | 
action\_result\.data\.\*\.title | string | 
action\_result\.summary | string | 
action\_result\.summary\.status | string | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'test connectivity'
Validate the asset configuration for connectivity using supplied configuration

Type: **test**  
Read only: **True**

#### Action Parameters
No parameters are required for this action

#### Action Output
No Output