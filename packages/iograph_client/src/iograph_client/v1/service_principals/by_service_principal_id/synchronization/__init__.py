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
	from .templates import TemplatesRequest
	from .secrets import SecretsRequest
	from .acquire_access_token import AcquireAccessTokenRequest
	from .jobs import JobsRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.v1.synchronization import Synchronization
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError


class SynchronizationRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/servicePrincipals/{servicePrincipal%2Did}/synchronization", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> Synchronization:
		"""
		Get synchronization from servicePrincipals
		Represents the capability for Microsoft Entra identity synchronization through the Microsoft Graph API.
		"""
		tags = ['servicePrincipals.synchronization']

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
		return await self.request_adapter.send_async(request_info, Synchronization, error_mapping)

	async def put(
		self,
		body: Synchronization,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> Synchronization:
		"""
		Update the navigation property synchronization in servicePrincipals
		
		"""
		tags = ['servicePrincipals.synchronization']

		error_mapping: dict[str, type[BaseModel]] = {
			"XXX": ODataErrorsODataError,
		}

		request_info: RequestInformation = RequestInformation(
			method = Method.PUT,
			url_template = self.url_template,
			path_parameters = self.path_parameters,
		)
		request_info.configure(request_configuration)
		request_info.headers.try_add("Accept", "application/json")
		request_info.set_content(body, "application/json")
		return await self.request_adapter.send_async(request_info, Synchronization, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property synchronization for servicePrincipals
		
		"""
		tags = ['servicePrincipals.synchronization']
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



	def with_url(self, raw_url: str) -> SynchronizationRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: SynchronizationRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return SynchronizationRequest(self.request_adapter, self.path_parameters)

	def jobs(self,
		servicePrincipal_id: str,
	) -> JobsRequest:
		if servicePrincipal_id is None:
			raise TypeError("servicePrincipal_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["servicePrincipal%2Did"] =  servicePrincipal_id

		from .jobs import JobsRequest
		return JobsRequest(self.request_adapter, path_parameters)

	def acquire_access_token(self,
		servicePrincipal_id: str,
	) -> AcquireAccessTokenRequest:
		if servicePrincipal_id is None:
			raise TypeError("servicePrincipal_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["servicePrincipal%2Did"] =  servicePrincipal_id

		from .acquire_access_token import AcquireAccessTokenRequest
		return AcquireAccessTokenRequest(self.request_adapter, path_parameters)

	def secrets(self,
		servicePrincipal_id: str,
	) -> SecretsRequest:
		if servicePrincipal_id is None:
			raise TypeError("servicePrincipal_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["servicePrincipal%2Did"] =  servicePrincipal_id

		from .secrets import SecretsRequest
		return SecretsRequest(self.request_adapter, path_parameters)

	def templates(self,
		servicePrincipal_id: str,
	) -> TemplatesRequest:
		if servicePrincipal_id is None:
			raise TypeError("servicePrincipal_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["servicePrincipal%2Did"] =  servicePrincipal_id

		from .templates import TemplatesRequest
		return TemplatesRequest(self.request_adapter, path_parameters)

