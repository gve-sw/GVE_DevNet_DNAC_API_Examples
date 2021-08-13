'''
Copyright (c) 2021 Cisco and/or its affiliates.

This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at

               https://developer.cisco.com/docs/licenses

All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.
'''

import requests 
from env import dnac_host, token 
from pprint import pprint 
 
url = f"{dnac_host}/dna/intent/api/v1/wireless/profile" 
 
payload = None 
 
headers = { 
    "Content-Type": "application/json", 
    "Accept": "application/json", 
    "x-auth-token": f"{token}" 
} 
 
response = requests.request('GET', url, headers=headers, data = payload) 
 
response_data = response.json() 
 
pprint(response_data) 