# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .upload_client_certificate import UploadClientCertificateRequest
	from .ref import RefRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.identity_api_connector import IdentityApiConnector


class PostAttributeCollectionRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/identity/b2xUserFlows/{b2xIdentityUserFlow%2Did}/apiConnectorConfiguration/postAttributeCollection", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> IdentityApiConnector:
		"""
		Get postAttributeCollection from identity
		
		"""
		tags = ['identity.b2xIdentityUserFlow']

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
		return await self.request_adapter.send_async(request_info, IdentityApiConnector, error_mapping)

	async def patch(
		self,
		body: IdentityApiConnector,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> IdentityApiConnector:
		"""
		Update the navigation property postAttributeCollection in identity
		
		"""
		tags = ['identity.b2xIdentityUserFlow']

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
		return await self.request_adapter.send_async(request_info, IdentityApiConnector, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property postAttributeCollection for identity
		
		"""
		tags = ['identity.b2xIdentityUserFlow']
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



	def with_url(self, raw_url: str) -> PostAttributeCollectionRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: PostAttributeCollectionRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return PostAttributeCollectionRequest(self.request_adapter, self.path_parameters)

	def ref(self,
		b2xIdentityUserFlow_id: str,
	) -> RefRequest:
		if b2xIdentityUserFlow_id is None:
			raise TypeError("b2xIdentityUserFlow_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["b2xIdentityUserFlow%2Did"] =  b2xIdentityUserFlow_id

		from .ref import RefRequest
		return RefRequest(self.request_adapter, path_parameters)

	def upload_client_certificate(self,
		b2xIdentityUserFlow_id: str,
	) -> UploadClientCertificateRequest:
		if b2xIdentityUserFlow_id is None:
			raise TypeError("b2xIdentityUserFlow_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["b2xIdentityUserFlow%2Did"] =  b2xIdentityUserFlow_id

		from .upload_client_certificate import UploadClientCertificateRequest
		return UploadClientCertificateRequest(self.request_adapter, path_parameters)

