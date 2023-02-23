from googleapiclient import errors
from googleapiclient.discovery import build

# Create the compute service client
service = build('compute', 'v1')

# Project ID and zone
project_id = 'your_project_id'
zone = 'us-central1-a'

# VM details
instance_name = 'my-new-vm'
machine_type = 'zones/{}/machineTypes/n1-standard-1'.format(zone)
image_project = 'ubuntu-os-cloud'
image_family = 'ubuntu-1804-lts'

# Create the VM
request = service.instances().insert(project=project_id, zone=zone, body={
    'name': instance_name,
    'machineType': machine_type,
    'disks': [{
        'boot': True,
        'autoDelete': True,
        'initializeParams': {
            'sourceImage': 'projects/{}/global/images/{}'.format(image_project, image_family)
        }
    }],
    'networkInterfaces': [{
        'network': 'global/networks/default'
    }]
})

try:
    response = request.execute()
    print(response)
except HttpError as error:
    print(f'An error occurred: {error}')



This script will create a new n1-standard-1 instance, running Ubuntu 18.04 LTS, in the us-central1-a zone.
You will need to replace 'your_project_id' with your Google Cloud project ID
