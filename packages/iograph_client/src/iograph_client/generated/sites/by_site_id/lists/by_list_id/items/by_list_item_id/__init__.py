# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .versions import VersionsRequest
	from .create_link import CreateLinkRequest
	from .last_modified_by_user import LastModifiedByUserRequest
	from .fields import FieldsRequest
	from .drive_item import DriveItemRequest
	from .document_set_versions import DocumentSetVersionsRequest
	from .created_by_user import CreatedByUserRequest
	from .analytics import AnalyticsRequest
	from ........request_adapter import HttpxRequestAdapter
from iograph_models.models.list_item import ListItem
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class ByListItemIdRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/sites/{site%2Did}/lists/{list%2Did}/items/{listItem%2Did}"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> ListItem:
		"""
		Get listItem
		Returns the metadata for an item in a list.
		Find more info here: https://learn.microsoft.com/graph/api/listitem-get?view=graph-rest-1.0
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
		return await self.request_adapter.send_async(request_info, ListItem, error_mapping)

	async def patch(
		self,
		body: ListItem,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> ListItem:
		"""
		Update the navigation property items in sites
		
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
		return await self.request_adapter.send_async(request_info, ListItem, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete an item from a list
		Removes an item from a list.
		Find more info here: https://learn.microsoft.com/graph/api/listitem-delete?view=graph-rest-1.0
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



	@property
	def analytics(self,
	) -> AnalyticsRequest:
		from .analytics import AnalyticsRequest
		return AnalyticsRequest(self.request_adapter, self.path_parameters)

	@property
	def created_by_user(self,
	) -> CreatedByUserRequest:
		from .created_by_user import CreatedByUserRequest
		return CreatedByUserRequest(self.request_adapter, self.path_parameters)

	@property
	def document_set_versions(self,
	) -> DocumentSetVersionsRequest:
		from .document_set_versions import DocumentSetVersionsRequest
		return DocumentSetVersionsRequest(self.request_adapter, self.path_parameters)

	@property
	def drive_item(self,
	) -> DriveItemRequest:
		from .drive_item import DriveItemRequest
		return DriveItemRequest(self.request_adapter, self.path_parameters)

	@property
	def fields(self,
	) -> FieldsRequest:
		from .fields import FieldsRequest
		return FieldsRequest(self.request_adapter, self.path_parameters)

	@property
	def last_modified_by_user(self,
	) -> LastModifiedByUserRequest:
		from .last_modified_by_user import LastModifiedByUserRequest
		return LastModifiedByUserRequest(self.request_adapter, self.path_parameters)

	@property
	def create_link(self,
	) -> CreateLinkRequest:
		from .create_link import CreateLinkRequest
		return CreateLinkRequest(self.request_adapter, self.path_parameters)

	@property
	def versions(self,
	) -> VersionsRequest:
		from .versions import VersionsRequest
		return VersionsRequest(self.request_adapter, self.path_parameters)

