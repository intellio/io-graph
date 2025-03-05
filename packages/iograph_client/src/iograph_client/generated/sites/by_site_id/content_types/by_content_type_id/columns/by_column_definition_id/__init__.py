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
	from .source_column import SourceColumnRequest
	from ........request_adapter import HttpxRequestAdapter
from iograph_models.models.column_definition import ColumnDefinition
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class ByColumnDefinitionIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/sites/{site%2Did}/contentTypes/{contentType%2Did}/columns/{columnDefinition%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> ColumnDefinition:
		"""
		Get columnDefinition
		Retrieve the metadata for a site, a list, or a contentType column.
		Find more info here: https://learn.microsoft.com/graph/api/columndefinition-get?view=graph-rest-1.0
		"""
		tags = ['sites.contentType']

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
		return await self.request_adapter.send_async(request_info, ColumnDefinition, error_mapping)

	async def patch(
		self,
		body: ColumnDefinition,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> ColumnDefinition:
		"""
		Update columnDefinition
		Update a site, a list, or a content type column.
		Find more info here: https://learn.microsoft.com/graph/api/columndefinition-update?view=graph-rest-1.0
		"""
		tags = ['sites.contentType']

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
		return await self.request_adapter.send_async(request_info, ColumnDefinition, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete columnDefinition
		Remove a column from a site, a list, or a content type.
		Find more info here: https://learn.microsoft.com/graph/api/columndefinition-delete?view=graph-rest-1.0
		"""
		tags = ['sites.contentType']
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



	def with_url(self, raw_url: str) -> ByColumnDefinitionIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByColumnDefinitionIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByColumnDefinitionIdRequest(self.request_adapter, self.path_parameters)

	def source_column(self,
		site_id: str,
		contentType_id: str,
		columnDefinition_id: str,
	) -> SourceColumnRequest:
		if site_id is None:
			raise TypeError("site_id cannot be null.")
		if contentType_id is None:
			raise TypeError("contentType_id cannot be null.")
		if columnDefinition_id is None:
			raise TypeError("columnDefinition_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["site%2Did"] =  site_id
		path_parameters["contentType%2Did"] =  contentType_id
		path_parameters["columnDefinition%2Did"] =  columnDefinition_id

		from .source_column import SourceColumnRequest
		return SourceColumnRequest(self.request_adapter, path_parameters)

