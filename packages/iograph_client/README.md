# Microsoft Graph Python SDK
Microsoft Graph Python SDK. Heavily influenced ny the official released SDK client by Microsoft, but better!  


Quick Start:
```
import httpx
from azure.identity.aio import ClientSecretCredential
from kiota_authentication_azure.azure_identity_authentication_provider import AzureIdentityAuthenticationProvider
from msgraph_core import GraphClientFactory
from msgraph_core._enums import APIVersion, NationalClouds


def create_httpx_client():
    client = httpx.AsyncClient()
    return client

# credential is one of the credential classes from azure.identity
credential = ClientSecretCredential(
        tenant_id=TENANT_ID,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    )

# scopes is an array of permission scope strings
auth_provider = AzureIdentityAuthenticationProvider(credential, scopes=SCOPES)

http_client = GraphClientFactory.create_with_default_middleware(
    api_version = APIVersion.v1,
    client = create_httpx_client(),
    host = NationalClouds.Global,
    options = None
)

```
