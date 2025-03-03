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
	from .by_horizontal_section_column_id import ByHorizontalSectionColumnIdRequest
	from .............request_adapter import HttpxRequestAdapter
from iograph_models.models.horizontal_section_column_collection_response import HorizontalSectionColumnCollectionResponse
from iograph_models.models.horizontal_section_column import HorizontalSectionColumn
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class ColumnsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/groups/{group%2Did}/sites/{site%2Did}/pages/{baseSitePage%2Did}/graph.sitePage/canvasLayout/horizontalSections/{horizontalSection%2Did}/columns", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> HorizontalSectionColumnCollectionResponse:
		"""
		Get columns from groups
		The set of vertical columns in this section.
		"""
		tags = ['groups.site']

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
		return await self.request_adapter.send_async(request_info, HorizontalSectionColumnCollectionResponse, error_mapping)

	async def post(
		self,
		body: HorizontalSectionColumn,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> HorizontalSectionColumn:
		"""
		Create new navigation property to columns for groups
		
		"""
		tags = ['groups.site']

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
		return await self.request_adapter.send_async(request_info, HorizontalSectionColumn, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> ColumnsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ColumnsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ColumnsRequest(self.request_adapter, self.path_parameters)

	def by_horizontal_section_column_id(self,
		group_id: str,
		site_id: str,
		baseSitePage_id: str,
		horizontalSection_id: str,
		horizontalSectionColumn_id: str,
	) -> ByHorizontalSectionColumnIdRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")
		if site_id is None:
			raise TypeError("site_id cannot be null.")
		if baseSitePage_id is None:
			raise TypeError("baseSitePage_id cannot be null.")
		if horizontalSection_id is None:
			raise TypeError("horizontalSection_id cannot be null.")
		if horizontalSectionColumn_id is None:
			raise TypeError("horizontalSectionColumn_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id
		path_parameters["site%2Did"] =  site_id
		path_parameters["baseSitePage%2Did"] =  baseSitePage_id
		path_parameters["horizontalSection%2Did"] =  horizontalSection_id
		path_parameters["horizontalSectionColumn%2Did"] =  horizontalSectionColumn_id

		from .by_horizontal_section_column_id import ByHorizontalSectionColumnIdRequest
		return ByHorizontalSectionColumnIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

