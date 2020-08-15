[![PyPi](https://img.shields.io/pypi/v/hass-metlink-api.svg)](https://pypi.python.org/pypi/hass-metlink-api)
[![Version](https://img.shields.io/pypi/pyversions/hass-metlink-api.svg)](https://pypi.python.org/pypi/hass-metlink-api)


# Hass Metlink API
A Metlink Wellington API Data Manager for Home Assistant.

This library provides convenient async access to Metlink Wellington transport network stop departure 
information using the undocumented Metlink Wellington API.

## Installation
`pip install hass-metlink-api` or use with Home Assistant Metlink Wellington Integration.

## Usage
After instantiating the MetlinkDataManager class, there are four functions that can be called
by supplying the required parameters. 

See below for examples of how these functions can be used.  

1. MetlinkDataManager.async_met_get

This function attempts to retrieve stop and departure information for the selected stop_id from the Metlink API.

**Parameters**

| Parameter          | Description                               |
|--------------------|-------------------------------------------|
| `stop_id` | The stop/station/wharf id |

Two variables are returned: 1. Status code 2. API data or none

The status code return value will be a tuple indicating the type of status. 

If data is sucessfully returned the API information is a JSON serialised nested dictonary. An example of the data returned is:

{"LastModified":"2020-08-10T18:12:28+12:00","Stop":{"Name":"Wellington Station","Sms":"WELL","Farezone":"1","Lat":-41.2789686,"Long":174.7805617,"LastModified":"2020-08-10T00:02:10+12:00"},"Notices":[{"RecordedAtTime":"2020-08-10T18:12:21+12:00","MonitoringRef":"WELL","LineRef":"","DirectionRef":"","LineNote":"HVL: Today - Some evening services between\nWELL and UPPE will be replaced by bus. See\nmetlink.org.nz for more info"}],"Services":[{"ServiceID":"HVL","IsRealtime":true,"VehicleRef":"4264","Direction":"Outbound","OperatorRef":"RAIL","OriginStopID":"WELL","OriginStopName":"WgtnStn","DestinationStopID":"TAIT2","DestinationStopName":"TAIT-All stops","AimedArrival":null,"AimedDeparture":"2020-08-10T18:11:00+12:00","VehicleFeature":null,"DepartureStatus":"onTime","ExpectedDeparture":"2020-08-10T18:12:31+12:00","DisplayDeparture":"2020-08-10T18:12:31+12:00","DisplayDepartureSeconds":10,"Service":{"Code":"HVL","TrimmedCode":"HVL","Name":"Hutt Valley Line (Upper Hutt - Wellington)","Mode":"Train","Link":"\/timetables\/train\/HVL"}},{"ServiceID":"KPL","IsRealtime":true,"VehicleRef":"4283","Direction":"Outbound","OperatorRef":"RAIL","OriginStopID":"WELL","OriginStopName":"WgtnStn","DestinationStopID":"WAIK","DestinationStopName":"WAIK-All stops","AimedArrival":null,"AimedDeparture":"2020-08-10T18:14:00+12:00","VehicleFeature":null,"DepartureStatus":"onTime","ExpectedDeparture":"2020-08-10T18:14:00+12:00","DisplayDeparture":"2020-08-10T18:14:00+12:00","DisplayDepartureSeconds":99,"Service":{"Code":"KPL","TrimmedCode":"KPL","Name":"Kapiti Line (Waikanae - Wellington)","Mode":"Train","Link":"\/timetables\/train\/KPL"}},{"ServiceID":"JVL","IsRealtime":false,"VehicleRef":null,"Direction":"Outbound","OperatorRef":"RAIL","OriginStopID":"WELL","OriginStopName":"WgtnStn","DestinationStopID":"JOHN","DestinationStopName":"JOHN-All stops","AimedArrival":null,"AimedDeparture":"2020-08-10T18:17:00+12:00","VehicleFeature":null,"DepartureStatus":null,"ExpectedDeparture":null,"DisplayDeparture":"2020-08-10T18:17:00+12:00","DisplayDepartureSeconds":279,"Service":{"Code":"JVL","TrimmedCode":"JVL","Name":"Johnsonville Line (Johnsonville - Wellington)","Mode":"Train","Link":"\/timetables\/train\/JVL"}},

An explanation of the data returned by the API is:

A single stop and multiple services that depart from the stop location.

Record | Explanation
------------ | -------------
Stop: |
Name | The name of the stop/station/wharf
SMS | The number or ID for the stop/station/wharf
Farezone | The zone which is used to determine the fare when travelling in a zone or between zones
Lat | Latitude for the location of the stop/station/wharf
Long | Longitude for the location of the stop/station/wharf 
Last Modified | The date and time the stop information was last updated
Notices | Any notices issued for the stop
Services: |
ServiceID | The number or ID for the route (service)
IsRealTime | Displays true if the info is realtime, otherwise is blank
VehicleRef | The number or ID of the bus/train/ferry
Direction | Inbound or Outbound to the stop
OperatorRef | The business operating the service e.g. RAIL or a bus company 
OriginStopID | The number or ID for the stop/station/wharf the service commences from 
OriginStopName | The name of the stop/station/wharf the service commences from
DestinationStopID | The number or ID of the stop/station/wharf where the service will finish the route
DestinationStopName | The name of the stop/station/wharf where the service will finish the route
AimedArrival | The date and time the service is scheduled to arrive at the stop
AimedDeparture | The date and time the service is scheduled to depart from the stop
VehicleFeature | Displays any special features of the service e.g. a bus that can drop low to allow a wheelchair to enter
DepartureStatus | Displays whether the service is on time or if there is a delay from the expected time (real time service only)
ExpectedDeparture |  The date and time the next service is expected to depart from the location (real time service only)
DisplayDeparture | The date and time to display to customers (Expected if available otherwise Aimed)
DisplayDepartureSeconds | The number of seconds until the service will depart
Code | The number or ID for the route (service)
TrimmedCode | The number or ID for the route (service)
Name | The name of the route (service)
Mode | The type of vehicle used for the service: bus, train, or ferry
Link | The location on the metlink website where the timetable for the route is available

If the data is retrieved then an ok status code is returned.  

If there are problems retrieving the data then an error result will be returned (see below) for the status code, and the API data variable will return None.

Status Codes

| Status code          | Description                               |
|--------------------|-------------------------------------------|
| `"no_net": "error"` | Network connection error  |
| `"no_reply": "error"` | Connection timeout error  |
| `"not_id": "invalid"` | Invalid stop id provided  |
| `"no_api": "n/a"` | No data was received from the server  |
| `"no_err": "ok"` | Data was sucessfully retrieved from the server  |
| `"not_known": "error"` | Something went wrong during the request  |

2. MetlinkDataManager.async_met_assess

This function is designed to be used with Home Assistant.

Three variables are returned: 1. State code  2. Flattened data or none  3. Position of services or none 

It assesses the nature of the status code, and if the status is not ok, then logs an error message and sets a state for a Home Assistant entity.

If the status is ok, it then uses the flatten_data function to flatten the nested data (each service is identified by adding a number to each key), and identify the postion of services in the data for a desired route using the services_filter function. It then returns the flattened data and the positon of the services for the route. If the route does not exist at the stop then it returns an error in place of the position of the services for the route. 

An example of the flattened data is:

OrderedDict([('LastModified', '2020-07-12T14:16:54+12:00'), ('Stop_Name', 'Crofton Downs Station'), ('Stop_Sms', 'CROF'), ('Stop_Farezone', '3'), ('Stop_Lat', -41.2550408), ('Stop_Long', 174.7664988), ('Stop_LastModified', '2020-07-12T00:02:14+12:00'), ('Notices_0_RecordedAtTime', '2020-07-12T14:16:54+12:00'), ('Notices_0_MonitoringRef', 'CROF'), ('Notices_0_LineRef', ''), ('Notices_0_DirectionRef', ''), ('Notices_0_LineNote', 'JVL: Regular fares and ticketing now applies, have your tickets ready for inspection. See Metlink.org.nz for more info.'), ('Notices_1_RecordedAtTime', '2020-07-12T14:16:54+12:00'), ('Notices_1_MonitoringRef', 'CROF'), ('Notices_1_LineRef', ''), ('Notices_1_DirectionRef', ''), ('Notices_1_LineNote', 'JVL: Additional carriages and extra services operating today for Super Rugby. See metlink.org.nz for more info'), ('Services_0_ServiceID', 'JVL'), ('Services_0_IsRealtime', True), ('Services_0_VehicleRef', '4155'), ('Services_0_Direction', 'Inbound'), ('Services_0_OperatorRef', 'RAIL'), ('Services_0_OriginStopID', 'JOHN'), ('Services_0_OriginStopName', 'JohnsonvilleStn'), ('Services_0_DestinationStopID', 'WELL'), ('Services_0_DestinationStopName', 'WELL-All stops'), ('Services_0_AimedArrival', '2020-07-12T14:14:00+12:00'), ('Services_0_AimedDeparture', '2020-07-12T14:14:00+12:00'), ('Services_0_VehicleFeature', None), ('Services_0_DepartureStatus', 'delayed'), ('Services_0_ExpectedDeparture', '2020-07-12T14:18:42+12:00'), ('Services_0_DisplayDeparture', '2020-07-12T14:18:42+12:00'), ('Services_0_DisplayDepartureSeconds', 108), ('Services_0_Service_Code', 'JVL'), ('Services_0_Service_TrimmedCode', 'JVL'), ('Services_0_Service_Name', 'Johnsonville Line (Johnsonville - Wellington)'), ('Services_0_Service_Mode', 'Train'), ('Services_0_Service_Link', '/timetables/train/JVL'), ('Services_1_ServiceID', 'JVL'), ('Services_1_IsRealtime', False), ('Services_1_VehicleRef', None), ('Services_1_Direction', 'Outbound'), ('Services_1_OperatorRef', 'RAIL'), ('Services_1_OriginStopID', 'WELL'), ('Services_1_OriginStopName', 'WgtnStn'), ('Services_1_DestinationStopID', 'JOHN'), ('Services_1_DestinationStopName', 'JOHN-All stops'), ('Services_1_AimedArrival', '2020-07-12T14:40:00+12:00'), ('Services_1_AimedDeparture', '2020-07-12T14:40:00+12:00'), ('Services_1_VehicleFeature', None), ('Services_1_DepartureStatus', None), ('Services_1_ExpectedDeparture', None), ('Services_1_DisplayDeparture', '2020-07-12T14:40:00+12:00'), ('Services_1_DisplayDepartureSeconds', 1386), ('Services_1_Service_Code', 'JVL'), ('Services_1_Service_TrimmedCode', 'JVL'), ('Services_1_Service_Name', 'Johnsonville Line (Johnsonville - Wellington)'), ('Services_1_Service_Mode', 'Train'), ('Services_1_Service_Link', '/timetables/train/JVL')

**Parameters**

| Parameter          | Description                               |
|--------------------|-------------------------------------------|
| `status` | Status code returned by async_met_get function  |
| `data` | API data dictionary returned by async_met_get function if available |
| `available` | The current availability of the Home Assistant entity - True or False |
| `route_id` | The route id for the desired service at the stop location |
| `ser_n` | The number of services for the route at the stop that you wish to retrieve from the data |

3. MetlinkDataManager.flatten_data

Returns one variable: The flattened data dictonary.

This function flattens the nested data dictonary into a flat data dictonary. The tuples for each previously nested service are now seperately identified by adding a number to each key (see above for example of flattened data).  

**Parameters**

| Parameter          | Description                               |
|--------------------|-------------------------------------------|
| `jdata` | API data dictionary returned by async_met_get function  |
| `sep` | Seperator used to seperate number from key name. Preset to an underscore |

4. MetlinkDataManager.services_filter

Returns one variable: a. List of the numbered positons for the services for the route or 2. an error value  

Function identifies the postion of services in the data for a desired route. It then returns the positon of the services for the route. If the route does not exist at the stop then it returns an error in place of the position of the services for the route. 

The services data for the route can be extracted from the flattened data using a call if their position in the data dictonary is known.  

| Parameter          | Description                               |
|--------------------|-------------------------------------------|
| `flat_data` | Flattened data dictionary returned by flatten_data function  |
| `route` | The route at the stop for which services will be identified in the data |
| `ser_num` | The number of service records for the route to identify |

