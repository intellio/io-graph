# Microsoft Graph Python SDK
Microsoft Graph Python SDK. Heavily influenced by the official released SDK client by Microsoft, but better!
Main difference with the official package is using Pydantic models instead of dataclasses and use its powerful features e.g validation, serialisation, discrimination ...


Quick Start:
```
import httpx
import asyncio
from azure.identity.aio import ClientSecretCredential
from kiota_authentication_azure.azure_identity_authentication_provider import AzureIdentityAuthenticationProvider
from msgraph_core import GraphClientFactory
from msgraph_core._enums import APIVersion, NationalClouds
from iograph_client.client import GraphServiceClient
from iograph_client.request_adapter import HttpxRequestAdapter


# a httpx client provider
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

# http client
http_client = GraphClientFactory.create_with_default_middleware(
    api_version=APIVersion.v1,
    client=create_httpx_client(),
    host=NationalClouds.Global,
    options=None
)

adapter = HttpxRequestAdapter(
    http_client=http_client,
    authentication_provider=auth_provider,
    base_url=NationalClouds.Global,
    api_version=APIVersion.v1
)

client = GraphServiceClient(adapter)


async def main():
    return await client.identity.conditional_access.named_locations.get()

result = asyncio.run(main())
```
All available Get Query Parameters acceptable by each enpoind is defined as a pydantic model insdie endpoint's request class

```
from kiota_abstractions.base_request_configuration import RequestConfiguration
from iograph_client.generated.identity.conditional_access.policies import PoliciesRequest

async def main():
    query_parameters = PoliciesRequest.GetQueryParams(top=1)
    request_config = RequestConfiguration(
        query_parameters=query_parameters
    )
    return await client.identity.conditional_access.policies.get(request_config)

result = asyncio.run(main())
```
