# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .count import CountRequest
	from .by_column_definition_id import ByColumnDefinitionIdRequest
	from ........request_adapter import HttpxRequestAdapter
from iograph_models.beta.column_definition import ColumnDefinition
from iograph_models.beta.column_definition_collection_response import ColumnDefinitionCollectionResponse
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ColumnsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/drives/{drive%2Did}/list/contentTypes/{contentType%2Did}/columns", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> ColumnDefinitionCollectionResponse:
		"""
		Get columns from drives
		The collection of column definitions for this content type.
		"""
		tags = ['drives.list']

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
		Create new navigation property to columns for drives
		
		"""
		tags = ['drives.list']

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
		drive_id: str,
		contentType_id: str,
		columnDefinition_id: str,
	) -> ByColumnDefinitionIdRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if contentType_id is None:
			raise TypeError("contentType_id cannot be null.")
		if columnDefinition_id is None:
			raise TypeError("columnDefinition_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["contentType%2Did"] =  contentType_id
		path_parameters["columnDefinition%2Did"] =  columnDefinition_id

		from .by_column_definition_id import ByColumnDefinitionIdRequest
		return ByColumnDefinitionIdRequest(self.request_adapter, path_parameters)

	def count(self,
		drive_id: str,
		contentType_id: str,
	) -> CountRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if contentType_id is None:
			raise TypeError("contentType_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["contentType%2Did"] =  contentType_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

