from abc import abstractmethod
from typing import List, Optional, Union
from contextlib import asynccontextmanager, contextmanager
from collections.abc import AsyncGenerator
import httpx
from httpx import AsyncClient
import datetime
import time
from azure.core.credentials import TokenCredential
from azure.core.credentials_async import AsyncTokenCredential
from azure.identity.aio import ClientSecretCredential as aioClientSecretCredential
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from .generated._generated_base_service_client import GraphServiceClientBase
from .request_adapter import HttpxRequestAdapter

from kiota_authentication_azure.azure_identity_authentication_provider import (
    AzureIdentityAuthenticationProvider,
)


class GraphServiceClient(BaseRequestBuilder, GraphServiceClientBase):

    def __init__(self, request_adapter: HttpxRequestAdapter) -> None:
        super().__init__(request_adapter, "{+baseurl}", None)
        if not self.request_adapter.base_url:
            raise ValueError("base_url is required in request_adapter")
        self.path_parameters["base_url"] = self.request_adapter.base_url

    @abstractmethod
    def batch(self):
        """
        Returns a BatchRequestBuilder to enable batch requests.
        to be implemented based on original https://github.com/microsoftgraph/msgraph-sdk-python/blob/main/msgraph/graph_service_client.py
        """
        ...
