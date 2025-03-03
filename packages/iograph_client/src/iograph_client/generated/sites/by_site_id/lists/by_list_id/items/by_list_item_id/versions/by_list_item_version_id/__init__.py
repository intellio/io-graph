# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ..........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .restore_version import RestoreVersionRequest
	from .fields import FieldsRequest
	from ..........request_adapter import HttpxRequestAdapter
from iograph_models.models.list_item_version import ListItemVersion
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class ByListItemVersionIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/sites/{site%2Did}/lists/{list%2Did}/items/{listItem%2Did}/versions/{listItemVersion%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> ListItemVersion:
		"""
		Get a ListItemVersion resource
		Retrieve the metadata for a specific version of a ListItem.
		Find more info here: https://learn.microsoft.com/graph/api/listitemversion-get?view=graph-rest-1.0
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
		return await self.request_adapter.send_async(request_info, ListItemVersion, error_mapping)

	async def patch(
		self,
		body: ListItemVersion,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> ListItemVersion:
		"""
		Update the navigation property versions in sites
		
		"""
		tags = ['sites.list']

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
		return await self.request_adapter.send_async(request_info, ListItemVersion, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property versions for sites
		
		"""
		tags = ['sites.list']
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



	def with_url(self, raw_url: str) -> ByListItemVersionIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByListItemVersionIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByListItemVersionIdRequest(self.request_adapter, self.path_parameters)

	@property
	def fields(self,
	) -> FieldsRequest:
		from .fields import FieldsRequest
		return FieldsRequest(self.request_adapter, self.path_parameters)

	@property
	def restore_version(self,
	) -> RestoreVersionRequest:
		from .restore_version import RestoreVersionRequest
		return RestoreVersionRequest(self.request_adapter, self.path_parameters)

