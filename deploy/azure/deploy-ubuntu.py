from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.compute import ComputeManagementClient

# Credentials
credentials = ServicePrincipalCredentials(
    client_id='your_client_id',
    secret='your
