from abc import abstractmethod
from typing import TypeVar, Callable


from kiota_abstractions.base_request_builder import BaseRequestBuilder
from .v1._generated_base_service_client import GraphServiceClientBase as V1GraphServiceClientBase
from .beta._generated_base_service_client import GraphServiceClientBase as BetaGraphServiceClientBase
from .request_adapter import HttpxRequestAdapter


T = TypeVar("T")

class GraphServiceClientMixins:
    @staticmethod
    async def get_all(endpoint: Callable[[],T], request_configuration=None) -> T:
        """
        This function is used to get all the values from the endpoint.
        Its a recursive function that will keep calling the endpoint until all the values are fetched.
        The way it finds that there are more values to fetch is by checking the odata_next_link in the response.
        Args:
            endpoints (str): The endpoint to call. This is a string that is split by '.' to get the final endpoint.
            request_configuration (RequestConfiguration): The request configuration to be used for the request. Defaults to None.
        """
        # if isinstance(endpoint, str):
        #     calling_endpoint = reduce(getattr,endpoint.split('.'),self) 
        # else:
        #     calling_endpoint = endpoint
        calling_endpoint = endpoint
        
        response =  await calling_endpoint.get(request_configuration=request_configuration)
        if response:
            response_collection = []
            if hasattr(response,'value') and isinstance(response.value, list):
                response_collection = response
            else:
                return response

            while response is not None and response.odata_nextLink is not None:
                response = await calling_endpoint.with_url(response.odata_next_link).get()
                response_collection.value.extend(response.value)
            return response_collection
        else:
            raise ValueError('Value error')

    @abstractmethod
    def batch(self):
        """
        Returns a BatchRequestBuilder to enable batch requests.
        to be implemented based on original https://github.com/microsoftgraph/msgraph-sdk-python/blob/main/msgraph/graph_service_client.py
        """
        ...


class GraphServiceClient(BaseRequestBuilder, V1GraphServiceClientBase, GraphServiceClientMixins):

    def __init__(self, request_adapter: HttpxRequestAdapter) -> None:
        super().__init__(request_adapter, "{+baseurl}", None)

        if not self.request_adapter.base_url:
            raise ValueError("base_url is required in request_adapter")
        self.path_parameters["base_url"] = self.request_adapter.base_url
    
class GraphBetaServiceClient(BaseRequestBuilder, BetaGraphServiceClientBase, GraphServiceClientMixins):

    def __init__(self, request_adapter: HttpxRequestAdapter) -> None:
        super().__init__(request_adapter, "{+baseurl}", None)

        if not self.request_adapter.base_url:
            raise ValueError("base_url is required in request_adapter")
        self.path_parameters["base_url"] = self.request_adapter.base_url