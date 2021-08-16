# GVE DevNet DNAC API Examples

This repository contains examples of how to use the [DNA Center REST API](https://developer.cisco.com/docs/dna-center/#!cisco-dna-2-2-3-api-overview) using Python and the `requests` library. 

## Contacts
* Simon Fang (sifang@cisco.com)
* Ramona Renner (ramrenne@cisco.com)

## Solution Components
* DNA Center
* Python
* `requests` library

## Pre-requisites
* DNA Center Lab
* DNA Center API Token
> Please note that the section `DNA Center API Token` explains how to obtain this token

## Installation/Configuration
The following commands are executed in the terminal.

1. Create and activate a virtual environment for the project:
   
        #WINDOWS:
        $ py -3 -m venv [add_name_of_virtual_environment_here] 
        $ source [add_name_of_virtual_environment_here]/Scripts/activate
        #MAC:
        $ python3 -m venv [add_name_of_virtual_environment_here] 
        $ source [aadd_name_of_virtual_environment_here]/bin/activate
        

> For more information about virtual environments, please click [here](https://docs.python.org/3/tutorial/venv.html)

2. Access the created virutal environment folder

        $ cd [add_name_of_virtual_environment_here]

3. Clone this repository

        $ git clone [add_link_to_repository_here]

4. Access the folder `GVE_DevNet_DNA_API_Examples`

        $ cd GVE_DevNet_DNA_API_Examples

5. Install the dependencies:

        $ pip install -r requirements.txt

## DNA Center API Token

In order to use the DNA Center API, we need to obtain a DNA Center API Token. The token is needed for authentication purposes. Follow the following instructions in order to obtain an API token:

1. Open the `env.py`file and fill in the following details: 

    ```python
    dnac_host = ""
    dnac_username = ""
    dnac_password = ""
    ```
    An example of these details can be obtained from the DevNet sandbox and are as follows:

    * **Url/dnac_host:** `https://sandboxdnac2.cisco.com`
    * **Username:** `devnetuser`
    * **Password:** `Cisco123!` 


2. Open the terminal and execute the following command:

        $ python 0_auth.py

    You will obtain the following response: 

        { 'Token': 'example_token' }

3. Open the `env.py` file and paste the token here: 

    ```python
    token = "example_token"
    ```

## Environment Variables

1. Open the `env.py` file and make sure that you have added the missing values of `dnac_host`, `dnac_username`, `dnac_password` and `token`. The other values are only required for some of the following scripts. Please note, see section `DNA Center API Token` for information on how to obtain the `dnac_host`, `dnac_username`, `dnac_password` and `token`:
    
    ```python
    dnac_host = "" #Please see section DNA Center API Token
    dnac_username = "" #Please see section DNA Center API Token
    dnac_password = "" #Please see section DNA Center API Token
    token = "" #Please see section DNA Center API Token

    # Below is optional, only for script 1:
    entity_type = "" # must either be `network_user_id` or `mac_address`
    entity_value = "" # contains the actual value for the entity type that has been defined

    # Below is optional, only for script 4, 8:
    siteId = ""

    # Below is optional, only for script 10:
    deviceUuid = ""
    taskId = ""
    fileId = ""

    # Below is optional, only for script 11:
    deviceId = ""
    ```

## Usage

In this repository, there are 14 Python scripts in total. Note: script 10 is subdivided into 3 subscripts. Below, we will provide a brief explanation of each script and we will show how to execute the script in the terminal:

* `0_auth.py`: This script returns the DNA Center authentication token that is needed throughout the session. You can run the script by executing the following command in the terminal:

        $ python 0_auth.py

* `1_get_user_enrichment_details.py`: This script returns information about the connected devices. Please note that you have to specify the `entity_type` and `entity_value` in the `env.py` file. In case of the `entity_type`: `mac_address` the `entity_value` can be looked up in the DNA Center client view. You can run the script by executing the following command in the terminal:

        $ python 1_get_user_enrichment_details.py

* `2_all_access_points.py`: This script returns a list of all access points including the location. The response will be a list of JSON objects. Within this JSON object, you will have keys such as `deviceId` that can be used in the scripts below. You can run the script by executing the following command in the terminal:

        $ python 2_all_access_points.py

* `3_all_locations_address_info.py`: This script returns a list of all locations including address information. Among the response will also be a key with the `siteId`, which can be used in some of the scripts below. You can run the script by executing the following command in the terminal:

        $ python 3_all_locations_address_info.py

* `4_all_access_points_one_location.py`: This script returns a list of all access points at one location. Please note that you have to add the `siteId` in the `env.py` file in order to specify the location. The `siteId` can be obtained from the response of a former script, e.g., script 3. You can run the script by executing the following command in the terminal:

        $ python 4_all_access_points_one_location.py

* `5_get_all_SSIDs.py`: This script returns a list of all SSIDs. You can run the script by executing the following command in the terminal:

        $ python 5_get_all_SSIDs.py

* `6_all_locations_WLAN.py`: This script returns a list of all locations with a certain WLAN. Please note that we assumed that the WLAN is represented by all the SSIDs at a certain site. You can run the script by executing the following command in the terminal:

        $ python 6_all_locations_WLAN.py

* `8_all_WLC_one_location.py`: This script returns a list of all WLAN controllers at a certain location. Please note that you have to specify the location denoted by `siteId` in the `env.py` file. The `siteId` can be obtained from the response of a former script, e.g., script 3. You can run the script by executing the following command in the terminal:

        $ python 8_all_WLC_one_location.py

* `9_all_access_points_connected_to_WLC.py`: This script returns a list of all access points associated with a WLAN controller. You can run the script by executing the following command in the terminal:

        $ python 9_all_access_points_connected_to_WLC.py

* `10X_call_config_of_access_point.py`: This script returns the running configuration of an access point. The script is subdivided into three parts. You have to run the scripts in the order `a`, `b` and `c`. Please note that you have to add the `deviceUuid` to the `env.py` file before running script `a`. After running script `a`, you will obtain the `taskId` which you will have to save in the `env.py` file. After running script `b`, you will obtain a `fileId`, which you will have to save in the `env.py` file. You can run the script by executing the following commands in the terminal:

        $ python 10a_call_config_of_access_point.py
        $ python 10b_call_config_of_access_point.py
        $ python 10c_call_config_of_access_point.py

* `11_device_info.py`: This script returns information about a specific device. Please note that you have to add `deviceId` to the `env.py` file. The `deviceId` can be obtained from the response of a former script, e.g., script 2. You can run the script by executing the following command in the terminal:

        $ python 11_device_info.py

* `12_location_info.py`: This script returns information about the locations. You can run the script by executing the following command in the terminal:

        $ python 12_location_info.py

* `13_interface_info.py`: This script returns information about the interfaces. You can run the script by executing the following command in the terminal:

        $ python 13_interface_info.py


## Further Resources

Official DNA Center getting started guides:

> https://developer.cisco.com/site/dnac-101/

> https://developer.cisco.com/docs/dna-center/#!getting-started

DNA Center REST API Documentation 2.2.2:

> https://developer.cisco.com/docs/dna-center/#!cisco-dna-2-2-2-api-overview

DNA Center Postman Collections:

> https://developer.cisco.com/docs/dna-center/#!postman-collections

DNA Center Python SDK:

> https://developer.cisco.com/docs/dna-center/#!python-sdk-getting-started

> https://dnacentersdk.readthedocs.io/en/latest/api/api.html

Cisco DNA Center Sandboxes:

> [Cisco DNA Center Always On 1.3.1.4](https://devnetsandbox.cisco.com/RM/Diagram/Index/471eb739-323e-4805-b2a6-d0ec813dc8fc?diagramType=Topology)

> [Cisco DNA Center Always On 2.1.2.5](https://devnetsandbox.cisco.com/RM/Diagram/Index/c3c949dc-30af-498b-9d77-4f1c07d835f9?diagramType=Topology)

> Further sandboxes under: https://developer.cisco.com/site/sandbox/

Cisco DevNet DNA Center Learning Labs:

> https://developer.cisco.com/learning/tracks/dnacenter-programmability


### LICENSE

Provided under Cisco Sample Code License, for details see [LICENSE](LICENSE.md)

### CODE_OF_CONDUCT

Our code of conduct is available [here](CODE_OF_CONDUCT.md)

### CONTRIBUTING

See our contributing guidelines [here](CONTRIBUTING.md)

#### DISCLAIMER:
<b>Please note:</b> This script is meant for demo purposes only. All tools/ scripts in this repo are released for use "AS IS" without any warranties of any kind, including, but not limited to their installation, use, or performance. Any use of these scripts and tools is at your own risk. There is no guarantee that they have been through thorough testing in a comparable environment and we are not responsible for any damage or data loss incurred with their use.
You are responsible for reviewing and testing any scripts you run thoroughly before use in any non-testing environment.