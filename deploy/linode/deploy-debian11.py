import requests
import json

# API credentials
api_key = 'your_api_key'

# Headers
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + api_key
}

# API endpoint
url = 'https://api.linode.com/v4/linode/instances'

# Data to send in the request
data = {
    'type': 'g6-standard-1',
    'region': 'ca-central',
    'image': 'linode/ubuntu20.04',
    'root_pass': 'your_root_password',
    'label': 'my_new_vm',
    'private_ip': True
}

# Send the request
response = requests.post(url, headers=headers, data=json.dumps(data))

# Print the response
print(response.text)
