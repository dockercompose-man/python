import boto3

# Create the EC2 client
client = boto3.client('ec2')

# VM details
image_id = 'ami-0c3b95d5a95376f4f'
instance_type = 't2.micro'
key_name = 'my_key_pair'
security_group_ids = ['sg-01234567890abcdef0']
subnet_id = 'subnet-01234567890abcdef0'

# Create the VM
response = client.run_instances(
    ImageId=image_id,
    InstanceType=instance_type,
    KeyName=key_name,
    SecurityGroupIds=security_group_ids,
    SubnetId=subnet_id
)

# Print the response
print(response)


This script will create a new t2.micro instance, using the specified Amazon Machine Image (AMI), in the specified subnet and security group.
You will need to replace 'ami-0c3b95d5a95376f4f' with the correct AMI ID for your desired OS, replace the security group id and the subnet id

Azure:

Copy code
from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.compute import ComputeManagementClient

# Credentials
credentials = ServicePrincipalCredentials(
    client_id='your_client_id',
    secret='your



Regenerate response
