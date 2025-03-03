# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .............request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .count import CountRequest
	from .by_term_id1 import ByTermId1Request
	from .............request_adapter import HttpxRequestAdapter
from iograph_models.models.term_store_term_collection_response import TermStoreTermCollectionResponse
from iograph_models.models.term_store_term import TermStoreTerm
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class ChildrenRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/sites/{site%2Did}/termStores/{store%2Did}/groups/{group%2Did}/sets/{set%2Did}/children/{term%2Did}/children", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> TermStoreTermCollectionResponse:
		"""
		Get children from sites
		Children of current term.
		"""
		tags = ['sites.store']

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
		return await self.request_adapter.send_async(request_info, TermStoreTermCollectionResponse, error_mapping)

	async def post(
		self,
		body: TermStoreTerm,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> TermStoreTerm:
		"""
		Create new navigation property to children for sites
		
		"""
		tags = ['sites.store']

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
		return await self.request_adapter.send_async(request_info, TermStoreTerm, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> ChildrenRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ChildrenRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ChildrenRequest(self.request_adapter, self.path_parameters)

	def by_term_id1(self,
		site_id: str,
		store_id: str,
		group_id: str,
		set_id: str,
		term_id: str,
		term_id1: str,
	) -> ByTermId1Request:
		if site_id is None:
			raise TypeError("site_id cannot be null.")
		if store_id is None:
			raise TypeError("store_id cannot be null.")
		if group_id is None:
			raise TypeError("group_id cannot be null.")
		if set_id is None:
			raise TypeError("set_id cannot be null.")
		if term_id is None:
			raise TypeError("term_id cannot be null.")
		if term_id1 is None:
			raise TypeError("term_id1 cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["site%2Did"] =  site_id
		path_parameters["store%2Did"] =  store_id
		path_parameters["group%2Did"] =  group_id
		path_parameters["set%2Did"] =  set_id
		path_parameters["term%2Did"] =  term_id
		path_parameters["term%2Did1"] =  term_id1

		from .by_term_id1 import ByTermId1Request
		return ByTermId1Request(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

