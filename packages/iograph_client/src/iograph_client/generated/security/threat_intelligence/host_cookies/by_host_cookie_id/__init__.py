# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .host import HostRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.models.security_host_cookie import SecurityHostCookie
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class ByHostCookieIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/security/threatIntelligence/hostCookies/{hostCookie%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> SecurityHostCookie:
		"""
		Get hostCookie
		Read the properties and relationships of a hostCookie object.
		Find more info here: https://learn.microsoft.com/graph/api/security-hostcookie-get?view=graph-rest-1.0
		"""
		tags = ['security.threatIntelligence']

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
		return await self.request_adapter.send_async(request_info, SecurityHostCookie, error_mapping)

	async def patch(
		self,
		body: SecurityHostCookie,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> SecurityHostCookie:
		"""
		Update the navigation property hostCookies in security
		
		"""
		tags = ['security.threatIntelligence']

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
		return await self.request_adapter.send_async(request_info, SecurityHostCookie, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property hostCookies for security
		
		"""
		tags = ['security.threatIntelligence']
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



	def with_url(self, raw_url: str) -> ByHostCookieIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByHostCookieIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByHostCookieIdRequest(self.request_adapter, self.path_parameters)

	@property
	def host(self,
	) -> HostRequest:
		from .host import HostRequest
		return HostRequest(self.request_adapter, self.path_parameters)

