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
	from .count import CountRequest
	from .by_host_cookie_id import ByHostCookieIdRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.security_host_cookie_collection_response import SecurityHostCookieCollectionResponse


class CookiesRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/security/threatIntelligence/hosts/{host%2Did}/cookies", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> SecurityHostCookieCollectionResponse:
		"""
		List cookies
		Get a list of hostCookie resources.
		Find more info here: https://learn.microsoft.com/graph/api/security-host-list-cookies?view=graph-rest-beta
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
		return await self.request_adapter.send_async(request_info, SecurityHostCookieCollectionResponse, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")

	def with_url(self, raw_url: str) -> CookiesRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: CookiesRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return CookiesRequest(self.request_adapter, self.path_parameters)

	def by_host_cookie_id(self,
		host_id: str,
		hostCookie_id: str,
	) -> ByHostCookieIdRequest:
		if host_id is None:
			raise TypeError("host_id cannot be null.")
		if hostCookie_id is None:
			raise TypeError("hostCookie_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["host%2Did"] =  host_id
		path_parameters["hostCookie%2Did"] =  hostCookie_id

		from .by_host_cookie_id import ByHostCookieIdRequest
		return ByHostCookieIdRequest(self.request_adapter, path_parameters)

	def count(self,
		host_id: str,
	) -> CountRequest:
		if host_id is None:
			raise TypeError("host_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["host%2Did"] =  host_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

