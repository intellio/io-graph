# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .transitive_members import TransitiveMembersRequest
	from .transitive_member_of import TransitiveMemberOfRequest
	from .threads import ThreadsRequest
	from .team import TeamRequest
	from .sites import SitesRequest
	from .settings import SettingsRequest
	from .service_provisioning_errors import ServiceProvisioningErrorsRequest
	from .rejected_senders import RejectedSendersRequest
	from .planner import PlannerRequest
	from .photos import PhotosRequest
	from .photo import PhotoRequest
	from .permission_grants import PermissionGrantsRequest
	from .owners import OwnersRequest
	from .onenote import OnenoteRequest
	from .validate_properties import ValidatePropertiesRequest
	from .unsubscribe_by_mail import UnsubscribeByMailRequest
	from .subscribe_by_mail import SubscribeByMailRequest
	from .retry_service_provisioning import RetryServiceProvisioningRequest
	from .restore import RestoreRequest
	from .reset_unseen_count import ResetUnseenCountRequest
	from .renew import RenewRequest
	from .remove_favorite import RemoveFavoriteRequest
	from .get_member_objects import GetMemberObjectsRequest
	from .get_member_groups import GetMemberGroupsRequest
	from .check_member_objects import CheckMemberObjectsRequest
	from .check_member_groups import CheckMemberGroupsRequest
	from .check_granted_permissions_for_app import CheckGrantedPermissionsForAppRequest
	from .assign_license import AssignLicenseRequest
	from .add_favorite import AddFavoriteRequest
	from .members_with_license_errors import MembersWithLicenseErrorsRequest
	from .members import MembersRequest
	from .member_of import MemberOfRequest
	from .group_lifecycle_policies import GroupLifecyclePoliciesRequest
	from .extensions import ExtensionsRequest
	from .events import EventsRequest
	from .drives import DrivesRequest
	from .drive import DriveRequest
	from .created_on_behalf_of import CreatedOnBehalfOfRequest
	from .conversations import ConversationsRequest
	from .calendar_view import CalendarViewRequest
	from .calendar import CalendarRequest
	from .app_role_assignments import AppRoleAssignmentsRequest
	from .accepted_senders import AcceptedSendersRequest
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.models.group import Group
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class ByGroupIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/groups/{group%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> Group:
		"""
		Get group
		Get the properties and relationships of a group object. This operation returns by default only a subset of all the available properties, as noted in the Properties section. To get properties that aren't_ returned by default, specify them in a $select OData query option. The hasMembersWithLicenseErrors and isArchived properties are an exception and aren't returned in the $select query.
		Find more info here: https://learn.microsoft.com/graph/api/group-get?view=graph-rest-1.0
		"""
		tags = ['groups.group']

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
		return await self.request_adapter.send_async(request_info, Group, error_mapping)

	async def patch(
		self,
		body: Group,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> Group:
		"""
		Upsert group
		Create a new group object if it doesn't exist, or update the properties of an existing group object.
You can create or update the following types of group: By default, this operation returns only a subset of the properties for each group. For a list of properties that are returned by default, see the Properties section of the group resource. To get properties that are not returned by default, do a GET operation and specify the properties in a $select OData query option.
		Find more info here: https://learn.microsoft.com/graph/api/group-upsert?view=graph-rest-1.0
		"""
		tags = ['groups.group']

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
		return await self.request_adapter.send_async(request_info, Group, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete group
		Delete a group. When deleted, Microsoft 365 groups are moved to a temporary container and can be restored within 30 days. After that time, they're permanently deleted. This isn't applicable to Security groups and Distribution groups which are permanently deleted immediately. To learn more, see deletedItems.
		Find more info here: https://learn.microsoft.com/graph/api/group-delete?view=graph-rest-1.0
		"""
		tags = ['groups.group']
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



	def with_url(self, raw_url: str) -> ByGroupIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByGroupIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByGroupIdRequest(self.request_adapter, self.path_parameters)

	@property
	def accepted_senders(self,
	) -> AcceptedSendersRequest:
		from .accepted_senders import AcceptedSendersRequest
		return AcceptedSendersRequest(self.request_adapter, self.path_parameters)

	@property
	def app_role_assignments(self,
	) -> AppRoleAssignmentsRequest:
		from .app_role_assignments import AppRoleAssignmentsRequest
		return AppRoleAssignmentsRequest(self.request_adapter, self.path_parameters)

	@property
	def calendar(self,
	) -> CalendarRequest:
		from .calendar import CalendarRequest
		return CalendarRequest(self.request_adapter, self.path_parameters)

	@property
	def calendar_view(self,
	) -> CalendarViewRequest:
		from .calendar_view import CalendarViewRequest
		return CalendarViewRequest(self.request_adapter, self.path_parameters)

	@property
	def conversations(self,
	) -> ConversationsRequest:
		from .conversations import ConversationsRequest
		return ConversationsRequest(self.request_adapter, self.path_parameters)

	@property
	def created_on_behalf_of(self,
	) -> CreatedOnBehalfOfRequest:
		from .created_on_behalf_of import CreatedOnBehalfOfRequest
		return CreatedOnBehalfOfRequest(self.request_adapter, self.path_parameters)

	@property
	def drive(self,
	) -> DriveRequest:
		from .drive import DriveRequest
		return DriveRequest(self.request_adapter, self.path_parameters)

	@property
	def drives(self,
	) -> DrivesRequest:
		from .drives import DrivesRequest
		return DrivesRequest(self.request_adapter, self.path_parameters)

	@property
	def events(self,
	) -> EventsRequest:
		from .events import EventsRequest
		return EventsRequest(self.request_adapter, self.path_parameters)

	@property
	def extensions(self,
	) -> ExtensionsRequest:
		from .extensions import ExtensionsRequest
		return ExtensionsRequest(self.request_adapter, self.path_parameters)

	@property
	def group_lifecycle_policies(self,
	) -> GroupLifecyclePoliciesRequest:
		from .group_lifecycle_policies import GroupLifecyclePoliciesRequest
		return GroupLifecyclePoliciesRequest(self.request_adapter, self.path_parameters)

	@property
	def member_of(self,
	) -> MemberOfRequest:
		from .member_of import MemberOfRequest
		return MemberOfRequest(self.request_adapter, self.path_parameters)

	@property
	def members(self,
	) -> MembersRequest:
		from .members import MembersRequest
		return MembersRequest(self.request_adapter, self.path_parameters)

	@property
	def members_with_license_errors(self,
	) -> MembersWithLicenseErrorsRequest:
		from .members_with_license_errors import MembersWithLicenseErrorsRequest
		return MembersWithLicenseErrorsRequest(self.request_adapter, self.path_parameters)

	@property
	def add_favorite(self,
	) -> AddFavoriteRequest:
		from .add_favorite import AddFavoriteRequest
		return AddFavoriteRequest(self.request_adapter, self.path_parameters)

	@property
	def assign_license(self,
	) -> AssignLicenseRequest:
		from .assign_license import AssignLicenseRequest
		return AssignLicenseRequest(self.request_adapter, self.path_parameters)

	@property
	def check_granted_permissions_for_app(self,
	) -> CheckGrantedPermissionsForAppRequest:
		from .check_granted_permissions_for_app import CheckGrantedPermissionsForAppRequest
		return CheckGrantedPermissionsForAppRequest(self.request_adapter, self.path_parameters)

	@property
	def check_member_groups(self,
	) -> CheckMemberGroupsRequest:
		from .check_member_groups import CheckMemberGroupsRequest
		return CheckMemberGroupsRequest(self.request_adapter, self.path_parameters)

	@property
	def check_member_objects(self,
	) -> CheckMemberObjectsRequest:
		from .check_member_objects import CheckMemberObjectsRequest
		return CheckMemberObjectsRequest(self.request_adapter, self.path_parameters)

	@property
	def get_member_groups(self,
	) -> GetMemberGroupsRequest:
		from .get_member_groups import GetMemberGroupsRequest
		return GetMemberGroupsRequest(self.request_adapter, self.path_parameters)

	@property
	def get_member_objects(self,
	) -> GetMemberObjectsRequest:
		from .get_member_objects import GetMemberObjectsRequest
		return GetMemberObjectsRequest(self.request_adapter, self.path_parameters)

	@property
	def remove_favorite(self,
	) -> RemoveFavoriteRequest:
		from .remove_favorite import RemoveFavoriteRequest
		return RemoveFavoriteRequest(self.request_adapter, self.path_parameters)

	@property
	def renew(self,
	) -> RenewRequest:
		from .renew import RenewRequest
		return RenewRequest(self.request_adapter, self.path_parameters)

	@property
	def reset_unseen_count(self,
	) -> ResetUnseenCountRequest:
		from .reset_unseen_count import ResetUnseenCountRequest
		return ResetUnseenCountRequest(self.request_adapter, self.path_parameters)

	@property
	def restore(self,
	) -> RestoreRequest:
		from .restore import RestoreRequest
		return RestoreRequest(self.request_adapter, self.path_parameters)

	@property
	def retry_service_provisioning(self,
	) -> RetryServiceProvisioningRequest:
		from .retry_service_provisioning import RetryServiceProvisioningRequest
		return RetryServiceProvisioningRequest(self.request_adapter, self.path_parameters)

	@property
	def subscribe_by_mail(self,
	) -> SubscribeByMailRequest:
		from .subscribe_by_mail import SubscribeByMailRequest
		return SubscribeByMailRequest(self.request_adapter, self.path_parameters)

	@property
	def unsubscribe_by_mail(self,
	) -> UnsubscribeByMailRequest:
		from .unsubscribe_by_mail import UnsubscribeByMailRequest
		return UnsubscribeByMailRequest(self.request_adapter, self.path_parameters)

	@property
	def validate_properties(self,
	) -> ValidatePropertiesRequest:
		from .validate_properties import ValidatePropertiesRequest
		return ValidatePropertiesRequest(self.request_adapter, self.path_parameters)

	@property
	def onenote(self,
	) -> OnenoteRequest:
		from .onenote import OnenoteRequest
		return OnenoteRequest(self.request_adapter, self.path_parameters)

	@property
	def owners(self,
	) -> OwnersRequest:
		from .owners import OwnersRequest
		return OwnersRequest(self.request_adapter, self.path_parameters)

	@property
	def permission_grants(self,
	) -> PermissionGrantsRequest:
		from .permission_grants import PermissionGrantsRequest
		return PermissionGrantsRequest(self.request_adapter, self.path_parameters)

	@property
	def photo(self,
	) -> PhotoRequest:
		from .photo import PhotoRequest
		return PhotoRequest(self.request_adapter, self.path_parameters)

	@property
	def photos(self,
	) -> PhotosRequest:
		from .photos import PhotosRequest
		return PhotosRequest(self.request_adapter, self.path_parameters)

	@property
	def planner(self,
	) -> PlannerRequest:
		from .planner import PlannerRequest
		return PlannerRequest(self.request_adapter, self.path_parameters)

	@property
	def rejected_senders(self,
	) -> RejectedSendersRequest:
		from .rejected_senders import RejectedSendersRequest
		return RejectedSendersRequest(self.request_adapter, self.path_parameters)

	@property
	def service_provisioning_errors(self,
	) -> ServiceProvisioningErrorsRequest:
		from .service_provisioning_errors import ServiceProvisioningErrorsRequest
		return ServiceProvisioningErrorsRequest(self.request_adapter, self.path_parameters)

	@property
	def settings(self,
	) -> SettingsRequest:
		from .settings import SettingsRequest
		return SettingsRequest(self.request_adapter, self.path_parameters)

	@property
	def sites(self,
	) -> SitesRequest:
		from .sites import SitesRequest
		return SitesRequest(self.request_adapter, self.path_parameters)

	@property
	def team(self,
	) -> TeamRequest:
		from .team import TeamRequest
		return TeamRequest(self.request_adapter, self.path_parameters)

	@property
	def threads(self,
	) -> ThreadsRequest:
		from .threads import ThreadsRequest
		return ThreadsRequest(self.request_adapter, self.path_parameters)

	@property
	def transitive_member_of(self,
	) -> TransitiveMemberOfRequest:
		from .transitive_member_of import TransitiveMemberOfRequest
		return TransitiveMemberOfRequest(self.request_adapter, self.path_parameters)

	@property
	def transitive_members(self,
	) -> TransitiveMembersRequest:
		from .transitive_members import TransitiveMembersRequest
		return TransitiveMembersRequest(self.request_adapter, self.path_parameters)

