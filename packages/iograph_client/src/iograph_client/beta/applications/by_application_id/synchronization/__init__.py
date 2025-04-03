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
	from .ping import PingRequest
	from .acquire_access_token import AcquireAccessTokenRequest
	from .jobs import JobsRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.synchronization import Synchronization


class SynchronizationRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/applications/{application%2Did}/synchronization", path_parameters)

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
		application_id: str,
	) -> JobsRequest:
		if application_id is None:
			raise TypeError("application_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["application%2Did"] =  application_id

		from .jobs import JobsRequest
		return JobsRequest(self.request_adapter, path_parameters)

	def acquire_access_token(self,
		application_id: str,
	) -> AcquireAccessTokenRequest:
		if application_id is None:
			raise TypeError("application_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["application%2Did"] =  application_id

		from .acquire_access_token import AcquireAccessTokenRequest
		return AcquireAccessTokenRequest(self.request_adapter, path_parameters)

	def ping(self,
		application_id: str,
	) -> PingRequest:
		if application_id is None:
			raise TypeError("application_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["application%2Did"] =  application_id

		from .ping import PingRequest
		return PingRequest(self.request_adapter, path_parameters)

	def secrets(self,
		application_id: str,
	) -> SecretsRequest:
		if application_id is None:
			raise TypeError("application_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["application%2Did"] =  application_id

		from .secrets import SecretsRequest
		return SecretsRequest(self.request_adapter, path_parameters)

	def templates(self,
		application_id: str,
	) -> TemplatesRequest:
		if application_id is None:
			raise TypeError("application_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["application%2Did"] =  application_id

		from .templates import TemplatesRequest
		return TemplatesRequest(self.request_adapter, path_parameters)

