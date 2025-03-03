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
	from .by_column_definition_id import ByColumnDefinitionIdRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.models.column_definition import ColumnDefinition
from iograph_models.models.column_definition_collection_response import ColumnDefinitionCollectionResponse
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class ColumnsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/sites/{site%2Did}/columns", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> ColumnDefinitionCollectionResponse:
		"""
		List columns in a site
		Get the collection of columns represented as columnDefinition resources in a site.
		Find more info here: https://learn.microsoft.com/graph/api/site-list-columns?view=graph-rest-1.0
		"""
		tags = ['sites.columnDefinition']

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
		return await self.request_adapter.send_async(request_info, ColumnDefinitionCollectionResponse, error_mapping)

	async def post(
		self,
		body: ColumnDefinition,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> ColumnDefinition:
		"""
		Create a columnDefinition in a site
		Create a column for a site with a request that specifies a columnDefinition.
		Find more info here: https://learn.microsoft.com/graph/api/site-post-columns?view=graph-rest-1.0
		"""
		tags = ['sites.columnDefinition']

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
		return await self.request_adapter.send_async(request_info, ColumnDefinition, error_mapping)

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

	def by_column_definition_id(self,
		site_id: str,
		columnDefinition_id: str,
	) -> ByColumnDefinitionIdRequest:
		if site_id is None:
			raise TypeError("site_id cannot be null.")
		if columnDefinition_id is None:
			raise TypeError("columnDefinition_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["site%2Did"] =  site_id
		path_parameters["columnDefinition%2Did"] =  columnDefinition_id

		from .by_column_definition_id import ByColumnDefinitionIdRequest
		return ByColumnDefinitionIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

