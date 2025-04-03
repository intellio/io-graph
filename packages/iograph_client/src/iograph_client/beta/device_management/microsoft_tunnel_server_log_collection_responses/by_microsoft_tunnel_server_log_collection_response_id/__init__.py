# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .generate_download_url import GenerateDownloadUrlRequest
	from .create_download_url import CreateDownloadUrlRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.microsoft_tunnel_server_log_collection_response import MicrosoftTunnelServerLogCollectionResponse


class ByMicrosoftTunnelServerLogCollectionResponseIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceManagement/microsoftTunnelServerLogCollectionResponses/{microsoftTunnelServerLogCollectionResponse%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> MicrosoftTunnelServerLogCollectionResponse:
		"""
		Get microsoftTunnelServerLogCollectionResponses from deviceManagement
		Collection of MicrosoftTunnelServerLogCollectionResponse settings associated with account.
		"""
		tags = ['deviceManagement.microsoftTunnelServerLogCollectionResponse']

		error_mapping: dict[str, type[BaseModel]] = {
			"XXX": ODataErrorsODataError,
		}

		request_info: RequestInformation = RequestInformation(
			method = Method.GET,
			url_template = self.url_template,
			path_parameters = self.path_parameters,
		)
		request_info.configure(request_configuration)
		request_info.headers.try_add("Accept", "application/json")
		return await self.request_adapter.send_async(request_info, MicrosoftTunnelServerLogCollectionResponse, error_mapping)

	async def patch(
		self,
		body: MicrosoftTunnelServerLogCollectionResponse,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> MicrosoftTunnelServerLogCollectionResponse:
		"""
		Update the navigation property microsoftTunnelServerLogCollectionResponses in deviceManagement
		
		"""
		tags = ['deviceManagement.microsoftTunnelServerLogCollectionResponse']

		error_mapping: dict[str, type[BaseModel]] = {
			"XXX": ODataErrorsODataError,
		}

		request_info: RequestInformation = RequestInformation(
			method = Method.PATCH,
			url_template = self.url_template,
			path_parameters = self.path_parameters,
		)
		request_info.configure(request_configuration)
		request_info.headers.try_add("Accept", "application/json")
		request_info.set_content(body, "application/json")
		return await self.request_adapter.send_async(request_info, MicrosoftTunnelServerLogCollectionResponse, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property microsoftTunnelServerLogCollectionResponses for deviceManagement
		
		"""
		tags = ['deviceManagement.microsoftTunnelServerLogCollectionResponse']
		header_parameters = [{'name': 'If-Match', 'in': 'header', 'description': 'ETag', 'schema': {'type': 'string'}}]

		error_mapping: dict[str, type[BaseModel]] = {
			"XXX": ODataErrorsODataError,
		}

		request_info: RequestInformation = RequestInformation(
			method = Method.DELETE,
			url_template = self.url_template,
			path_parameters = self.path_parameters,
		)
		request_info.configure(request_configuration)
		request_info.headers.try_add("Accept", "application/json")
		return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)

	class GetQueryParams(BaseModel):
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")



	def with_url(self, raw_url: str) -> ByMicrosoftTunnelServerLogCollectionResponseIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByMicrosoftTunnelServerLogCollectionResponseIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByMicrosoftTunnelServerLogCollectionResponseIdRequest(self.request_adapter, self.path_parameters)

	def create_download_url(self,
		microsoftTunnelServerLogCollectionResponse_id: str,
	) -> CreateDownloadUrlRequest:
		if microsoftTunnelServerLogCollectionResponse_id is None:
			raise TypeError("microsoftTunnelServerLogCollectionResponse_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["microsoftTunnelServerLogCollectionResponse%2Did"] =  microsoftTunnelServerLogCollectionResponse_id

		from .create_download_url import CreateDownloadUrlRequest
		return CreateDownloadUrlRequest(self.request_adapter, path_parameters)

	def generate_download_url(self,
		microsoftTunnelServerLogCollectionResponse_id: str,
	) -> GenerateDownloadUrlRequest:
		if microsoftTunnelServerLogCollectionResponse_id is None:
			raise TypeError("microsoftTunnelServerLogCollectionResponse_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["microsoftTunnelServerLogCollectionResponse%2Did"] =  microsoftTunnelServerLogCollectionResponse_id

		from .generate_download_url import GenerateDownloadUrlRequest
		return GenerateDownloadUrlRequest(self.request_adapter, path_parameters)

