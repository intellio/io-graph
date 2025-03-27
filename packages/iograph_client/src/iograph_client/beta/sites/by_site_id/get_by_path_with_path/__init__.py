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
	from .term_store import TermStoreRequest
	from .sites import SitesRequest
	from .recycle_bin import RecycleBinRequest
	from .permissions import PermissionsRequest
	from .page_templates import PageTemplatesRequest
	from .pages import PagesRequest
	from .operations import OperationsRequest
	from .onenote import OnenoteRequest
	from .unarchive import UnarchiveRequest
	from .get_applicable_content_types_for_list_with_listid import GetApplicableContentTypesForListWithListIdRequest
	from .get_activities_by_interval_with_startdatetime_enddatetime_interval import GetActivitiesByIntervalWithStartDateTimeEndDateTimeIntervalRequest
	from .archive import ArchiveRequest
	from .lists import ListsRequest
	from .last_modified_by_user import LastModifiedByUserRequest
	from .items import ItemsRequest
	from .information_protection import InformationProtectionRequest
	from .external_columns import ExternalColumnsRequest
	from .drives import DrivesRequest
	from .drive import DriveRequest
	from .document_processing_jobs import DocumentProcessingJobsRequest
	from .created_by_user import CreatedByUserRequest
	from .content_types import ContentTypesRequest
	from .content_models import ContentModelsRequest
	from .columns import ColumnsRequest
	from .analytics import AnalyticsRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.beta.site import Site
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class GetByPathWithPathRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/sites/{site%2Did}/getByPath(path='{path}')", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> Site:
		"""
		Invoke function getByPath
		
		"""
		tags = ['sites.site.Functions']

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


	def with_url(self, raw_url: str) -> GetByPathWithPathRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: GetByPathWithPathRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return GetByPathWithPathRequest(self.request_adapter, self.path_parameters)

	def analytics(self,
		site_id: str,
		path: str,
	) -> AnalyticsRequest:
		if site_id is None:
			raise TypeError("site_id cannot be null.")
		if path is None:
			raise TypeError("path cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["site%2Did"] =  site_id
		path_parameters["path"] =  path

		from .analytics import AnalyticsRequest
		return AnalyticsRequest(self.request_adapter, path_parameters)

	def columns(self,
		site_id: str,
		path: str,
	) -> ColumnsRequest:
		if site_id is None:
			raise TypeError("site_id cannot be null.")
		if path is None:
			raise TypeError("path cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["site%2Did"] =  site_id
		path_parameters["path"] =  path

		from .columns import ColumnsRequest
		return ColumnsRequest(self.request_adapter, path_parameters)

	def content_models(self,
		site_id: str,
		path: str,
	) -> ContentModelsRequest:
		if site_id is None:
			raise TypeError("site_id cannot be null.")
		if path is None:
			raise TypeError("path cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["site%2Did"] =  site_id
		path_parameters["path"] =  path

		from .content_models import ContentModelsRequest
		return ContentModelsRequest(self.request_adapter, path_parameters)

	def content_types(self,
		site_id: str,
		path: str,
	) -> ContentTypesRequest:
		if site_id is None:
			raise TypeError("site_id cannot be null.")
		if path is None:
			raise TypeError("path cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["site%2Did"] =  site_id
		path_parameters["path"] =  path

		from .content_types import ContentTypesRequest
		return ContentTypesRequest(self.request_adapter, path_parameters)

	def created_by_user(self,
		site_id: str,
		path: str,
	) -> CreatedByUserRequest:
		if site_id is None:
			raise TypeError("site_id cannot be null.")
		if path is None:
			raise TypeError("path cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["site%2Did"] =  site_id
		path_parameters["path"] =  path

		from .created_by_user import CreatedByUserRequest
		return CreatedByUserRequest(self.request_adapter, path_parameters)

	def document_processing_jobs(self,
		site_id: str,
		path: str,
	) -> DocumentProcessingJobsRequest:
		if site_id is None:
			raise TypeError("site_id cannot be null.")
		if path is None:
			raise TypeError("path cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["site%2Did"] =  site_id
		path_parameters["path"] =  path

		from .document_processing_jobs import DocumentProcessingJobsRequest
		return DocumentProcessingJobsRequest(self.request_adapter, path_parameters)

	def drive(self,
		site_id: str,
		path: str,
	) -> DriveRequest:
		if site_id is None:
			raise TypeError("site_id cannot be null.")
		if path is None:
			raise TypeError("path cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["site%2Did"] =  site_id
		path_parameters["path"] =  path

		from .drive import DriveRequest
		return DriveRequest(self.request_adapter, path_parameters)

	def drives(self,
		site_id: str,
		path: str,
	) -> DrivesRequest:
		if site_id is None:
			raise TypeError("site_id cannot be null.")
		if path is None:
			raise TypeError("path cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["site%2Did"] =  site_id
		path_parameters["path"] =  path

		from .drives import DrivesRequest
		return DrivesRequest(self.request_adapter, path_parameters)

	def external_columns(self,
		site_id: str,
		path: str,
	) -> ExternalColumnsRequest:
		if site_id is None:
			raise TypeError("site_id cannot be null.")
		if path is None:
			raise TypeError("path cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["site%2Did"] =  site_id
		path_parameters["path"] =  path

		from .external_columns import ExternalColumnsRequest
		return ExternalColumnsRequest(self.request_adapter, path_parameters)

	def information_protection(self,
		site_id: str,
		path: str,
	) -> InformationProtectionRequest:
		if site_id is None:
			raise TypeError("site_id cannot be null.")
		if path is None:
			raise TypeError("path cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["site%2Did"] =  site_id
		path_parameters["path"] =  path

		from .information_protection import InformationProtectionRequest
		return InformationProtectionRequest(self.request_adapter, path_parameters)

	def items(self,
		site_id: str,
		path: str,
	) -> ItemsRequest:
		if site_id is None:
			raise TypeError("site_id cannot be null.")
		if path is None:
			raise TypeError("path cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["site%2Did"] =  site_id
		path_parameters["path"] =  path

		from .items import ItemsRequest
		return ItemsRequest(self.request_adapter, path_parameters)

	def last_modified_by_user(self,
		site_id: str,
		path: str,
	) -> LastModifiedByUserRequest:
		if site_id is None:
			raise TypeError("site_id cannot be null.")
		if path is None:
			raise TypeError("path cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["site%2Did"] =  site_id
		path_parameters["path"] =  path

		from .last_modified_by_user import LastModifiedByUserRequest
		return LastModifiedByUserRequest(self.request_adapter, path_parameters)

	def lists(self,
		site_id: str,
		path: str,
	) -> ListsRequest:
		if site_id is None:
			raise TypeError("site_id cannot be null.")
		if path is None:
			raise TypeError("path cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["site%2Did"] =  site_id
		path_parameters["path"] =  path

		from .lists import ListsRequest
		return ListsRequest(self.request_adapter, path_parameters)

	def archive(self,
		site_id: str,
		path: str,
	) -> ArchiveRequest:
		if site_id is None:
			raise TypeError("site_id cannot be null.")
		if path is None:
			raise TypeError("path cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["site%2Did"] =  site_id
		path_parameters["path"] =  path

		from .archive import ArchiveRequest
		return ArchiveRequest(self.request_adapter, path_parameters)

	def get_activities_by_interval_with_startdatetime_enddatetime_interval(self,
		site_id: str,
		path: str,
		startDateTime: str,
		endDateTime: str,
		interval: str,
	) -> GetActivitiesByIntervalWithStartDateTimeEndDateTimeIntervalRequest:
		if site_id is None:
			raise TypeError("site_id cannot be null.")
		if path is None:
			raise TypeError("path cannot be null.")
		if startDateTime is None:
			raise TypeError("startDateTime cannot be null.")
		if endDateTime is None:
			raise TypeError("endDateTime cannot be null.")
		if interval is None:
			raise TypeError("interval cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["site%2Did"] =  site_id
		path_parameters["path"] =  path
		path_parameters["startDateTime"] =  startDateTime
		path_parameters["endDateTime"] =  endDateTime
		path_parameters["interval"] =  interval

		from .get_activities_by_interval_with_startdatetime_enddatetime_interval import GetActivitiesByIntervalWithStartDateTimeEndDateTimeIntervalRequest
		return GetActivitiesByIntervalWithStartDateTimeEndDateTimeIntervalRequest(self.request_adapter, path_parameters)

	def get_applicable_content_types_for_list_with_listid(self,
		site_id: str,
		path: str,
		listId: str,
	) -> GetApplicableContentTypesForListWithListIdRequest:
		if site_id is None:
			raise TypeError("site_id cannot be null.")
		if path is None:
			raise TypeError("path cannot be null.")
		if listId is None:
			raise TypeError("listId cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["site%2Did"] =  site_id
		path_parameters["path"] =  path
		path_parameters["listId"] =  listId

		from .get_applicable_content_types_for_list_with_listid import GetApplicableContentTypesForListWithListIdRequest
		return GetApplicableContentTypesForListWithListIdRequest(self.request_adapter, path_parameters)

	def unarchive(self,
		site_id: str,
		path: str,
	) -> UnarchiveRequest:
		if site_id is None:
			raise TypeError("site_id cannot be null.")
		if path is None:
			raise TypeError("path cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["site%2Did"] =  site_id
		path_parameters["path"] =  path

		from .unarchive import UnarchiveRequest
		return UnarchiveRequest(self.request_adapter, path_parameters)

	def onenote(self,
		site_id: str,
		path: str,
	) -> OnenoteRequest:
		if site_id is None:
			raise TypeError("site_id cannot be null.")
		if path is None:
			raise TypeError("path cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["site%2Did"] =  site_id
		path_parameters["path"] =  path

		from .onenote import OnenoteRequest
		return OnenoteRequest(self.request_adapter, path_parameters)

	def operations(self,
		site_id: str,
		path: str,
	) -> OperationsRequest:
		if site_id is None:
			raise TypeError("site_id cannot be null.")
		if path is None:
			raise TypeError("path cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["site%2Did"] =  site_id
		path_parameters["path"] =  path

		from .operations import OperationsRequest
		return OperationsRequest(self.request_adapter, path_parameters)

	def pages(self,
		site_id: str,
		path: str,
	) -> PagesRequest:
		if site_id is None:
			raise TypeError("site_id cannot be null.")
		if path is None:
			raise TypeError("path cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["site%2Did"] =  site_id
		path_parameters["path"] =  path

		from .pages import PagesRequest
		return PagesRequest(self.request_adapter, path_parameters)

	def page_templates(self,
		site_id: str,
		path: str,
	) -> PageTemplatesRequest:
		if site_id is None:
			raise TypeError("site_id cannot be null.")
		if path is None:
			raise TypeError("path cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["site%2Did"] =  site_id
		path_parameters["path"] =  path

		from .page_templates import PageTemplatesRequest
		return PageTemplatesRequest(self.request_adapter, path_parameters)

	def permissions(self,
		site_id: str,
		path: str,
	) -> PermissionsRequest:
		if site_id is None:
			raise TypeError("site_id cannot be null.")
		if path is None:
			raise TypeError("path cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["site%2Did"] =  site_id
		path_parameters["path"] =  path

		from .permissions import PermissionsRequest
		return PermissionsRequest(self.request_adapter, path_parameters)

	def recycle_bin(self,
		site_id: str,
		path: str,
	) -> RecycleBinRequest:
		if site_id is None:
			raise TypeError("site_id cannot be null.")
		if path is None:
			raise TypeError("path cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["site%2Did"] =  site_id
		path_parameters["path"] =  path

		from .recycle_bin import RecycleBinRequest
		return RecycleBinRequest(self.request_adapter, path_parameters)

	def sites(self,
		site_id: str,
		path: str,
	) -> SitesRequest:
		if site_id is None:
			raise TypeError("site_id cannot be null.")
		if path is None:
			raise TypeError("path cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["site%2Did"] =  site_id
		path_parameters["path"] =  path

		from .sites import SitesRequest
		return SitesRequest(self.request_adapter, path_parameters)

	def term_store(self,
		site_id: str,
		path: str,
	) -> TermStoreRequest:
		if site_id is None:
			raise TypeError("site_id cannot be null.")
		if path is None:
			raise TypeError("path cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["site%2Did"] =  site_id
		path_parameters["path"] =  path

		from .term_store import TermStoreRequest
		return TermStoreRequest(self.request_adapter, path_parameters)

