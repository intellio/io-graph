# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ...request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .qnas import QnasRequest
	from .query import QueryRequest
	from .bookmarks import BookmarksRequest
	from .acronyms import AcronymsRequest
	from ...request_adapter import HttpxRequestAdapter
from iograph_models.beta.search_entity import SearchEntity
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class SearchRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/search", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> SearchEntity:
		"""
		Get search
		
		"""
		tags = ['search.searchEntity']

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
		return await self.request_adapter.send_async(request_info, SearchEntity, error_mapping)

	async def patch(
		self,
		body: SearchEntity,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> SearchEntity:
		"""
		Update search
		
		"""
		tags = ['search.searchEntity']

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
		return await self.request_adapter.send_async(request_info, SearchEntity, error_mapping)

	class GetQueryParams(BaseModel):
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> SearchRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: SearchRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return SearchRequest(self.request_adapter, self.path_parameters)

	@property
	def acronyms(self,
	) -> AcronymsRequest:
		from .acronyms import AcronymsRequest
		return AcronymsRequest(self.request_adapter, self.path_parameters)

	@property
	def bookmarks(self,
	) -> BookmarksRequest:
		from .bookmarks import BookmarksRequest
		return BookmarksRequest(self.request_adapter, self.path_parameters)

	@property
	def query(self,
	) -> QueryRequest:
		from .query import QueryRequest
		return QueryRequest(self.request_adapter, self.path_parameters)

	@property
	def qnas(self,
	) -> QnasRequest:
		from .qnas import QnasRequest
		return QnasRequest(self.request_adapter, self.path_parameters)

