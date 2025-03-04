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
	from .workbook import WorkbookRequest
	from .versions import VersionsRequest
	from .thumbnails import ThumbnailsRequest
	from .subscriptions import SubscriptionsRequest
	from .retention_label import RetentionLabelRequest
	from .permissions import PermissionsRequest
	from .validate_permission import ValidatePermissionRequest
	from .unfollow import UnfollowRequest
	from .search import SearchRequest
	from .restore import RestoreRequest
	from .preview import PreviewRequest
	from .permanent_delete import PermanentDeleteRequest
	from .invite import InviteRequest
	from .get_activities_by_interval import GetActivitiesByIntervalRequest
	from .follow import FollowRequest
	from .extract_sensitivity_labels import ExtractSensitivityLabelsRequest
	from .discard_checkout import DiscardCheckoutRequest
	from .delta import DeltaRequest
	from .create_upload_session import CreateUploadSessionRequest
	from .create_link import CreateLinkRequest
	from .copy import CopyRequest
	from .checkout import CheckoutRequest
	from .checkin import CheckinRequest
	from .assign_sensitivity_label import AssignSensitivityLabelRequest
	from .list_item import ListItemRequest
	from .last_modified_by_user import LastModifiedByUserRequest
	from .created_by_user import CreatedByUserRequest
	from .content import ContentRequest
	from .children import ChildrenRequest
	from .analytics import AnalyticsRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.models.drive_item import DriveItem
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class ByDriveItemIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/drives/{drive%2Did}/items/{driveItem%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> DriveItem:
		"""
		Get items from drives
		All items contained in the drive. Read-only. Nullable.
		"""
		tags = ['drives.driveItem']

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
		return await self.request_adapter.send_async(request_info, DriveItem, error_mapping)

	async def patch(
		self,
		body: DriveItem,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> DriveItem:
		"""
		Update the navigation property items in drives
		
		"""
		tags = ['drives.driveItem']

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
		return await self.request_adapter.send_async(request_info, DriveItem, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property items for drives
		
		"""
		tags = ['drives.driveItem']
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



	def with_url(self, raw_url: str) -> ByDriveItemIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByDriveItemIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByDriveItemIdRequest(self.request_adapter, self.path_parameters)

	def analytics(self,
		drive_id: str,
		driveItem_id: str,
	) -> AnalyticsRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .analytics import AnalyticsRequest
		return AnalyticsRequest(self.request_adapter, path_parameters)

	def children(self,
		drive_id: str,
		driveItem_id: str,
	) -> ChildrenRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .children import ChildrenRequest
		return ChildrenRequest(self.request_adapter, path_parameters)

	def content(self,
		drive_id: str,
		driveItem_id: str,
	) -> ContentRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .content import ContentRequest
		return ContentRequest(self.request_adapter, path_parameters)

	def created_by_user(self,
		drive_id: str,
		driveItem_id: str,
	) -> CreatedByUserRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .created_by_user import CreatedByUserRequest
		return CreatedByUserRequest(self.request_adapter, path_parameters)

	def last_modified_by_user(self,
		drive_id: str,
		driveItem_id: str,
	) -> LastModifiedByUserRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .last_modified_by_user import LastModifiedByUserRequest
		return LastModifiedByUserRequest(self.request_adapter, path_parameters)

	def list_item(self,
		drive_id: str,
		driveItem_id: str,
	) -> ListItemRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .list_item import ListItemRequest
		return ListItemRequest(self.request_adapter, path_parameters)

	def assign_sensitivity_label(self,
		drive_id: str,
		driveItem_id: str,
	) -> AssignSensitivityLabelRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .assign_sensitivity_label import AssignSensitivityLabelRequest
		return AssignSensitivityLabelRequest(self.request_adapter, path_parameters)

	def checkin(self,
		drive_id: str,
		driveItem_id: str,
	) -> CheckinRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .checkin import CheckinRequest
		return CheckinRequest(self.request_adapter, path_parameters)

	def checkout(self,
		drive_id: str,
		driveItem_id: str,
	) -> CheckoutRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .checkout import CheckoutRequest
		return CheckoutRequest(self.request_adapter, path_parameters)

	def copy(self,
		drive_id: str,
		driveItem_id: str,
	) -> CopyRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .copy import CopyRequest
		return CopyRequest(self.request_adapter, path_parameters)

	def create_link(self,
		drive_id: str,
		driveItem_id: str,
	) -> CreateLinkRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .create_link import CreateLinkRequest
		return CreateLinkRequest(self.request_adapter, path_parameters)

	def create_upload_session(self,
		drive_id: str,
		driveItem_id: str,
	) -> CreateUploadSessionRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .create_upload_session import CreateUploadSessionRequest
		return CreateUploadSessionRequest(self.request_adapter, path_parameters)

	def delta(self,
		drive_id: str,
		driveItem_id: str,
	) -> DeltaRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .delta import DeltaRequest
		return DeltaRequest(self.request_adapter, path_parameters)

	def discard_checkout(self,
		drive_id: str,
		driveItem_id: str,
	) -> DiscardCheckoutRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .discard_checkout import DiscardCheckoutRequest
		return DiscardCheckoutRequest(self.request_adapter, path_parameters)

	def extract_sensitivity_labels(self,
		drive_id: str,
		driveItem_id: str,
	) -> ExtractSensitivityLabelsRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .extract_sensitivity_labels import ExtractSensitivityLabelsRequest
		return ExtractSensitivityLabelsRequest(self.request_adapter, path_parameters)

	def follow(self,
		drive_id: str,
		driveItem_id: str,
	) -> FollowRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .follow import FollowRequest
		return FollowRequest(self.request_adapter, path_parameters)

	def get_activities_by_interval(self,
		drive_id: str,
		driveItem_id: str,
	) -> GetActivitiesByIntervalRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .get_activities_by_interval import GetActivitiesByIntervalRequest
		return GetActivitiesByIntervalRequest(self.request_adapter, path_parameters)

	def invite(self,
		drive_id: str,
		driveItem_id: str,
	) -> InviteRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .invite import InviteRequest
		return InviteRequest(self.request_adapter, path_parameters)

	def permanent_delete(self,
		drive_id: str,
		driveItem_id: str,
	) -> PermanentDeleteRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .permanent_delete import PermanentDeleteRequest
		return PermanentDeleteRequest(self.request_adapter, path_parameters)

	def preview(self,
		drive_id: str,
		driveItem_id: str,
	) -> PreviewRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .preview import PreviewRequest
		return PreviewRequest(self.request_adapter, path_parameters)

	def restore(self,
		drive_id: str,
		driveItem_id: str,
	) -> RestoreRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .restore import RestoreRequest
		return RestoreRequest(self.request_adapter, path_parameters)

	def search(self,
		drive_id: str,
		driveItem_id: str,
		q: str,
	) -> SearchRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if q is None:
			raise TypeError("q cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["q"] =  q

		from .search import SearchRequest
		return SearchRequest(self.request_adapter, path_parameters)

	def unfollow(self,
		drive_id: str,
		driveItem_id: str,
	) -> UnfollowRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .unfollow import UnfollowRequest
		return UnfollowRequest(self.request_adapter, path_parameters)

	def validate_permission(self,
		drive_id: str,
		driveItem_id: str,
	) -> ValidatePermissionRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .validate_permission import ValidatePermissionRequest
		return ValidatePermissionRequest(self.request_adapter, path_parameters)

	def permissions(self,
		drive_id: str,
		driveItem_id: str,
	) -> PermissionsRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .permissions import PermissionsRequest
		return PermissionsRequest(self.request_adapter, path_parameters)

	def retention_label(self,
		drive_id: str,
		driveItem_id: str,
	) -> RetentionLabelRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .retention_label import RetentionLabelRequest
		return RetentionLabelRequest(self.request_adapter, path_parameters)

	def subscriptions(self,
		drive_id: str,
		driveItem_id: str,
	) -> SubscriptionsRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .subscriptions import SubscriptionsRequest
		return SubscriptionsRequest(self.request_adapter, path_parameters)

	def thumbnails(self,
		drive_id: str,
		driveItem_id: str,
	) -> ThumbnailsRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .thumbnails import ThumbnailsRequest
		return ThumbnailsRequest(self.request_adapter, path_parameters)

	def versions(self,
		drive_id: str,
		driveItem_id: str,
	) -> VersionsRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .versions import VersionsRequest
		return VersionsRequest(self.request_adapter, path_parameters)

	def workbook(self,
		drive_id: str,
		driveItem_id: str,
	) -> WorkbookRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .workbook import WorkbookRequest
		return WorkbookRequest(self.request_adapter, path_parameters)

