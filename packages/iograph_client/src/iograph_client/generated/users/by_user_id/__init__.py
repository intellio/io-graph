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
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.models.user import User
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class ByUserIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/users/{user%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> User:
		"""
		Get user
		Read properties and relationships of the user object.
		Find more info here: https://learn.microsoft.com/graph/api/intune-mam-user-get?view=graph-rest-1.0
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
		Find more info here: https://learn.microsoft.com/graph/api/user-update?view=graph-rest-1.0
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
		Delete user
		Deletes a user.
		Find more info here: https://learn.microsoft.com/graph/api/intune-mam-user-delete?view=graph-rest-1.0
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

	def app_role_assignments(self,
		user_id: str,
	) -> AppRoleAssignmentsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .app_role_assignments import AppRoleAssignmentsRequest
		return AppRoleAssignmentsRequest(self.request_adapter, path_parameters)

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

	def device_management_troubleshooting_events(self,
		user_id: str,
	) -> DeviceManagementTroubleshootingEventsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .device_management_troubleshooting_events import DeviceManagementTroubleshootingEventsRequest
		return DeviceManagementTroubleshootingEventsRequest(self.request_adapter, path_parameters)

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

	def insights(self,
		user_id: str,
	) -> InsightsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .insights import InsightsRequest
		return InsightsRequest(self.request_adapter, path_parameters)

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

	def wipe_managed_app_registrations_by_device_tag(self,
		user_id: str,
	) -> WipeManagedAppRegistrationsByDeviceTagRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .wipe_managed_app_registrations_by_device_tag import WipeManagedAppRegistrationsByDeviceTagRequest
		return WipeManagedAppRegistrationsByDeviceTagRequest(self.request_adapter, path_parameters)

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

