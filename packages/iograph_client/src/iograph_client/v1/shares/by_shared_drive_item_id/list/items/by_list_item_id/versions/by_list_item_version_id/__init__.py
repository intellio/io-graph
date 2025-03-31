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
	from .restore_version import RestoreVersionRequest
	from .fields import FieldsRequest
	from .........request_adapter import HttpxRequestAdapter
from iograph_models.v1.list_item_version import ListItemVersion
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError


class ByListItemVersionIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/shares/{sharedDriveItem%2Did}/list/items/{listItem%2Did}/versions/{listItemVersion%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> ListItemVersion:
		"""
		Get versions from shares
		The list of previous versions of the list item.
		"""
		tags = ['shares.list']

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
		Update the navigation property versions in shares
		
		"""
		tags = ['shares.list']

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
		Delete navigation property versions for shares
		
		"""
		tags = ['shares.list']
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

	def fields(self,
		sharedDriveItem_id: str,
		listItem_id: str,
		listItemVersion_id: str,
	) -> FieldsRequest:
		if sharedDriveItem_id is None:
			raise TypeError("sharedDriveItem_id cannot be null.")
		if listItem_id is None:
			raise TypeError("listItem_id cannot be null.")
		if listItemVersion_id is None:
			raise TypeError("listItemVersion_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["sharedDriveItem%2Did"] =  sharedDriveItem_id
		path_parameters["listItem%2Did"] =  listItem_id
		path_parameters["listItemVersion%2Did"] =  listItemVersion_id

		from .fields import FieldsRequest
		return FieldsRequest(self.request_adapter, path_parameters)

	def restore_version(self,
		sharedDriveItem_id: str,
		listItem_id: str,
		listItemVersion_id: str,
	) -> RestoreVersionRequest:
		if sharedDriveItem_id is None:
			raise TypeError("sharedDriveItem_id cannot be null.")
		if listItem_id is None:
			raise TypeError("listItem_id cannot be null.")
		if listItemVersion_id is None:
			raise TypeError("listItemVersion_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["sharedDriveItem%2Did"] =  sharedDriveItem_id
		path_parameters["listItem%2Did"] =  listItem_id
		path_parameters["listItemVersion%2Did"] =  listItemVersion_id

		from .restore_version import RestoreVersionRequest
		return RestoreVersionRequest(self.request_adapter, path_parameters)

