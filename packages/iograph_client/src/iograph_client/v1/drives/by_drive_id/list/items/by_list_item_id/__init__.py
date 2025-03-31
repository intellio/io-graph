# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .versions import VersionsRequest
	from .get_activities_by_interval_with_startdatetime_enddatetime_interval import GetActivitiesByIntervalWithStartDateTimeEndDateTimeIntervalRequest
	from .get_activities_by_interval import GetActivitiesByIntervalRequest
	from .create_link import CreateLinkRequest
	from .last_modified_by_user import LastModifiedByUserRequest
	from .fields import FieldsRequest
	from .drive_item import DriveItemRequest
	from .document_set_versions import DocumentSetVersionsRequest
	from .created_by_user import CreatedByUserRequest
	from .analytics import AnalyticsRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.v1.list_item import ListItem
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError


class ByListItemIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/drives/{drive%2Did}/list/items/{listItem%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> ListItem:
		"""
		Get items from drives
		All items contained in the list.
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
		return await self.request_adapter.send_async(request_info, ListItem, error_mapping)

	async def patch(
		self,
		body: ListItem,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> ListItem:
		"""
		Update the navigation property items in drives
		
		"""
		tags = ['drives.list']

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
		Delete navigation property items for drives
		
		"""
		tags = ['drives.list']
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



	def with_url(self, raw_url: str) -> ByListItemIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByListItemIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByListItemIdRequest(self.request_adapter, self.path_parameters)

	def analytics(self,
		drive_id: str,
		listItem_id: str,
	) -> AnalyticsRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if listItem_id is None:
			raise TypeError("listItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["listItem%2Did"] =  listItem_id

		from .analytics import AnalyticsRequest
		return AnalyticsRequest(self.request_adapter, path_parameters)

	def created_by_user(self,
		drive_id: str,
		listItem_id: str,
	) -> CreatedByUserRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if listItem_id is None:
			raise TypeError("listItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["listItem%2Did"] =  listItem_id

		from .created_by_user import CreatedByUserRequest
		return CreatedByUserRequest(self.request_adapter, path_parameters)

	def document_set_versions(self,
		drive_id: str,
		listItem_id: str,
	) -> DocumentSetVersionsRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if listItem_id is None:
			raise TypeError("listItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["listItem%2Did"] =  listItem_id

		from .document_set_versions import DocumentSetVersionsRequest
		return DocumentSetVersionsRequest(self.request_adapter, path_parameters)

	def drive_item(self,
		drive_id: str,
		listItem_id: str,
	) -> DriveItemRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if listItem_id is None:
			raise TypeError("listItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["listItem%2Did"] =  listItem_id

		from .drive_item import DriveItemRequest
		return DriveItemRequest(self.request_adapter, path_parameters)

	def fields(self,
		drive_id: str,
		listItem_id: str,
	) -> FieldsRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if listItem_id is None:
			raise TypeError("listItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["listItem%2Did"] =  listItem_id

		from .fields import FieldsRequest
		return FieldsRequest(self.request_adapter, path_parameters)

	def last_modified_by_user(self,
		drive_id: str,
		listItem_id: str,
	) -> LastModifiedByUserRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if listItem_id is None:
			raise TypeError("listItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["listItem%2Did"] =  listItem_id

		from .last_modified_by_user import LastModifiedByUserRequest
		return LastModifiedByUserRequest(self.request_adapter, path_parameters)

	def create_link(self,
		drive_id: str,
		listItem_id: str,
	) -> CreateLinkRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if listItem_id is None:
			raise TypeError("listItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["listItem%2Did"] =  listItem_id

		from .create_link import CreateLinkRequest
		return CreateLinkRequest(self.request_adapter, path_parameters)

	def get_activities_by_interval(self,
		drive_id: str,
		listItem_id: str,
	) -> GetActivitiesByIntervalRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if listItem_id is None:
			raise TypeError("listItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["listItem%2Did"] =  listItem_id

		from .get_activities_by_interval import GetActivitiesByIntervalRequest
		return GetActivitiesByIntervalRequest(self.request_adapter, path_parameters)

	def get_activities_by_interval_with_startdatetime_enddatetime_interval(self,
		drive_id: str,
		listItem_id: str,
		startDateTime: str,
		endDateTime: str,
		interval: str,
	) -> GetActivitiesByIntervalWithStartDateTimeEndDateTimeIntervalRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if listItem_id is None:
			raise TypeError("listItem_id cannot be null.")
		if startDateTime is None:
			raise TypeError("startDateTime cannot be null.")
		if endDateTime is None:
			raise TypeError("endDateTime cannot be null.")
		if interval is None:
			raise TypeError("interval cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["listItem%2Did"] =  listItem_id
		path_parameters["startDateTime"] =  startDateTime
		path_parameters["endDateTime"] =  endDateTime
		path_parameters["interval"] =  interval

		from .get_activities_by_interval_with_startdatetime_enddatetime_interval import GetActivitiesByIntervalWithStartDateTimeEndDateTimeIntervalRequest
		return GetActivitiesByIntervalWithStartDateTimeEndDateTimeIntervalRequest(self.request_adapter, path_parameters)

	def versions(self,
		drive_id: str,
		listItem_id: str,
	) -> VersionsRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if listItem_id is None:
			raise TypeError("listItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["listItem%2Did"] =  listItem_id

		from .versions import VersionsRequest
		return VersionsRequest(self.request_adapter, path_parameters)

