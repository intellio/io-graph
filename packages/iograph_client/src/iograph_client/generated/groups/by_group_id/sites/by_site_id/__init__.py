# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .term_stores import TermStoresRequest
	from .term_store import TermStoreRequest
	from .sites import SitesRequest
	from .permissions import PermissionsRequest
	from .pages import PagesRequest
	from .operations import OperationsRequest
	from .onenote import OnenoteRequest
	from .get_by_path_with_path import GetByPathWithPathRequest
	from .get_applicable_content_types_for_list_with_listid import GetApplicableContentTypesForListWithListIdRequest
	from .get_activities_by_interval_with_startdatetime_enddatetime_interval import GetActivitiesByIntervalWithStartDateTimeEndDateTimeIntervalRequest
	from .get_activities_by_interval import GetActivitiesByIntervalRequest
	from .lists import ListsRequest
	from .last_modified_by_user import LastModifiedByUserRequest
	from .items import ItemsRequest
	from .external_columns import ExternalColumnsRequest
	from .drives import DrivesRequest
	from .drive import DriveRequest
	from .created_by_user import CreatedByUserRequest
	from .content_types import ContentTypesRequest
	from .columns import ColumnsRequest
	from .analytics import AnalyticsRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.models.site import Site
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class BySiteIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/groups/{group%2Did}/sites/{site%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> Site:
		"""
		Get sites from groups
		The list of SharePoint sites in this group. Access the default site with /sites/root.
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
		return await self.request_adapter.send_async(request_info, Site, error_mapping)

	async def patch(
		self,
		body: Site,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> Site:
		"""
		Update the navigation property sites in groups
		
		"""
		tags = ['groups.site']

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
		return await self.request_adapter.send_async(request_info, Site, error_mapping)

	class GetQueryParams(BaseModel):
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> BySiteIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: BySiteIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return BySiteIdRequest(self.request_adapter, self.path_parameters)

	def analytics(self,
		group_id: str,
		site_id: str,
	) -> AnalyticsRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")
		if site_id is None:
			raise TypeError("site_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id
		path_parameters["site%2Did"] =  site_id

		from .analytics import AnalyticsRequest
		return AnalyticsRequest(self.request_adapter, path_parameters)

	def columns(self,
		group_id: str,
		site_id: str,
	) -> ColumnsRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")
		if site_id is None:
			raise TypeError("site_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id
		path_parameters["site%2Did"] =  site_id

		from .columns import ColumnsRequest
		return ColumnsRequest(self.request_adapter, path_parameters)

	def content_types(self,
		group_id: str,
		site_id: str,
	) -> ContentTypesRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")
		if site_id is None:
			raise TypeError("site_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id
		path_parameters["site%2Did"] =  site_id

		from .content_types import ContentTypesRequest
		return ContentTypesRequest(self.request_adapter, path_parameters)

	def created_by_user(self,
		group_id: str,
		site_id: str,
	) -> CreatedByUserRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")
		if site_id is None:
			raise TypeError("site_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id
		path_parameters["site%2Did"] =  site_id

		from .created_by_user import CreatedByUserRequest
		return CreatedByUserRequest(self.request_adapter, path_parameters)

	def drive(self,
		group_id: str,
		site_id: str,
	) -> DriveRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")
		if site_id is None:
			raise TypeError("site_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id
		path_parameters["site%2Did"] =  site_id

		from .drive import DriveRequest
		return DriveRequest(self.request_adapter, path_parameters)

	def drives(self,
		group_id: str,
		site_id: str,
	) -> DrivesRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")
		if site_id is None:
			raise TypeError("site_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id
		path_parameters["site%2Did"] =  site_id

		from .drives import DrivesRequest
		return DrivesRequest(self.request_adapter, path_parameters)

	def external_columns(self,
		group_id: str,
		site_id: str,
	) -> ExternalColumnsRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")
		if site_id is None:
			raise TypeError("site_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id
		path_parameters["site%2Did"] =  site_id

		from .external_columns import ExternalColumnsRequest
		return ExternalColumnsRequest(self.request_adapter, path_parameters)

	def items(self,
		group_id: str,
		site_id: str,
	) -> ItemsRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")
		if site_id is None:
			raise TypeError("site_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id
		path_parameters["site%2Did"] =  site_id

		from .items import ItemsRequest
		return ItemsRequest(self.request_adapter, path_parameters)

	def last_modified_by_user(self,
		group_id: str,
		site_id: str,
	) -> LastModifiedByUserRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")
		if site_id is None:
			raise TypeError("site_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id
		path_parameters["site%2Did"] =  site_id

		from .last_modified_by_user import LastModifiedByUserRequest
		return LastModifiedByUserRequest(self.request_adapter, path_parameters)

	def lists(self,
		group_id: str,
		site_id: str,
	) -> ListsRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")
		if site_id is None:
			raise TypeError("site_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id
		path_parameters["site%2Did"] =  site_id

		from .lists import ListsRequest
		return ListsRequest(self.request_adapter, path_parameters)

	def get_activities_by_interval(self,
		group_id: str,
		site_id: str,
	) -> GetActivitiesByIntervalRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")
		if site_id is None:
			raise TypeError("site_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id
		path_parameters["site%2Did"] =  site_id

		from .get_activities_by_interval import GetActivitiesByIntervalRequest
		return GetActivitiesByIntervalRequest(self.request_adapter, path_parameters)

	def get_activities_by_interval_with_startdatetime_enddatetime_interval(self,
		group_id: str,
		site_id: str,
		startDateTime: str,
		endDateTime: str,
		interval: str,
	) -> GetActivitiesByIntervalWithStartDateTimeEndDateTimeIntervalRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")
		if site_id is None:
			raise TypeError("site_id cannot be null.")
		if startDateTime is None:
			raise TypeError("startDateTime cannot be null.")
		if endDateTime is None:
			raise TypeError("endDateTime cannot be null.")
		if interval is None:
			raise TypeError("interval cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id
		path_parameters["site%2Did"] =  site_id
		path_parameters["startDateTime"] =  startDateTime
		path_parameters["endDateTime"] =  endDateTime
		path_parameters["interval"] =  interval

		from .get_activities_by_interval_with_startdatetime_enddatetime_interval import GetActivitiesByIntervalWithStartDateTimeEndDateTimeIntervalRequest
		return GetActivitiesByIntervalWithStartDateTimeEndDateTimeIntervalRequest(self.request_adapter, path_parameters)

	def get_applicable_content_types_for_list_with_listid(self,
		group_id: str,
		site_id: str,
		listId: str,
	) -> GetApplicableContentTypesForListWithListIdRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")
		if site_id is None:
			raise TypeError("site_id cannot be null.")
		if listId is None:
			raise TypeError("listId cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id
		path_parameters["site%2Did"] =  site_id
		path_parameters["listId"] =  listId

		from .get_applicable_content_types_for_list_with_listid import GetApplicableContentTypesForListWithListIdRequest
		return GetApplicableContentTypesForListWithListIdRequest(self.request_adapter, path_parameters)

	def get_by_path_with_path(self,
		group_id: str,
		site_id: str,
		path: str,
	) -> GetByPathWithPathRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")
		if site_id is None:
			raise TypeError("site_id cannot be null.")
		if path is None:
			raise TypeError("path cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id
		path_parameters["site%2Did"] =  site_id
		path_parameters["path"] =  path

		from .get_by_path_with_path import GetByPathWithPathRequest
		return GetByPathWithPathRequest(self.request_adapter, path_parameters)

	def onenote(self,
		group_id: str,
		site_id: str,
	) -> OnenoteRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")
		if site_id is None:
			raise TypeError("site_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id
		path_parameters["site%2Did"] =  site_id

		from .onenote import OnenoteRequest
		return OnenoteRequest(self.request_adapter, path_parameters)

	def operations(self,
		group_id: str,
		site_id: str,
	) -> OperationsRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")
		if site_id is None:
			raise TypeError("site_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id
		path_parameters["site%2Did"] =  site_id

		from .operations import OperationsRequest
		return OperationsRequest(self.request_adapter, path_parameters)

	def pages(self,
		group_id: str,
		site_id: str,
	) -> PagesRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")
		if site_id is None:
			raise TypeError("site_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id
		path_parameters["site%2Did"] =  site_id

		from .pages import PagesRequest
		return PagesRequest(self.request_adapter, path_parameters)

	def permissions(self,
		group_id: str,
		site_id: str,
	) -> PermissionsRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")
		if site_id is None:
			raise TypeError("site_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id
		path_parameters["site%2Did"] =  site_id

		from .permissions import PermissionsRequest
		return PermissionsRequest(self.request_adapter, path_parameters)

	def sites(self,
		group_id: str,
		site_id: str,
	) -> SitesRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")
		if site_id is None:
			raise TypeError("site_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id
		path_parameters["site%2Did"] =  site_id

		from .sites import SitesRequest
		return SitesRequest(self.request_adapter, path_parameters)

	def term_store(self,
		group_id: str,
		site_id: str,
	) -> TermStoreRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")
		if site_id is None:
			raise TypeError("site_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id
		path_parameters["site%2Did"] =  site_id

		from .term_store import TermStoreRequest
		return TermStoreRequest(self.request_adapter, path_parameters)

	def term_stores(self,
		group_id: str,
		site_id: str,
	) -> TermStoresRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")
		if site_id is None:
			raise TypeError("site_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id
		path_parameters["site%2Did"] =  site_id

		from .term_stores import TermStoresRequest
		return TermStoresRequest(self.request_adapter, path_parameters)

