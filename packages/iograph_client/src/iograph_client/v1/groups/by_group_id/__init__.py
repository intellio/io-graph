# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
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
from iograph_models.v1.group import Group
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError


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

	def accepted_senders(self,
		group_id: str,
	) -> AcceptedSendersRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id

		from .accepted_senders import AcceptedSendersRequest
		return AcceptedSendersRequest(self.request_adapter, path_parameters)

	def app_role_assignments(self,
		group_id: str,
	) -> AppRoleAssignmentsRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id

		from .app_role_assignments import AppRoleAssignmentsRequest
		return AppRoleAssignmentsRequest(self.request_adapter, path_parameters)

	def calendar(self,
		group_id: str,
	) -> CalendarRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id

		from .calendar import CalendarRequest
		return CalendarRequest(self.request_adapter, path_parameters)

	def calendar_view(self,
		group_id: str,
	) -> CalendarViewRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id

		from .calendar_view import CalendarViewRequest
		return CalendarViewRequest(self.request_adapter, path_parameters)

	def conversations(self,
		group_id: str,
	) -> ConversationsRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id

		from .conversations import ConversationsRequest
		return ConversationsRequest(self.request_adapter, path_parameters)

	def created_on_behalf_of(self,
		group_id: str,
	) -> CreatedOnBehalfOfRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id

		from .created_on_behalf_of import CreatedOnBehalfOfRequest
		return CreatedOnBehalfOfRequest(self.request_adapter, path_parameters)

	def drive(self,
		group_id: str,
	) -> DriveRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id

		from .drive import DriveRequest
		return DriveRequest(self.request_adapter, path_parameters)

	def drives(self,
		group_id: str,
	) -> DrivesRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id

		from .drives import DrivesRequest
		return DrivesRequest(self.request_adapter, path_parameters)

	def events(self,
		group_id: str,
	) -> EventsRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id

		from .events import EventsRequest
		return EventsRequest(self.request_adapter, path_parameters)

	def extensions(self,
		group_id: str,
	) -> ExtensionsRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id

		from .extensions import ExtensionsRequest
		return ExtensionsRequest(self.request_adapter, path_parameters)

	def group_lifecycle_policies(self,
		group_id: str,
	) -> GroupLifecyclePoliciesRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id

		from .group_lifecycle_policies import GroupLifecyclePoliciesRequest
		return GroupLifecyclePoliciesRequest(self.request_adapter, path_parameters)

	def member_of(self,
		group_id: str,
	) -> MemberOfRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id

		from .member_of import MemberOfRequest
		return MemberOfRequest(self.request_adapter, path_parameters)

	def members(self,
		group_id: str,
	) -> MembersRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id

		from .members import MembersRequest
		return MembersRequest(self.request_adapter, path_parameters)

	def members_with_license_errors(self,
		group_id: str,
	) -> MembersWithLicenseErrorsRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id

		from .members_with_license_errors import MembersWithLicenseErrorsRequest
		return MembersWithLicenseErrorsRequest(self.request_adapter, path_parameters)

	def add_favorite(self,
		group_id: str,
	) -> AddFavoriteRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id

		from .add_favorite import AddFavoriteRequest
		return AddFavoriteRequest(self.request_adapter, path_parameters)

	def assign_license(self,
		group_id: str,
	) -> AssignLicenseRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id

		from .assign_license import AssignLicenseRequest
		return AssignLicenseRequest(self.request_adapter, path_parameters)

	def check_granted_permissions_for_app(self,
		group_id: str,
	) -> CheckGrantedPermissionsForAppRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id

		from .check_granted_permissions_for_app import CheckGrantedPermissionsForAppRequest
		return CheckGrantedPermissionsForAppRequest(self.request_adapter, path_parameters)

	def check_member_groups(self,
		group_id: str,
	) -> CheckMemberGroupsRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id

		from .check_member_groups import CheckMemberGroupsRequest
		return CheckMemberGroupsRequest(self.request_adapter, path_parameters)

	def check_member_objects(self,
		group_id: str,
	) -> CheckMemberObjectsRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id

		from .check_member_objects import CheckMemberObjectsRequest
		return CheckMemberObjectsRequest(self.request_adapter, path_parameters)

	def get_member_groups(self,
		group_id: str,
	) -> GetMemberGroupsRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id

		from .get_member_groups import GetMemberGroupsRequest
		return GetMemberGroupsRequest(self.request_adapter, path_parameters)

	def get_member_objects(self,
		group_id: str,
	) -> GetMemberObjectsRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id

		from .get_member_objects import GetMemberObjectsRequest
		return GetMemberObjectsRequest(self.request_adapter, path_parameters)

	def remove_favorite(self,
		group_id: str,
	) -> RemoveFavoriteRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id

		from .remove_favorite import RemoveFavoriteRequest
		return RemoveFavoriteRequest(self.request_adapter, path_parameters)

	def renew(self,
		group_id: str,
	) -> RenewRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id

		from .renew import RenewRequest
		return RenewRequest(self.request_adapter, path_parameters)

	def reset_unseen_count(self,
		group_id: str,
	) -> ResetUnseenCountRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id

		from .reset_unseen_count import ResetUnseenCountRequest
		return ResetUnseenCountRequest(self.request_adapter, path_parameters)

	def restore(self,
		group_id: str,
	) -> RestoreRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id

		from .restore import RestoreRequest
		return RestoreRequest(self.request_adapter, path_parameters)

	def retry_service_provisioning(self,
		group_id: str,
	) -> RetryServiceProvisioningRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id

		from .retry_service_provisioning import RetryServiceProvisioningRequest
		return RetryServiceProvisioningRequest(self.request_adapter, path_parameters)

	def subscribe_by_mail(self,
		group_id: str,
	) -> SubscribeByMailRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id

		from .subscribe_by_mail import SubscribeByMailRequest
		return SubscribeByMailRequest(self.request_adapter, path_parameters)

	def unsubscribe_by_mail(self,
		group_id: str,
	) -> UnsubscribeByMailRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id

		from .unsubscribe_by_mail import UnsubscribeByMailRequest
		return UnsubscribeByMailRequest(self.request_adapter, path_parameters)

	def validate_properties(self,
		group_id: str,
	) -> ValidatePropertiesRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id

		from .validate_properties import ValidatePropertiesRequest
		return ValidatePropertiesRequest(self.request_adapter, path_parameters)

	def onenote(self,
		group_id: str,
	) -> OnenoteRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id

		from .onenote import OnenoteRequest
		return OnenoteRequest(self.request_adapter, path_parameters)

	def owners(self,
		group_id: str,
	) -> OwnersRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id

		from .owners import OwnersRequest
		return OwnersRequest(self.request_adapter, path_parameters)

	def permission_grants(self,
		group_id: str,
	) -> PermissionGrantsRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id

		from .permission_grants import PermissionGrantsRequest
		return PermissionGrantsRequest(self.request_adapter, path_parameters)

	def photo(self,
		group_id: str,
	) -> PhotoRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id

		from .photo import PhotoRequest
		return PhotoRequest(self.request_adapter, path_parameters)

	def photos(self,
		group_id: str,
	) -> PhotosRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id

		from .photos import PhotosRequest
		return PhotosRequest(self.request_adapter, path_parameters)

	def planner(self,
		group_id: str,
	) -> PlannerRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id

		from .planner import PlannerRequest
		return PlannerRequest(self.request_adapter, path_parameters)

	def rejected_senders(self,
		group_id: str,
	) -> RejectedSendersRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id

		from .rejected_senders import RejectedSendersRequest
		return RejectedSendersRequest(self.request_adapter, path_parameters)

	def service_provisioning_errors(self,
		group_id: str,
	) -> ServiceProvisioningErrorsRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id

		from .service_provisioning_errors import ServiceProvisioningErrorsRequest
		return ServiceProvisioningErrorsRequest(self.request_adapter, path_parameters)

	def settings(self,
		group_id: str,
	) -> SettingsRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id

		from .settings import SettingsRequest
		return SettingsRequest(self.request_adapter, path_parameters)

	def sites(self,
		group_id: str,
	) -> SitesRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id

		from .sites import SitesRequest
		return SitesRequest(self.request_adapter, path_parameters)

	def team(self,
		group_id: str,
	) -> TeamRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id

		from .team import TeamRequest
		return TeamRequest(self.request_adapter, path_parameters)

	def threads(self,
		group_id: str,
	) -> ThreadsRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id

		from .threads import ThreadsRequest
		return ThreadsRequest(self.request_adapter, path_parameters)

	def transitive_member_of(self,
		group_id: str,
	) -> TransitiveMemberOfRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id

		from .transitive_member_of import TransitiveMemberOfRequest
		return TransitiveMemberOfRequest(self.request_adapter, path_parameters)

	def transitive_members(self,
		group_id: str,
	) -> TransitiveMembersRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id

		from .transitive_members import TransitiveMembersRequest
		return TransitiveMembersRequest(self.request_adapter, path_parameters)

