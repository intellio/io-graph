# Auto-generated client

from __future__ import annotations
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
	from .restore import RestoreRequest
	from .preview import PreviewRequest
	from .permanent_delete import PermanentDeleteRequest
	from .invite import InviteRequest
	from .follow import FollowRequest
	from .extract_sensitivity_labels import ExtractSensitivityLabelsRequest
	from .discard_checkout import DiscardCheckoutRequest
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

	@property
	def analytics(self,
	) -> AnalyticsRequest:
		from .analytics import AnalyticsRequest
		return AnalyticsRequest(self.request_adapter, self.path_parameters)

	@property
	def children(self,
	) -> ChildrenRequest:
		from .children import ChildrenRequest
		return ChildrenRequest(self.request_adapter, self.path_parameters)

	@property
	def content(self,
	) -> ContentRequest:
		from .content import ContentRequest
		return ContentRequest(self.request_adapter, self.path_parameters)

	@property
	def created_by_user(self,
	) -> CreatedByUserRequest:
		from .created_by_user import CreatedByUserRequest
		return CreatedByUserRequest(self.request_adapter, self.path_parameters)

	@property
	def last_modified_by_user(self,
	) -> LastModifiedByUserRequest:
		from .last_modified_by_user import LastModifiedByUserRequest
		return LastModifiedByUserRequest(self.request_adapter, self.path_parameters)

	@property
	def list_item(self,
	) -> ListItemRequest:
		from .list_item import ListItemRequest
		return ListItemRequest(self.request_adapter, self.path_parameters)

	@property
	def assign_sensitivity_label(self,
	) -> AssignSensitivityLabelRequest:
		from .assign_sensitivity_label import AssignSensitivityLabelRequest
		return AssignSensitivityLabelRequest(self.request_adapter, self.path_parameters)

	@property
	def checkin(self,
	) -> CheckinRequest:
		from .checkin import CheckinRequest
		return CheckinRequest(self.request_adapter, self.path_parameters)

	@property
	def checkout(self,
	) -> CheckoutRequest:
		from .checkout import CheckoutRequest
		return CheckoutRequest(self.request_adapter, self.path_parameters)

	@property
	def copy(self,
	) -> CopyRequest:
		from .copy import CopyRequest
		return CopyRequest(self.request_adapter, self.path_parameters)

	@property
	def create_link(self,
	) -> CreateLinkRequest:
		from .create_link import CreateLinkRequest
		return CreateLinkRequest(self.request_adapter, self.path_parameters)

	@property
	def create_upload_session(self,
	) -> CreateUploadSessionRequest:
		from .create_upload_session import CreateUploadSessionRequest
		return CreateUploadSessionRequest(self.request_adapter, self.path_parameters)

	@property
	def discard_checkout(self,
	) -> DiscardCheckoutRequest:
		from .discard_checkout import DiscardCheckoutRequest
		return DiscardCheckoutRequest(self.request_adapter, self.path_parameters)

	@property
	def extract_sensitivity_labels(self,
	) -> ExtractSensitivityLabelsRequest:
		from .extract_sensitivity_labels import ExtractSensitivityLabelsRequest
		return ExtractSensitivityLabelsRequest(self.request_adapter, self.path_parameters)

	@property
	def follow(self,
	) -> FollowRequest:
		from .follow import FollowRequest
		return FollowRequest(self.request_adapter, self.path_parameters)

	@property
	def invite(self,
	) -> InviteRequest:
		from .invite import InviteRequest
		return InviteRequest(self.request_adapter, self.path_parameters)

	@property
	def permanent_delete(self,
	) -> PermanentDeleteRequest:
		from .permanent_delete import PermanentDeleteRequest
		return PermanentDeleteRequest(self.request_adapter, self.path_parameters)

	@property
	def preview(self,
	) -> PreviewRequest:
		from .preview import PreviewRequest
		return PreviewRequest(self.request_adapter, self.path_parameters)

	@property
	def restore(self,
	) -> RestoreRequest:
		from .restore import RestoreRequest
		return RestoreRequest(self.request_adapter, self.path_parameters)

	@property
	def unfollow(self,
	) -> UnfollowRequest:
		from .unfollow import UnfollowRequest
		return UnfollowRequest(self.request_adapter, self.path_parameters)

	@property
	def validate_permission(self,
	) -> ValidatePermissionRequest:
		from .validate_permission import ValidatePermissionRequest
		return ValidatePermissionRequest(self.request_adapter, self.path_parameters)

	@property
	def permissions(self,
	) -> PermissionsRequest:
		from .permissions import PermissionsRequest
		return PermissionsRequest(self.request_adapter, self.path_parameters)

	@property
	def retention_label(self,
	) -> RetentionLabelRequest:
		from .retention_label import RetentionLabelRequest
		return RetentionLabelRequest(self.request_adapter, self.path_parameters)

	@property
	def subscriptions(self,
	) -> SubscriptionsRequest:
		from .subscriptions import SubscriptionsRequest
		return SubscriptionsRequest(self.request_adapter, self.path_parameters)

	@property
	def thumbnails(self,
	) -> ThumbnailsRequest:
		from .thumbnails import ThumbnailsRequest
		return ThumbnailsRequest(self.request_adapter, self.path_parameters)

	@property
	def versions(self,
	) -> VersionsRequest:
		from .versions import VersionsRequest
		return VersionsRequest(self.request_adapter, self.path_parameters)

	@property
	def workbook(self,
	) -> WorkbookRequest:
		from .workbook import WorkbookRequest
		return WorkbookRequest(self.request_adapter, self.path_parameters)

