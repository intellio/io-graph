# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
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
from iograph_models.models.synchronization import Synchronization
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class SynchronizationRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/applications/{application%2Did}/synchronization"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> Synchronization:
		"""
		Get synchronization from applications
		Represents the capability for Microsoft Entra identity synchronization through the Microsoft Graph API.
		"""
		tags = ['applications.synchronization']

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
		Update the navigation property synchronization in applications
		
		"""
		tags = ['applications.synchronization']

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
		Delete navigation property synchronization for applications
		
		"""
		tags = ['applications.synchronization']
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



	@property
	def jobs(self,
	) -> JobsRequest:
		from .jobs import JobsRequest
		return JobsRequest(self.request_adapter, self.path_parameters)

	@property
	def acquire_access_token(self,
	) -> AcquireAccessTokenRequest:
		from .acquire_access_token import AcquireAccessTokenRequest
		return AcquireAccessTokenRequest(self.request_adapter, self.path_parameters)

	@property
	def secrets(self,
	) -> SecretsRequest:
		from .secrets import SecretsRequest
		return SecretsRequest(self.request_adapter, self.path_parameters)

	@property
	def templates(self,
	) -> TemplatesRequest:
		from .templates import TemplatesRequest
		return TemplatesRequest(self.request_adapter, self.path_parameters)

