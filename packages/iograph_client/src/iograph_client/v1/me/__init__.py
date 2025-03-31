# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ...request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .transitive_member_of import TransitiveMemberOfRequest
	from .todo import TodoRequest
	from .teamwork import TeamworkRequest
	from .sponsors import SponsorsRequest
	from .solutions import SolutionsRequest
	from .settings import SettingsRequest
	from .service_provisioning_errors import ServiceProvisioningErrorsRequest
	from .scoped_role_member_of import ScopedRoleMemberOfRequest
	from .registered_devices import RegisteredDevicesRequest
	from .presence import PresenceRequest
	from .planner import PlannerRequest
	from .photos import PhotosRequest
	from .photo import PhotoRequest
	from .permission_grants import PermissionGrantsRequest
	from .people import PeopleRequest
	from .owned_objects import OwnedObjectsRequest
	from .owned_devices import OwnedDevicesRequest
	from .outlook import OutlookRequest
	from .online_meetings import OnlineMeetingsRequest
	from .onenote import OnenoteRequest
	from .oauth2_permission_grants import Oauth2PermissionGrantsRequest
	from .wipe_managed_app_registrations_by_device_tag import WipeManagedAppRegistrationsByDeviceTagRequest
	from .translate_exchange_ids import TranslateExchangeIdsRequest
	from .send_mail import SendMailRequest
	from .revoke_sign_in_sessions import RevokeSignInSessionsRequest
	from .retry_service_provisioning import RetryServiceProvisioningRequest
	from .restore import RestoreRequest
	from .reprocess_license_assignment import ReprocessLicenseAssignmentRequest
	from .remove_all_devices_from_management import RemoveAllDevicesFromManagementRequest
	from .reminder_view_with_startdatetime_enddatetime import ReminderViewWithStartDateTimeEndDateTimeRequest
	from .get_member_objects import GetMemberObjectsRequest
	from .get_member_groups import GetMemberGroupsRequest
	from .get_managed_devices_with_app_failures import GetManagedDevicesWithAppFailuresRequest
	from .get_managed_app_policies import GetManagedAppPoliciesRequest
	from .get_managed_app_diagnostic_statuses import GetManagedAppDiagnosticStatusesRequest
	from .get_mail_tips import GetMailTipsRequest
	from .find_meeting_times import FindMeetingTimesRequest
	from .export_personal_data import ExportPersonalDataRequest
	from .export_device_and_app_management_data_with_skip_top import ExportDeviceAndAppManagementDataWithSkipTopRequest
	from .export_device_and_app_management_data import ExportDeviceAndAppManagementDataRequest
	from .check_member_objects import CheckMemberObjectsRequest
	from .check_member_groups import CheckMemberGroupsRequest
	from .change_password import ChangePasswordRequest
	from .assign_license import AssignLicenseRequest
	from .messages import MessagesRequest
	from .member_of import MemberOfRequest
	from .manager import ManagerRequest
	from .managed_devices import ManagedDevicesRequest
	from .managed_app_registrations import ManagedAppRegistrationsRequest
	from .mail_folders import MailFoldersRequest
	from .mailbox_settings import MailboxSettingsRequest
	from .license_details import LicenseDetailsRequest
	from .joined_teams import JoinedTeamsRequest
	from .insights import InsightsRequest
	from .inference_classification import InferenceClassificationRequest
	from .followed_sites import FollowedSitesRequest
	from .extensions import ExtensionsRequest
	from .events import EventsRequest
	from .employee_experience import EmployeeExperienceRequest
	from .drives import DrivesRequest
	from .drive import DriveRequest
	from .direct_reports import DirectReportsRequest
	from .device_management_troubleshooting_events import DeviceManagementTroubleshootingEventsRequest
	from .created_objects import CreatedObjectsRequest
	from .contacts import ContactsRequest
	from .contact_folders import ContactFoldersRequest
	from .cloud_clipboard import CloudClipboardRequest
	from .chats import ChatsRequest
	from .calendar_view import CalendarViewRequest
	from .calendars import CalendarsRequest
	from .calendar_groups import CalendarGroupsRequest
	from .calendar import CalendarRequest
	from .authentication import AuthenticationRequest
	from .app_role_assignments import AppRoleAssignmentsRequest
	from .agreement_acceptances import AgreementAcceptancesRequest
	from .activities import ActivitiesRequest
	from ...request_adapter import HttpxRequestAdapter
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.v1.user import User


class MeRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/me", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> User:
		"""
		List manager
		Returns the user or organizational contact assigned as the user's manager. Optionally, you can expand the manager's chain up to the root node.
		Find more info here: https://learn.microsoft.com/graph/api/user-list-manager?view=graph-rest-1.0
		"""
		tags = ['me.user']
		header_parameters = [{'name': 'ConsistencyLevel', 'in': 'header', 'description': 'Indicates the requested consistency level. Documentation URL: https://docs.microsoft.com/graph/aad-advanced-queries', 'schema': {'type': 'string'}, 'examples': {'example-1': {'description': "$search and $count queries require the client to set the ConsistencyLevel HTTP header to 'eventual'.", 'value': 'eventual'}}}]

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
		Find more info here: https://learn.microsoft.com/graph/api/user-update?view=graph-rest-1.0
		"""
		tags = ['me.user']

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

	class GetQueryParams(BaseModel):
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> MeRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: MeRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return MeRequest(self.request_adapter, self.path_parameters)

	@property
	def activities(self,
	) -> ActivitiesRequest:
		from .activities import ActivitiesRequest
		return ActivitiesRequest(self.request_adapter, self.path_parameters)

	@property
	def agreement_acceptances(self,
	) -> AgreementAcceptancesRequest:
		from .agreement_acceptances import AgreementAcceptancesRequest
		return AgreementAcceptancesRequest(self.request_adapter, self.path_parameters)

	@property
	def app_role_assignments(self,
	) -> AppRoleAssignmentsRequest:
		from .app_role_assignments import AppRoleAssignmentsRequest
		return AppRoleAssignmentsRequest(self.request_adapter, self.path_parameters)

	@property
	def authentication(self,
	) -> AuthenticationRequest:
		from .authentication import AuthenticationRequest
		return AuthenticationRequest(self.request_adapter, self.path_parameters)

	@property
	def calendar(self,
	) -> CalendarRequest:
		from .calendar import CalendarRequest
		return CalendarRequest(self.request_adapter, self.path_parameters)

	@property
	def calendar_groups(self,
	) -> CalendarGroupsRequest:
		from .calendar_groups import CalendarGroupsRequest
		return CalendarGroupsRequest(self.request_adapter, self.path_parameters)

	@property
	def calendars(self,
	) -> CalendarsRequest:
		from .calendars import CalendarsRequest
		return CalendarsRequest(self.request_adapter, self.path_parameters)

	@property
	def calendar_view(self,
	) -> CalendarViewRequest:
		from .calendar_view import CalendarViewRequest
		return CalendarViewRequest(self.request_adapter, self.path_parameters)

	@property
	def chats(self,
	) -> ChatsRequest:
		from .chats import ChatsRequest
		return ChatsRequest(self.request_adapter, self.path_parameters)

	@property
	def cloud_clipboard(self,
	) -> CloudClipboardRequest:
		from .cloud_clipboard import CloudClipboardRequest
		return CloudClipboardRequest(self.request_adapter, self.path_parameters)

	@property
	def contact_folders(self,
	) -> ContactFoldersRequest:
		from .contact_folders import ContactFoldersRequest
		return ContactFoldersRequest(self.request_adapter, self.path_parameters)

	@property
	def contacts(self,
	) -> ContactsRequest:
		from .contacts import ContactsRequest
		return ContactsRequest(self.request_adapter, self.path_parameters)

	@property
	def created_objects(self,
	) -> CreatedObjectsRequest:
		from .created_objects import CreatedObjectsRequest
		return CreatedObjectsRequest(self.request_adapter, self.path_parameters)

	@property
	def device_management_troubleshooting_events(self,
	) -> DeviceManagementTroubleshootingEventsRequest:
		from .device_management_troubleshooting_events import DeviceManagementTroubleshootingEventsRequest
		return DeviceManagementTroubleshootingEventsRequest(self.request_adapter, self.path_parameters)

	@property
	def direct_reports(self,
	) -> DirectReportsRequest:
		from .direct_reports import DirectReportsRequest
		return DirectReportsRequest(self.request_adapter, self.path_parameters)

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
	def employee_experience(self,
	) -> EmployeeExperienceRequest:
		from .employee_experience import EmployeeExperienceRequest
		return EmployeeExperienceRequest(self.request_adapter, self.path_parameters)

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
	def followed_sites(self,
	) -> FollowedSitesRequest:
		from .followed_sites import FollowedSitesRequest
		return FollowedSitesRequest(self.request_adapter, self.path_parameters)

	@property
	def inference_classification(self,
	) -> InferenceClassificationRequest:
		from .inference_classification import InferenceClassificationRequest
		return InferenceClassificationRequest(self.request_adapter, self.path_parameters)

	@property
	def insights(self,
	) -> InsightsRequest:
		from .insights import InsightsRequest
		return InsightsRequest(self.request_adapter, self.path_parameters)

	@property
	def joined_teams(self,
	) -> JoinedTeamsRequest:
		from .joined_teams import JoinedTeamsRequest
		return JoinedTeamsRequest(self.request_adapter, self.path_parameters)

	@property
	def license_details(self,
	) -> LicenseDetailsRequest:
		from .license_details import LicenseDetailsRequest
		return LicenseDetailsRequest(self.request_adapter, self.path_parameters)

	@property
	def mailbox_settings(self,
	) -> MailboxSettingsRequest:
		from .mailbox_settings import MailboxSettingsRequest
		return MailboxSettingsRequest(self.request_adapter, self.path_parameters)

	@property
	def mail_folders(self,
	) -> MailFoldersRequest:
		from .mail_folders import MailFoldersRequest
		return MailFoldersRequest(self.request_adapter, self.path_parameters)

	@property
	def managed_app_registrations(self,
	) -> ManagedAppRegistrationsRequest:
		from .managed_app_registrations import ManagedAppRegistrationsRequest
		return ManagedAppRegistrationsRequest(self.request_adapter, self.path_parameters)

	@property
	def managed_devices(self,
	) -> ManagedDevicesRequest:
		from .managed_devices import ManagedDevicesRequest
		return ManagedDevicesRequest(self.request_adapter, self.path_parameters)

	@property
	def manager(self,
	) -> ManagerRequest:
		from .manager import ManagerRequest
		return ManagerRequest(self.request_adapter, self.path_parameters)

	@property
	def member_of(self,
	) -> MemberOfRequest:
		from .member_of import MemberOfRequest
		return MemberOfRequest(self.request_adapter, self.path_parameters)

	@property
	def messages(self,
	) -> MessagesRequest:
		from .messages import MessagesRequest
		return MessagesRequest(self.request_adapter, self.path_parameters)

	@property
	def assign_license(self,
	) -> AssignLicenseRequest:
		from .assign_license import AssignLicenseRequest
		return AssignLicenseRequest(self.request_adapter, self.path_parameters)

	@property
	def change_password(self,
	) -> ChangePasswordRequest:
		from .change_password import ChangePasswordRequest
		return ChangePasswordRequest(self.request_adapter, self.path_parameters)

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
	def export_device_and_app_management_data(self,
	) -> ExportDeviceAndAppManagementDataRequest:
		from .export_device_and_app_management_data import ExportDeviceAndAppManagementDataRequest
		return ExportDeviceAndAppManagementDataRequest(self.request_adapter, self.path_parameters)

	def export_device_and_app_management_data_with_skip_top(self,
		skip: int,
		top: int,
	) -> ExportDeviceAndAppManagementDataWithSkipTopRequest:
		if skip is None:
			raise TypeError("skip cannot be null.")
		if top is None:
			raise TypeError("top cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["skip"] =  skip
		path_parameters["top"] =  top

		from .export_device_and_app_management_data_with_skip_top import ExportDeviceAndAppManagementDataWithSkipTopRequest
		return ExportDeviceAndAppManagementDataWithSkipTopRequest(self.request_adapter, path_parameters)

	@property
	def export_personal_data(self,
	) -> ExportPersonalDataRequest:
		from .export_personal_data import ExportPersonalDataRequest
		return ExportPersonalDataRequest(self.request_adapter, self.path_parameters)

	@property
	def find_meeting_times(self,
	) -> FindMeetingTimesRequest:
		from .find_meeting_times import FindMeetingTimesRequest
		return FindMeetingTimesRequest(self.request_adapter, self.path_parameters)

	@property
	def get_mail_tips(self,
	) -> GetMailTipsRequest:
		from .get_mail_tips import GetMailTipsRequest
		return GetMailTipsRequest(self.request_adapter, self.path_parameters)

	@property
	def get_managed_app_diagnostic_statuses(self,
	) -> GetManagedAppDiagnosticStatusesRequest:
		from .get_managed_app_diagnostic_statuses import GetManagedAppDiagnosticStatusesRequest
		return GetManagedAppDiagnosticStatusesRequest(self.request_adapter, self.path_parameters)

	@property
	def get_managed_app_policies(self,
	) -> GetManagedAppPoliciesRequest:
		from .get_managed_app_policies import GetManagedAppPoliciesRequest
		return GetManagedAppPoliciesRequest(self.request_adapter, self.path_parameters)

	@property
	def get_managed_devices_with_app_failures(self,
	) -> GetManagedDevicesWithAppFailuresRequest:
		from .get_managed_devices_with_app_failures import GetManagedDevicesWithAppFailuresRequest
		return GetManagedDevicesWithAppFailuresRequest(self.request_adapter, self.path_parameters)

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

	def reminder_view_with_startdatetime_enddatetime(self,
		StartDateTime: str,
		EndDateTime: str,
	) -> ReminderViewWithStartDateTimeEndDateTimeRequest:
		if StartDateTime is None:
			raise TypeError("StartDateTime cannot be null.")
		if EndDateTime is None:
			raise TypeError("EndDateTime cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["StartDateTime"] =  StartDateTime
		path_parameters["EndDateTime"] =  EndDateTime

		from .reminder_view_with_startdatetime_enddatetime import ReminderViewWithStartDateTimeEndDateTimeRequest
		return ReminderViewWithStartDateTimeEndDateTimeRequest(self.request_adapter, path_parameters)

	@property
	def remove_all_devices_from_management(self,
	) -> RemoveAllDevicesFromManagementRequest:
		from .remove_all_devices_from_management import RemoveAllDevicesFromManagementRequest
		return RemoveAllDevicesFromManagementRequest(self.request_adapter, self.path_parameters)

	@property
	def reprocess_license_assignment(self,
	) -> ReprocessLicenseAssignmentRequest:
		from .reprocess_license_assignment import ReprocessLicenseAssignmentRequest
		return ReprocessLicenseAssignmentRequest(self.request_adapter, self.path_parameters)

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
	def revoke_sign_in_sessions(self,
	) -> RevokeSignInSessionsRequest:
		from .revoke_sign_in_sessions import RevokeSignInSessionsRequest
		return RevokeSignInSessionsRequest(self.request_adapter, self.path_parameters)

	@property
	def send_mail(self,
	) -> SendMailRequest:
		from .send_mail import SendMailRequest
		return SendMailRequest(self.request_adapter, self.path_parameters)

	@property
	def translate_exchange_ids(self,
	) -> TranslateExchangeIdsRequest:
		from .translate_exchange_ids import TranslateExchangeIdsRequest
		return TranslateExchangeIdsRequest(self.request_adapter, self.path_parameters)

	@property
	def wipe_managed_app_registrations_by_device_tag(self,
	) -> WipeManagedAppRegistrationsByDeviceTagRequest:
		from .wipe_managed_app_registrations_by_device_tag import WipeManagedAppRegistrationsByDeviceTagRequest
		return WipeManagedAppRegistrationsByDeviceTagRequest(self.request_adapter, self.path_parameters)

	@property
	def oauth2_permission_grants(self,
	) -> Oauth2PermissionGrantsRequest:
		from .oauth2_permission_grants import Oauth2PermissionGrantsRequest
		return Oauth2PermissionGrantsRequest(self.request_adapter, self.path_parameters)

	@property
	def onenote(self,
	) -> OnenoteRequest:
		from .onenote import OnenoteRequest
		return OnenoteRequest(self.request_adapter, self.path_parameters)

	@property
	def online_meetings(self,
	) -> OnlineMeetingsRequest:
		from .online_meetings import OnlineMeetingsRequest
		return OnlineMeetingsRequest(self.request_adapter, self.path_parameters)

	@property
	def outlook(self,
	) -> OutlookRequest:
		from .outlook import OutlookRequest
		return OutlookRequest(self.request_adapter, self.path_parameters)

	@property
	def owned_devices(self,
	) -> OwnedDevicesRequest:
		from .owned_devices import OwnedDevicesRequest
		return OwnedDevicesRequest(self.request_adapter, self.path_parameters)

	@property
	def owned_objects(self,
	) -> OwnedObjectsRequest:
		from .owned_objects import OwnedObjectsRequest
		return OwnedObjectsRequest(self.request_adapter, self.path_parameters)

	@property
	def people(self,
	) -> PeopleRequest:
		from .people import PeopleRequest
		return PeopleRequest(self.request_adapter, self.path_parameters)

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
	def presence(self,
	) -> PresenceRequest:
		from .presence import PresenceRequest
		return PresenceRequest(self.request_adapter, self.path_parameters)

	@property
	def registered_devices(self,
	) -> RegisteredDevicesRequest:
		from .registered_devices import RegisteredDevicesRequest
		return RegisteredDevicesRequest(self.request_adapter, self.path_parameters)

	@property
	def scoped_role_member_of(self,
	) -> ScopedRoleMemberOfRequest:
		from .scoped_role_member_of import ScopedRoleMemberOfRequest
		return ScopedRoleMemberOfRequest(self.request_adapter, self.path_parameters)

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
	def solutions(self,
	) -> SolutionsRequest:
		from .solutions import SolutionsRequest
		return SolutionsRequest(self.request_adapter, self.path_parameters)

	@property
	def sponsors(self,
	) -> SponsorsRequest:
		from .sponsors import SponsorsRequest
		return SponsorsRequest(self.request_adapter, self.path_parameters)

	@property
	def teamwork(self,
	) -> TeamworkRequest:
		from .teamwork import TeamworkRequest
		return TeamworkRequest(self.request_adapter, self.path_parameters)

	@property
	def todo(self,
	) -> TodoRequest:
		from .todo import TodoRequest
		return TodoRequest(self.request_adapter, self.path_parameters)

	@property
	def transitive_member_of(self,
	) -> TransitiveMemberOfRequest:
		from .transitive_member_of import TransitiveMemberOfRequest
		return TransitiveMemberOfRequest(self.request_adapter, self.path_parameters)

