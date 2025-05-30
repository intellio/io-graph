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
	from .count import CountRequest
	from .by_list_id import ByListIdRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.v1.list import List
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.v1.list_collection_response import ListCollectionResponse


class ListsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/sites/{site%2Did}/lists", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> ListCollectionResponse:
		"""
		Get lists in a site
		Get the collection of lists for a site. Lists with the system facet are hidden by default.
To list them, include system in your $select statement.
		Find more info here: https://learn.microsoft.com/graph/api/list-list?view=graph-rest-1.0
		"""
		tags = ['sites.list']

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
		return await self.request_adapter.send_async(request_info, ListCollectionResponse, error_mapping)

	async def post(
		self,
		body: List,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> List:
		"""
		Create a new list
		Create a new list in a site.
		Find more info here: https://learn.microsoft.com/graph/api/list-create?view=graph-rest-1.0
		"""
		tags = ['sites.list']

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
		return await self.request_adapter.send_async(request_info, List, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> ListsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ListsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ListsRequest(self.request_adapter, self.path_parameters)

	def by_list_id(self,
		site_id: str,
		list_id: str,
	) -> ByListIdRequest:
		if site_id is None:
			raise TypeError("site_id cannot be null.")
		if list_id is None:
			raise TypeError("list_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["site%2Did"] =  site_id
		path_parameters["list%2Did"] =  list_id

		from .by_list_id import ByListIdRequest
		return ByListIdRequest(self.request_adapter, path_parameters)

	def count(self,
		site_id: str,
	) -> CountRequest:
		if site_id is None:
			raise TypeError("site_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["site%2Did"] =  site_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

