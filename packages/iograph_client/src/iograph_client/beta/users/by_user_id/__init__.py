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
	from .windows_information_protection_device_registrations import WindowsInformationProtectionDeviceRegistrationsRequest
	from .virtual_events import VirtualEventsRequest
	from .usage_rights import UsageRightsRequest
	from .transitive_reports import TransitiveReportsRequest
	from .transitive_member_of import TransitiveMemberOfRequest
	from .todo import TodoRequest
	from .teamwork import TeamworkRequest
	from .sponsors import SponsorsRequest
	from .solutions import SolutionsRequest
	from .settings import SettingsRequest
	from .service_provisioning_errors import ServiceProvisioningErrorsRequest
	from .security import SecurityRequest
	from .scoped_role_member_of import ScopedRoleMemberOfRequest
	from .registered_devices import RegisteredDevicesRequest
	from .profile import ProfileRequest
	from .presence import PresenceRequest
	from .planner import PlannerRequest
	from .photos import PhotosRequest
	from .photo import PhotoRequest
	from .permission_grants import PermissionGrantsRequest
	from .people import PeopleRequest
	from .pending_access_review_instances import PendingAccessReviewInstancesRequest
	from .owned_objects import OwnedObjectsRequest
	from .owned_devices import OwnedDevicesRequest
	from .outlook import OutlookRequest
	from .online_meetings_with_joinweburl import OnlineMeetingsWithJoinWebUrlRequest
	from .online_meetings import OnlineMeetingsRequest
	from .onenote import OnenoteRequest
	from .oauth2_permission_grants import Oauth2PermissionGrantsRequest
	from .notifications import NotificationsRequest
	from .mobile_app_troubleshooting_events import MobileAppTroubleshootingEventsRequest
	from .mobile_app_intent_and_states import MobileAppIntentAndStatesRequest
	from .wipe_managed_app_registrations_by_device_tag import WipeManagedAppRegistrationsByDeviceTagRequest
	from .wipe_managed_app_registrations_by_azure_ad_device_id import WipeManagedAppRegistrationsByAzureAdDeviceIdRequest
	from .wipe_managed_app_registration_by_device_tag import WipeManagedAppRegistrationByDeviceTagRequest
	from .wipe_and_block_managed_apps import WipeAndBlockManagedAppsRequest
	from .unblock_managed_apps import UnblockManagedAppsRequest
	from .translate_exchange_ids import TranslateExchangeIdsRequest
	from .send_mail import SendMailRequest
	from .revoke_sign_in_sessions import RevokeSignInSessionsRequest
	from .retry_service_provisioning import RetryServiceProvisioningRequest
	from .retrieve_managed_devices_with_app_installation_issues import RetrieveManagedDevicesWithAppInstallationIssuesRequest
	from .restore import RestoreRequest
	from .reprocess_license_assignment import ReprocessLicenseAssignmentRequest
	from .remove_all_devices_from_management import RemoveAllDevicesFromManagementRequest
	from .reminder_view_with_startdatetime_enddatetime import ReminderViewWithStartDateTimeEndDateTimeRequest
	from .is_managed_app_user_blocked import IsManagedAppUserBlockedRequest
	from .invalidate_all_refresh_tokens import InvalidateAllRefreshTokensRequest
	from .get_password_single_sign_on_credentials import GetPasswordSingleSignOnCredentialsRequest
	from .get_member_objects import GetMemberObjectsRequest
	from .get_member_groups import GetMemberGroupsRequest
	from .get_managed_devices_with_failed_or_pending_apps import GetManagedDevicesWithFailedOrPendingAppsRequest
	from .get_managed_devices_with_app_failures import GetManagedDevicesWithAppFailuresRequest
	from .get_managed_app_policies import GetManagedAppPoliciesRequest
	from .get_managed_app_diagnostic_statuses import GetManagedAppDiagnosticStatusesRequest
	from .get_mail_tips import GetMailTipsRequest
	from .get_logged_on_managed_devices import GetLoggedOnManagedDevicesRequest
	from .get_effective_device_enrollment_configurations import GetEffectiveDeviceEnrollmentConfigurationsRequest
	from .find_rooms_with_roomlist import FindRoomsWithRoomListRequest
	from .find_rooms import FindRoomsRequest
	from .find_room_lists import FindRoomListsRequest
	from .find_meeting_times import FindMeetingTimesRequest
	from .export_personal_data import ExportPersonalDataRequest
	from .export_device_and_app_management_data_with_skip_top import ExportDeviceAndAppManagementDataWithSkipTopRequest
	from .export_device_and_app_management_data import ExportDeviceAndAppManagementDataRequest
	from .delete_password_single_sign_on_credentials import DeletePasswordSingleSignOnCredentialsRequest
	from .convert_external_to_internal_member_user import ConvertExternalToInternalMemberUserRequest
	from .check_member_objects import CheckMemberObjectsRequest
	from .check_member_groups import CheckMemberGroupsRequest
	from .change_password import ChangePasswordRequest
	from .assign_license import AssignLicenseRequest
	from .messages import MessagesRequest
	from .member_of import MemberOfRequest
	from .manager import ManagerRequest
	from .managed_devices import ManagedDevicesRequest
	from .managed_app_registrations import ManagedAppRegistrationsRequest
	from .managed_app_log_collection_requests import ManagedAppLogCollectionRequestsRequest
	from .mail_folders import MailFoldersRequest
	from .mailbox_settings import MailboxSettingsRequest
	from .license_details import LicenseDetailsRequest
	from .joined_teams import JoinedTeamsRequest
	from .joined_groups import JoinedGroupsRequest
	from .invited_by import InvitedByRequest
	from .insights import InsightsRequest
	from .information_protection import InformationProtectionRequest
	from .inference_classification import InferenceClassificationRequest
	from .followed_sites import FollowedSitesRequest
	from .extensions import ExtensionsRequest
	from .events import EventsRequest
	from .employee_experience import EmployeeExperienceRequest
	from .drives import DrivesRequest
	from .drive import DriveRequest
	from .direct_reports import DirectReportsRequest
	from .devices_with_deviceid import DevicesWithDeviceIdRequest
	from .devices import DevicesRequest
	from .device_management_troubleshooting_events import DeviceManagementTroubleshootingEventsRequest
	from .device_enrollment_configurations import DeviceEnrollmentConfigurationsRequest
	from .created_objects import CreatedObjectsRequest
	from .contacts import ContactsRequest
	from .contact_folders import ContactFoldersRequest
	from .cloud_p_cs import CloudPCsRequest
	from .cloud_clipboard import CloudClipboardRequest
	from .chats import ChatsRequest
	from .calendar_view import CalendarViewRequest
	from .calendars import CalendarsRequest
	from .calendar_groups import CalendarGroupsRequest
	from .calendar import CalendarRequest
	from .authentication import AuthenticationRequest
	from .approvals import ApprovalsRequest
	from .app_role_assignments import AppRoleAssignmentsRequest
	from .app_role_assigned_resources_with_appid import AppRoleAssignedResourcesWithAppIdRequest
	from .app_role_assigned_resources import AppRoleAssignedResourcesRequest
	from .app_consent_requests_for_approval import AppConsentRequestsForApprovalRequest
	from .analytics import AnalyticsRequest
	from .agreement_acceptances import AgreementAcceptancesRequest
	from .activities import ActivitiesRequest
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.user import User


class ByUserIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/users/{user%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> User:
		"""
		Get user
		Retrieve the properties and relationships of user object. This operation returns by default only a subset of the more commonly used properties for each user. These default properties are noted in the Properties section. To get properties that are not returned by default, do a GET operation for the user and specify the properties in a $select OData query option. Because the user resource supports extensions, you can also use the GET operation to get custom properties and extension data in a user instance. Customers through Microsoft Entra ID for customers can also use this API operation to retrieve their details.
		Find more info here: https://learn.microsoft.com/graph/api/user-get?view=graph-rest-beta
		"""
		tags = ['users.user']

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
		return await self.request_adapter.send_async(request_info, User, error_mapping)

	async def patch(
		self,
		body: User,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> User:
		"""
		Update user
		Update the properties of a user object.
		Find more info here: https://learn.microsoft.com/graph/api/user-update?view=graph-rest-beta
		"""
		tags = ['users.user']

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
		return await self.request_adapter.send_async(request_info, User, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete a user
		Delete a user object.   When deleted, user resources, including their mailbox and license assignments, are moved to a temporary container and if the user is restored within 30 days, these objects are restored to them. The user is also restored to any groups they were a member of. After 30 days and if not restored, the user object is permanently deleted and their assigned resources freed. To manage the deleted user object, see deletedItems.
		Find more info here: https://learn.microsoft.com/graph/api/user-delete?view=graph-rest-beta
		"""
		tags = ['users.user']
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



	def with_url(self, raw_url: str) -> ByUserIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByUserIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByUserIdRequest(self.request_adapter, self.path_parameters)

	def activities(self,
		user_id: str,
	) -> ActivitiesRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .activities import ActivitiesRequest
		return ActivitiesRequest(self.request_adapter, path_parameters)

	def agreement_acceptances(self,
		user_id: str,
	) -> AgreementAcceptancesRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .agreement_acceptances import AgreementAcceptancesRequest
		return AgreementAcceptancesRequest(self.request_adapter, path_parameters)

	def analytics(self,
		user_id: str,
	) -> AnalyticsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .analytics import AnalyticsRequest
		return AnalyticsRequest(self.request_adapter, path_parameters)

	def app_consent_requests_for_approval(self,
		user_id: str,
	) -> AppConsentRequestsForApprovalRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .app_consent_requests_for_approval import AppConsentRequestsForApprovalRequest
		return AppConsentRequestsForApprovalRequest(self.request_adapter, path_parameters)

	def app_role_assigned_resources(self,
		user_id: str,
	) -> AppRoleAssignedResourcesRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .app_role_assigned_resources import AppRoleAssignedResourcesRequest
		return AppRoleAssignedResourcesRequest(self.request_adapter, path_parameters)

	def app_role_assigned_resources_with_appid(self,
		user_id: str,
		appId: str,
	) -> AppRoleAssignedResourcesWithAppIdRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if appId is None:
			raise TypeError("appId cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["appId"] =  appId

		from .app_role_assigned_resources_with_appid import AppRoleAssignedResourcesWithAppIdRequest
		return AppRoleAssignedResourcesWithAppIdRequest(self.request_adapter, path_parameters)

	def app_role_assignments(self,
		user_id: str,
	) -> AppRoleAssignmentsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .app_role_assignments import AppRoleAssignmentsRequest
		return AppRoleAssignmentsRequest(self.request_adapter, path_parameters)

	def approvals(self,
		user_id: str,
	) -> ApprovalsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .approvals import ApprovalsRequest
		return ApprovalsRequest(self.request_adapter, path_parameters)

	def authentication(self,
		user_id: str,
	) -> AuthenticationRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .authentication import AuthenticationRequest
		return AuthenticationRequest(self.request_adapter, path_parameters)

	def calendar(self,
		user_id: str,
	) -> CalendarRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .calendar import CalendarRequest
		return CalendarRequest(self.request_adapter, path_parameters)

	def calendar_groups(self,
		user_id: str,
	) -> CalendarGroupsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .calendar_groups import CalendarGroupsRequest
		return CalendarGroupsRequest(self.request_adapter, path_parameters)

	def calendars(self,
		user_id: str,
	) -> CalendarsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .calendars import CalendarsRequest
		return CalendarsRequest(self.request_adapter, path_parameters)

	def calendar_view(self,
		user_id: str,
	) -> CalendarViewRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .calendar_view import CalendarViewRequest
		return CalendarViewRequest(self.request_adapter, path_parameters)

	def chats(self,
		user_id: str,
	) -> ChatsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .chats import ChatsRequest
		return ChatsRequest(self.request_adapter, path_parameters)

	def cloud_clipboard(self,
		user_id: str,
	) -> CloudClipboardRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .cloud_clipboard import CloudClipboardRequest
		return CloudClipboardRequest(self.request_adapter, path_parameters)

	def cloud_p_cs(self,
		user_id: str,
	) -> CloudPCsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .cloud_p_cs import CloudPCsRequest
		return CloudPCsRequest(self.request_adapter, path_parameters)

	def contact_folders(self,
		user_id: str,
	) -> ContactFoldersRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .contact_folders import ContactFoldersRequest
		return ContactFoldersRequest(self.request_adapter, path_parameters)

	def contacts(self,
		user_id: str,
	) -> ContactsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .contacts import ContactsRequest
		return ContactsRequest(self.request_adapter, path_parameters)

	def created_objects(self,
		user_id: str,
	) -> CreatedObjectsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .created_objects import CreatedObjectsRequest
		return CreatedObjectsRequest(self.request_adapter, path_parameters)

	def device_enrollment_configurations(self,
		user_id: str,
	) -> DeviceEnrollmentConfigurationsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .device_enrollment_configurations import DeviceEnrollmentConfigurationsRequest
		return DeviceEnrollmentConfigurationsRequest(self.request_adapter, path_parameters)

	def device_management_troubleshooting_events(self,
		user_id: str,
	) -> DeviceManagementTroubleshootingEventsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .device_management_troubleshooting_events import DeviceManagementTroubleshootingEventsRequest
		return DeviceManagementTroubleshootingEventsRequest(self.request_adapter, path_parameters)

	def devices(self,
		user_id: str,
	) -> DevicesRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .devices import DevicesRequest
		return DevicesRequest(self.request_adapter, path_parameters)

	def devices_with_deviceid(self,
		user_id: str,
		deviceId: str,
	) -> DevicesWithDeviceIdRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if deviceId is None:
			raise TypeError("deviceId cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["deviceId"] =  deviceId

		from .devices_with_deviceid import DevicesWithDeviceIdRequest
		return DevicesWithDeviceIdRequest(self.request_adapter, path_parameters)

	def direct_reports(self,
		user_id: str,
	) -> DirectReportsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .direct_reports import DirectReportsRequest
		return DirectReportsRequest(self.request_adapter, path_parameters)

	def drive(self,
		user_id: str,
	) -> DriveRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .drive import DriveRequest
		return DriveRequest(self.request_adapter, path_parameters)

	def drives(self,
		user_id: str,
	) -> DrivesRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .drives import DrivesRequest
		return DrivesRequest(self.request_adapter, path_parameters)

	def employee_experience(self,
		user_id: str,
	) -> EmployeeExperienceRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .employee_experience import EmployeeExperienceRequest
		return EmployeeExperienceRequest(self.request_adapter, path_parameters)

	def events(self,
		user_id: str,
	) -> EventsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .events import EventsRequest
		return EventsRequest(self.request_adapter, path_parameters)

	def extensions(self,
		user_id: str,
	) -> ExtensionsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .extensions import ExtensionsRequest
		return ExtensionsRequest(self.request_adapter, path_parameters)

	def followed_sites(self,
		user_id: str,
	) -> FollowedSitesRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .followed_sites import FollowedSitesRequest
		return FollowedSitesRequest(self.request_adapter, path_parameters)

	def inference_classification(self,
		user_id: str,
	) -> InferenceClassificationRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .inference_classification import InferenceClassificationRequest
		return InferenceClassificationRequest(self.request_adapter, path_parameters)

	def information_protection(self,
		user_id: str,
	) -> InformationProtectionRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .information_protection import InformationProtectionRequest
		return InformationProtectionRequest(self.request_adapter, path_parameters)

	def insights(self,
		user_id: str,
	) -> InsightsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .insights import InsightsRequest
		return InsightsRequest(self.request_adapter, path_parameters)

	def invited_by(self,
		user_id: str,
	) -> InvitedByRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .invited_by import InvitedByRequest
		return InvitedByRequest(self.request_adapter, path_parameters)

	def joined_groups(self,
		user_id: str,
	) -> JoinedGroupsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .joined_groups import JoinedGroupsRequest
		return JoinedGroupsRequest(self.request_adapter, path_parameters)

	def joined_teams(self,
		user_id: str,
	) -> JoinedTeamsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .joined_teams import JoinedTeamsRequest
		return JoinedTeamsRequest(self.request_adapter, path_parameters)

	def license_details(self,
		user_id: str,
	) -> LicenseDetailsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .license_details import LicenseDetailsRequest
		return LicenseDetailsRequest(self.request_adapter, path_parameters)

	def mailbox_settings(self,
		user_id: str,
	) -> MailboxSettingsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .mailbox_settings import MailboxSettingsRequest
		return MailboxSettingsRequest(self.request_adapter, path_parameters)

	def mail_folders(self,
		user_id: str,
	) -> MailFoldersRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .mail_folders import MailFoldersRequest
		return MailFoldersRequest(self.request_adapter, path_parameters)

	def managed_app_log_collection_requests(self,
		user_id: str,
	) -> ManagedAppLogCollectionRequestsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .managed_app_log_collection_requests import ManagedAppLogCollectionRequestsRequest
		return ManagedAppLogCollectionRequestsRequest(self.request_adapter, path_parameters)

	def managed_app_registrations(self,
		user_id: str,
	) -> ManagedAppRegistrationsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .managed_app_registrations import ManagedAppRegistrationsRequest
		return ManagedAppRegistrationsRequest(self.request_adapter, path_parameters)

	def managed_devices(self,
		user_id: str,
	) -> ManagedDevicesRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .managed_devices import ManagedDevicesRequest
		return ManagedDevicesRequest(self.request_adapter, path_parameters)

	def manager(self,
		user_id: str,
	) -> ManagerRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .manager import ManagerRequest
		return ManagerRequest(self.request_adapter, path_parameters)

	def member_of(self,
		user_id: str,
	) -> MemberOfRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .member_of import MemberOfRequest
		return MemberOfRequest(self.request_adapter, path_parameters)

	def messages(self,
		user_id: str,
	) -> MessagesRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .messages import MessagesRequest
		return MessagesRequest(self.request_adapter, path_parameters)

	def assign_license(self,
		user_id: str,
	) -> AssignLicenseRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .assign_license import AssignLicenseRequest
		return AssignLicenseRequest(self.request_adapter, path_parameters)

	def change_password(self,
		user_id: str,
	) -> ChangePasswordRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .change_password import ChangePasswordRequest
		return ChangePasswordRequest(self.request_adapter, path_parameters)

	def check_member_groups(self,
		user_id: str,
	) -> CheckMemberGroupsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .check_member_groups import CheckMemberGroupsRequest
		return CheckMemberGroupsRequest(self.request_adapter, path_parameters)

	def check_member_objects(self,
		user_id: str,
	) -> CheckMemberObjectsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .check_member_objects import CheckMemberObjectsRequest
		return CheckMemberObjectsRequest(self.request_adapter, path_parameters)

	def convert_external_to_internal_member_user(self,
		user_id: str,
	) -> ConvertExternalToInternalMemberUserRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .convert_external_to_internal_member_user import ConvertExternalToInternalMemberUserRequest
		return ConvertExternalToInternalMemberUserRequest(self.request_adapter, path_parameters)

	def delete_password_single_sign_on_credentials(self,
		user_id: str,
	) -> DeletePasswordSingleSignOnCredentialsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .delete_password_single_sign_on_credentials import DeletePasswordSingleSignOnCredentialsRequest
		return DeletePasswordSingleSignOnCredentialsRequest(self.request_adapter, path_parameters)

	def export_device_and_app_management_data(self,
		user_id: str,
	) -> ExportDeviceAndAppManagementDataRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .export_device_and_app_management_data import ExportDeviceAndAppManagementDataRequest
		return ExportDeviceAndAppManagementDataRequest(self.request_adapter, path_parameters)

	def export_device_and_app_management_data_with_skip_top(self,
		user_id: str,
		skip: int,
		top: int,
	) -> ExportDeviceAndAppManagementDataWithSkipTopRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if skip is None:
			raise TypeError("skip cannot be null.")
		if top is None:
			raise TypeError("top cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["skip"] =  skip
		path_parameters["top"] =  top

		from .export_device_and_app_management_data_with_skip_top import ExportDeviceAndAppManagementDataWithSkipTopRequest
		return ExportDeviceAndAppManagementDataWithSkipTopRequest(self.request_adapter, path_parameters)

	def export_personal_data(self,
		user_id: str,
	) -> ExportPersonalDataRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .export_personal_data import ExportPersonalDataRequest
		return ExportPersonalDataRequest(self.request_adapter, path_parameters)

	def find_meeting_times(self,
		user_id: str,
	) -> FindMeetingTimesRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .find_meeting_times import FindMeetingTimesRequest
		return FindMeetingTimesRequest(self.request_adapter, path_parameters)

	def find_room_lists(self,
		user_id: str,
	) -> FindRoomListsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .find_room_lists import FindRoomListsRequest
		return FindRoomListsRequest(self.request_adapter, path_parameters)

	def find_rooms(self,
		user_id: str,
	) -> FindRoomsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .find_rooms import FindRoomsRequest
		return FindRoomsRequest(self.request_adapter, path_parameters)

	def find_rooms_with_roomlist(self,
		user_id: str,
		RoomList: str,
	) -> FindRoomsWithRoomListRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if RoomList is None:
			raise TypeError("RoomList cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["RoomList"] =  RoomList

		from .find_rooms_with_roomlist import FindRoomsWithRoomListRequest
		return FindRoomsWithRoomListRequest(self.request_adapter, path_parameters)

	def get_effective_device_enrollment_configurations(self,
		user_id: str,
	) -> GetEffectiveDeviceEnrollmentConfigurationsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .get_effective_device_enrollment_configurations import GetEffectiveDeviceEnrollmentConfigurationsRequest
		return GetEffectiveDeviceEnrollmentConfigurationsRequest(self.request_adapter, path_parameters)

	def get_logged_on_managed_devices(self,
		user_id: str,
	) -> GetLoggedOnManagedDevicesRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .get_logged_on_managed_devices import GetLoggedOnManagedDevicesRequest
		return GetLoggedOnManagedDevicesRequest(self.request_adapter, path_parameters)

	def get_mail_tips(self,
		user_id: str,
	) -> GetMailTipsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .get_mail_tips import GetMailTipsRequest
		return GetMailTipsRequest(self.request_adapter, path_parameters)

	def get_managed_app_diagnostic_statuses(self,
		user_id: str,
	) -> GetManagedAppDiagnosticStatusesRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .get_managed_app_diagnostic_statuses import GetManagedAppDiagnosticStatusesRequest
		return GetManagedAppDiagnosticStatusesRequest(self.request_adapter, path_parameters)

	def get_managed_app_policies(self,
		user_id: str,
	) -> GetManagedAppPoliciesRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .get_managed_app_policies import GetManagedAppPoliciesRequest
		return GetManagedAppPoliciesRequest(self.request_adapter, path_parameters)

	def get_managed_devices_with_app_failures(self,
		user_id: str,
	) -> GetManagedDevicesWithAppFailuresRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .get_managed_devices_with_app_failures import GetManagedDevicesWithAppFailuresRequest
		return GetManagedDevicesWithAppFailuresRequest(self.request_adapter, path_parameters)

	def get_managed_devices_with_failed_or_pending_apps(self,
		user_id: str,
	) -> GetManagedDevicesWithFailedOrPendingAppsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .get_managed_devices_with_failed_or_pending_apps import GetManagedDevicesWithFailedOrPendingAppsRequest
		return GetManagedDevicesWithFailedOrPendingAppsRequest(self.request_adapter, path_parameters)

	def get_member_groups(self,
		user_id: str,
	) -> GetMemberGroupsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .get_member_groups import GetMemberGroupsRequest
		return GetMemberGroupsRequest(self.request_adapter, path_parameters)

	def get_member_objects(self,
		user_id: str,
	) -> GetMemberObjectsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .get_member_objects import GetMemberObjectsRequest
		return GetMemberObjectsRequest(self.request_adapter, path_parameters)

	def get_password_single_sign_on_credentials(self,
		user_id: str,
	) -> GetPasswordSingleSignOnCredentialsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .get_password_single_sign_on_credentials import GetPasswordSingleSignOnCredentialsRequest
		return GetPasswordSingleSignOnCredentialsRequest(self.request_adapter, path_parameters)

	def invalidate_all_refresh_tokens(self,
		user_id: str,
	) -> InvalidateAllRefreshTokensRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .invalidate_all_refresh_tokens import InvalidateAllRefreshTokensRequest
		return InvalidateAllRefreshTokensRequest(self.request_adapter, path_parameters)

	def is_managed_app_user_blocked(self,
		user_id: str,
	) -> IsManagedAppUserBlockedRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .is_managed_app_user_blocked import IsManagedAppUserBlockedRequest
		return IsManagedAppUserBlockedRequest(self.request_adapter, path_parameters)

	def reminder_view_with_startdatetime_enddatetime(self,
		user_id: str,
		StartDateTime: str,
		EndDateTime: str,
	) -> ReminderViewWithStartDateTimeEndDateTimeRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if StartDateTime is None:
			raise TypeError("StartDateTime cannot be null.")
		if EndDateTime is None:
			raise TypeError("EndDateTime cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["StartDateTime"] =  StartDateTime
		path_parameters["EndDateTime"] =  EndDateTime

		from .reminder_view_with_startdatetime_enddatetime import ReminderViewWithStartDateTimeEndDateTimeRequest
		return ReminderViewWithStartDateTimeEndDateTimeRequest(self.request_adapter, path_parameters)

	def remove_all_devices_from_management(self,
		user_id: str,
	) -> RemoveAllDevicesFromManagementRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .remove_all_devices_from_management import RemoveAllDevicesFromManagementRequest
		return RemoveAllDevicesFromManagementRequest(self.request_adapter, path_parameters)

	def reprocess_license_assignment(self,
		user_id: str,
	) -> ReprocessLicenseAssignmentRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .reprocess_license_assignment import ReprocessLicenseAssignmentRequest
		return ReprocessLicenseAssignmentRequest(self.request_adapter, path_parameters)

	def restore(self,
		user_id: str,
	) -> RestoreRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .restore import RestoreRequest
		return RestoreRequest(self.request_adapter, path_parameters)

	def retrieve_managed_devices_with_app_installation_issues(self,
		user_id: str,
	) -> RetrieveManagedDevicesWithAppInstallationIssuesRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .retrieve_managed_devices_with_app_installation_issues import RetrieveManagedDevicesWithAppInstallationIssuesRequest
		return RetrieveManagedDevicesWithAppInstallationIssuesRequest(self.request_adapter, path_parameters)

	def retry_service_provisioning(self,
		user_id: str,
	) -> RetryServiceProvisioningRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .retry_service_provisioning import RetryServiceProvisioningRequest
		return RetryServiceProvisioningRequest(self.request_adapter, path_parameters)

	def revoke_sign_in_sessions(self,
		user_id: str,
	) -> RevokeSignInSessionsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .revoke_sign_in_sessions import RevokeSignInSessionsRequest
		return RevokeSignInSessionsRequest(self.request_adapter, path_parameters)

	def send_mail(self,
		user_id: str,
	) -> SendMailRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .send_mail import SendMailRequest
		return SendMailRequest(self.request_adapter, path_parameters)

	def translate_exchange_ids(self,
		user_id: str,
	) -> TranslateExchangeIdsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .translate_exchange_ids import TranslateExchangeIdsRequest
		return TranslateExchangeIdsRequest(self.request_adapter, path_parameters)

	def unblock_managed_apps(self,
		user_id: str,
	) -> UnblockManagedAppsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .unblock_managed_apps import UnblockManagedAppsRequest
		return UnblockManagedAppsRequest(self.request_adapter, path_parameters)

	def wipe_and_block_managed_apps(self,
		user_id: str,
	) -> WipeAndBlockManagedAppsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .wipe_and_block_managed_apps import WipeAndBlockManagedAppsRequest
		return WipeAndBlockManagedAppsRequest(self.request_adapter, path_parameters)

	def wipe_managed_app_registration_by_device_tag(self,
		user_id: str,
	) -> WipeManagedAppRegistrationByDeviceTagRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .wipe_managed_app_registration_by_device_tag import WipeManagedAppRegistrationByDeviceTagRequest
		return WipeManagedAppRegistrationByDeviceTagRequest(self.request_adapter, path_parameters)

	def wipe_managed_app_registrations_by_azure_ad_device_id(self,
		user_id: str,
	) -> WipeManagedAppRegistrationsByAzureAdDeviceIdRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .wipe_managed_app_registrations_by_azure_ad_device_id import WipeManagedAppRegistrationsByAzureAdDeviceIdRequest
		return WipeManagedAppRegistrationsByAzureAdDeviceIdRequest(self.request_adapter, path_parameters)

	def wipe_managed_app_registrations_by_device_tag(self,
		user_id: str,
	) -> WipeManagedAppRegistrationsByDeviceTagRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .wipe_managed_app_registrations_by_device_tag import WipeManagedAppRegistrationsByDeviceTagRequest
		return WipeManagedAppRegistrationsByDeviceTagRequest(self.request_adapter, path_parameters)

	def mobile_app_intent_and_states(self,
		user_id: str,
	) -> MobileAppIntentAndStatesRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .mobile_app_intent_and_states import MobileAppIntentAndStatesRequest
		return MobileAppIntentAndStatesRequest(self.request_adapter, path_parameters)

	def mobile_app_troubleshooting_events(self,
		user_id: str,
	) -> MobileAppTroubleshootingEventsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .mobile_app_troubleshooting_events import MobileAppTroubleshootingEventsRequest
		return MobileAppTroubleshootingEventsRequest(self.request_adapter, path_parameters)

	def notifications(self,
		user_id: str,
	) -> NotificationsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .notifications import NotificationsRequest
		return NotificationsRequest(self.request_adapter, path_parameters)

	def oauth2_permission_grants(self,
		user_id: str,
	) -> Oauth2PermissionGrantsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .oauth2_permission_grants import Oauth2PermissionGrantsRequest
		return Oauth2PermissionGrantsRequest(self.request_adapter, path_parameters)

	def onenote(self,
		user_id: str,
	) -> OnenoteRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .onenote import OnenoteRequest
		return OnenoteRequest(self.request_adapter, path_parameters)

	def online_meetings(self,
		user_id: str,
	) -> OnlineMeetingsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .online_meetings import OnlineMeetingsRequest
		return OnlineMeetingsRequest(self.request_adapter, path_parameters)

	def online_meetings_with_joinweburl(self,
		user_id: str,
		joinWebUrl: str,
	) -> OnlineMeetingsWithJoinWebUrlRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if joinWebUrl is None:
			raise TypeError("joinWebUrl cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["joinWebUrl"] =  joinWebUrl

		from .online_meetings_with_joinweburl import OnlineMeetingsWithJoinWebUrlRequest
		return OnlineMeetingsWithJoinWebUrlRequest(self.request_adapter, path_parameters)

	def outlook(self,
		user_id: str,
	) -> OutlookRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .outlook import OutlookRequest
		return OutlookRequest(self.request_adapter, path_parameters)

	def owned_devices(self,
		user_id: str,
	) -> OwnedDevicesRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .owned_devices import OwnedDevicesRequest
		return OwnedDevicesRequest(self.request_adapter, path_parameters)

	def owned_objects(self,
		user_id: str,
	) -> OwnedObjectsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .owned_objects import OwnedObjectsRequest
		return OwnedObjectsRequest(self.request_adapter, path_parameters)

	def pending_access_review_instances(self,
		user_id: str,
	) -> PendingAccessReviewInstancesRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .pending_access_review_instances import PendingAccessReviewInstancesRequest
		return PendingAccessReviewInstancesRequest(self.request_adapter, path_parameters)

	def people(self,
		user_id: str,
	) -> PeopleRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .people import PeopleRequest
		return PeopleRequest(self.request_adapter, path_parameters)

	def permission_grants(self,
		user_id: str,
	) -> PermissionGrantsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .permission_grants import PermissionGrantsRequest
		return PermissionGrantsRequest(self.request_adapter, path_parameters)

	def photo(self,
		user_id: str,
	) -> PhotoRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .photo import PhotoRequest
		return PhotoRequest(self.request_adapter, path_parameters)

	def photos(self,
		user_id: str,
	) -> PhotosRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .photos import PhotosRequest
		return PhotosRequest(self.request_adapter, path_parameters)

	def planner(self,
		user_id: str,
	) -> PlannerRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .planner import PlannerRequest
		return PlannerRequest(self.request_adapter, path_parameters)

	def presence(self,
		user_id: str,
	) -> PresenceRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .presence import PresenceRequest
		return PresenceRequest(self.request_adapter, path_parameters)

	def profile(self,
		user_id: str,
	) -> ProfileRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .profile import ProfileRequest
		return ProfileRequest(self.request_adapter, path_parameters)

	def registered_devices(self,
		user_id: str,
	) -> RegisteredDevicesRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .registered_devices import RegisteredDevicesRequest
		return RegisteredDevicesRequest(self.request_adapter, path_parameters)

	def scoped_role_member_of(self,
		user_id: str,
	) -> ScopedRoleMemberOfRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .scoped_role_member_of import ScopedRoleMemberOfRequest
		return ScopedRoleMemberOfRequest(self.request_adapter, path_parameters)

	def security(self,
		user_id: str,
	) -> SecurityRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .security import SecurityRequest
		return SecurityRequest(self.request_adapter, path_parameters)

	def service_provisioning_errors(self,
		user_id: str,
	) -> ServiceProvisioningErrorsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .service_provisioning_errors import ServiceProvisioningErrorsRequest
		return ServiceProvisioningErrorsRequest(self.request_adapter, path_parameters)

	def settings(self,
		user_id: str,
	) -> SettingsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .settings import SettingsRequest
		return SettingsRequest(self.request_adapter, path_parameters)

	def solutions(self,
		user_id: str,
	) -> SolutionsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .solutions import SolutionsRequest
		return SolutionsRequest(self.request_adapter, path_parameters)

	def sponsors(self,
		user_id: str,
	) -> SponsorsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .sponsors import SponsorsRequest
		return SponsorsRequest(self.request_adapter, path_parameters)

	def teamwork(self,
		user_id: str,
	) -> TeamworkRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .teamwork import TeamworkRequest
		return TeamworkRequest(self.request_adapter, path_parameters)

	def todo(self,
		user_id: str,
	) -> TodoRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .todo import TodoRequest
		return TodoRequest(self.request_adapter, path_parameters)

	def transitive_member_of(self,
		user_id: str,
	) -> TransitiveMemberOfRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .transitive_member_of import TransitiveMemberOfRequest
		return TransitiveMemberOfRequest(self.request_adapter, path_parameters)

	def transitive_reports(self,
		user_id: str,
	) -> TransitiveReportsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .transitive_reports import TransitiveReportsRequest
		return TransitiveReportsRequest(self.request_adapter, path_parameters)

	def usage_rights(self,
		user_id: str,
	) -> UsageRightsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .usage_rights import UsageRightsRequest
		return UsageRightsRequest(self.request_adapter, path_parameters)

	def virtual_events(self,
		user_id: str,
	) -> VirtualEventsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .virtual_events import VirtualEventsRequest
		return VirtualEventsRequest(self.request_adapter, path_parameters)

	def windows_information_protection_device_registrations(self,
		user_id: str,
	) -> WindowsInformationProtectionDeviceRegistrationsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .windows_information_protection_device_registrations import WindowsInformationProtectionDeviceRegistrationsRequest
		return WindowsInformationProtectionDeviceRegistrationsRequest(self.request_adapter, path_parameters)

