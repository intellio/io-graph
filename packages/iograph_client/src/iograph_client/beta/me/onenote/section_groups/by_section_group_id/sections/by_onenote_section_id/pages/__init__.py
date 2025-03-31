# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .count import CountRequest
	from .by_onenote_page_id import ByOnenotePageIdRequest
	from .........request_adapter import HttpxRequestAdapter
from iograph_models.beta.onenote_page import OnenotePage
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.onenote_page_collection_response import OnenotePageCollectionResponse


class PagesRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/me/onenote/sectionGroups/{sectionGroup%2Did}/sections/{onenoteSection%2Did}/pages", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> OnenotePageCollectionResponse:
		"""
		Get pages from me
		The collection of pages in the section.  Read-only. Nullable.
		"""
		tags = ['me.onenote']

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
		return await self.request_adapter.send_async(request_info, OnenotePageCollectionResponse, error_mapping)

	async def post(
		self,
		body: OnenotePage,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> OnenotePage:
		"""
		Create new navigation property to pages for me
		
		"""
		tags = ['me.onenote']

		error_mapping: dict[str, type[BaseModel]] = {
			"XXX": ODataErrorsODataError,
		}

		request_info: RequestInformation = RequestInformation(
			method = Method.POST,
			url_template = self.url_template,
			path_parameters = self.path_parameters,
		)
		request_info.configure(request_configuration)
		request_info.headers.try_add("Accept", "application/json")
		request_info.set_content(body, "application/json")
		return await self.request_adapter.send_async(request_info, OnenotePage, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> PagesRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: PagesRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return PagesRequest(self.request_adapter, self.path_parameters)

	def by_onenote_page_id(self,
		sectionGroup_id: str,
		onenoteSection_id: str,
		onenotePage_id: str,
	) -> ByOnenotePageIdRequest:
		if sectionGroup_id is None:
			raise TypeError("sectionGroup_id cannot be null.")
		if onenoteSection_id is None:
			raise TypeError("onenoteSection_id cannot be null.")
		if onenotePage_id is None:
			raise TypeError("onenotePage_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["sectionGroup%2Did"] =  sectionGroup_id
		path_parameters["onenoteSection%2Did"] =  onenoteSection_id
		path_parameters["onenotePage%2Did"] =  onenotePage_id

		from .by_onenote_page_id import ByOnenotePageIdRequest
		return ByOnenotePageIdRequest(self.request_adapter, path_parameters)

	def count(self,
		sectionGroup_id: str,
		onenoteSection_id: str,
	) -> CountRequest:
		if sectionGroup_id is None:
			raise TypeError("sectionGroup_id cannot be null.")
		if onenoteSection_id is None:
			raise TypeError("onenoteSection_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["sectionGroup%2Did"] =  sectionGroup_id
		path_parameters["onenoteSection%2Did"] =  onenoteSection_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

