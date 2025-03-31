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
	from .by_list_item_version_id import ByListItemVersionIdRequest
	from .........request_adapter import HttpxRequestAdapter
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.v1.list_item_version import ListItemVersion
from iograph_models.v1.list_item_version_collection_response import ListItemVersionCollectionResponse


class VersionsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/sites/{site%2Did}/lists/{list%2Did}/items/{listItem%2Did}/versions", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> ListItemVersionCollectionResponse:
		"""
		Listing versions of a ListItem
		SharePoint can be configured to retain the history for list items. Previous versions may be retained for a finite period of time depending on admin settings which may be unique per user or location.
		Find more info here: https://learn.microsoft.com/graph/api/listitem-list-versions?view=graph-rest-1.0
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
		return await self.request_adapter.send_async(request_info, ListItemVersionCollectionResponse, error_mapping)

	async def post(
		self,
		body: ListItemVersion,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> ListItemVersion:
		"""
		Create new navigation property to versions for sites
		
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
		return await self.request_adapter.send_async(request_info, ListItemVersion, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> VersionsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: VersionsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return VersionsRequest(self.request_adapter, self.path_parameters)

	def by_list_item_version_id(self,
		site_id: str,
		list_id: str,
		listItem_id: str,
		listItemVersion_id: str,
	) -> ByListItemVersionIdRequest:
		if site_id is None:
			raise TypeError("site_id cannot be null.")
		if list_id is None:
			raise TypeError("list_id cannot be null.")
		if listItem_id is None:
			raise TypeError("listItem_id cannot be null.")
		if listItemVersion_id is None:
			raise TypeError("listItemVersion_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["site%2Did"] =  site_id
		path_parameters["list%2Did"] =  list_id
		path_parameters["listItem%2Did"] =  listItem_id
		path_parameters["listItemVersion%2Did"] =  listItemVersion_id

		from .by_list_item_version_id import ByListItemVersionIdRequest
		return ByListItemVersionIdRequest(self.request_adapter, path_parameters)

	def count(self,
		site_id: str,
		list_id: str,
		listItem_id: str,
	) -> CountRequest:
		if site_id is None:
			raise TypeError("site_id cannot be null.")
		if list_id is None:
			raise TypeError("list_id cannot be null.")
		if listItem_id is None:
			raise TypeError("listItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["site%2Did"] =  site_id
		path_parameters["list%2Did"] =  list_id
		path_parameters["listItem%2Did"] =  listItem_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

