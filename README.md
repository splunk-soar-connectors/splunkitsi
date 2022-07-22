[comment]: # "Auto-generated SOAR connector documentation"
# Splunk IT Service Intelligence for SOAR

Publisher: Splunk Community  
Connector Version: 1\.0\.3  
Product Vendor: Splunk  
Product Name: Splunk ITSI  
Product Version Supported (regex): "\.\*"  
Minimum Product Version: 4\.8\.24304  

This app integrates with Splunk IT Service Intelligence to provide operations on Splunk IT Service Intelligence episodes, services, entities, and object maintenance

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
**maintenance\_window\_id** |  required  | Splunk ITSI maintenance window ID | string | 
**comment** |  required  | Comment | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.parameter\.maintenance\_window\_id | string | 
action\_result\.parameter\.comment | string | 
action\_result\.data | string | 
action\_result\.summary | string | 
action\_result\.status | string | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'update maintenance window'
Update Splunk ITSI maintenance window

Type: **generic**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**maintenance\_window\_id** |  required  | Splunk ITSI maintenance window ID | string | 
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
action\_result\.parameter\.maintenance\_window\_id | string | 
action\_result\.parameter\.title | string | 
action\_result\.parameter\.relative\_end\_time | numeric | 
action\_result\.parameter\.relative\_start\_time | numeric | 
action\_result\.parameter\.start\_time | numeric | 
action\_result\.parameter\.end\_time | numeric | 
action\_result\.parameter\.object\_type | string | 
action\_result\.parameter\.object\_ids | string | 
action\_result\.parameter\.comment | string | 
action\_result\.data | string | 
action\_result\.summary | string | 
action\_result\.status | string | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'add maintenance window'
Add Splunk ITSI maintenance window

Type: **generic**  
Read only: **False**

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
action\_result\.parameter\.title | string | 
action\_result\.parameter\.relative\_start\_time | numeric | 
action\_result\.parameter\.relative\_end\_time | numeric | 
action\_result\.parameter\.start\_time | numeric | 
action\_result\.parameter\.end\_time | numeric | 
action\_result\.parameter\.object\_type | string | 
action\_result\.parameter\.object\_ids | string | 
action\_result\.parameter\.comment | string | 
action\_result\.data | string | 
action\_result\.summary | string | 
action\_result\.status | string | 
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
**maintenance\_window\_id** |  required  | Splunk ITSI maintenance window ID | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.parameter\.maintenance\_window\_id | string | 
action\_result\.data | string | 
action\_result\.summary | string | 
action\_result\.status | string | 
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
action\_result\.parameter\.itsi\_service\_id | string |  `splunk itsi service id` 
action\_result\.parameter\.service\_status | string | 
action\_result\.data | string | 
action\_result\.summary | string | 
action\_result\.status | string | 
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
action\_result\.parameter\.itsi\_service\_id | string |  `splunk itsi service id` 
action\_result\.data | string | 
action\_result\.summary | string | 
action\_result\.status | string | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'get service'
Get Splunk ITSI service information

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**itsi\_service\_id** |  required  | Splunk ITSI service ID | string |  `splunk itsi service id` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.parameter\.itsi\_service\_id | string |  `splunk itsi service id` 
action\_result\.data | string | 
action\_result\.summary | string | 
action\_result\.status | string | 
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
**itsi\_entity\_id** |  required  | Splunk ITSI entity ID | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.parameter\.itsi\_entity\_id | string | 
action\_result\.data | string | 
action\_result\.summary | string | 
action\_result\.status | string | 
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
action\_result\.parameter\.itsi\_group\_id | string |  `splunk itsi group id` 
action\_result\.data | string | 
action\_result\.summary | string | 
action\_result\.status | string | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'add episode ticket'
Add a ticket to a Splunk ITSI episode

Type: **generic**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**itsi\_group\_id** |  required  | Splunk ITSI episode ID | string |  `splunk itsi group id` 
**ticket\_system** |  optional  | Name of the ticketing system | string | 
**ticket\_id** |  optional  | Ticket ID in the ticketing system | string | 
**ticket\_url** |  optional  | Ticket URL in the ticketing system | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.parameter\.itsi\_group\_id | string |  `splunk itsi group id` 
action\_result\.parameter\.ticket\_system | string | 
action\_result\.parameter\.ticket\_id | string | 
action\_result\.parameter\.ticket\_url | string | 
action\_result\.data | string | 
action\_result\.summary | string | 
action\_result\.status | string | 
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
**max\_results** |  required  | Max results retrieved by the search | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.parameter\.itsi\_group\_id | string |  `splunk itsi group id` 
action\_result\.parameter\.earliest\_time | string | 
action\_result\.parameter\.max\_results | string | 
action\_result\.data | string | 
action\_result\.summary | string | 
action\_result\.status | string | 
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
**break\_episode** |  optional  | Break episode | boolean | 
**itsi\_policy\_id** |  required  | Splunk ITSI notable event aggregation policy ID | string |  `splunk itsi policy id` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.parameter\.itsi\_group\_id | string |  `splunk itsi group id` 
action\_result\.parameter\.break\_episode | boolean | 
action\_result\.parameter\.itsi\_policy\_id | string |  `splunk itsi policy id` 
action\_result\.data | string | 
action\_result\.summary | string | 
action\_result\.status | string | 
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

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.parameter\.itsi\_group\_id | string |  `splunk itsi group id` 
action\_result\.parameter\.itsi\_policy\_id | string |  `splunk itsi policy id` 
action\_result\.data | string | 
action\_result\.summary | string | 
action\_result\.status | string | 
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
action\_result\.parameter\.itsi\_group\_id | string |  `splunk itsi group id` 
action\_result\.parameter\.comment | string | 
action\_result\.data | string | 
action\_result\.summary | string | 
action\_result\.status | string | 
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
action\_result\.parameter\.itsi\_group\_id | string |  `splunk itsi group id` 
action\_result\.parameter\.status | string | 
action\_result\.parameter\.severity | string | 
action\_result\.parameter\.owner | string | 
action\_result\.data | string | 
action\_result\.summary | string | 
action\_result\.status | string | 
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
action\_result\.parameter\.itsi\_group\_id | string |  `splunk itsi group id` 
action\_result\.data | string | 
action\_result\.summary | string | 
action\_result\.status | string | 
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