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
	from .security import SecurityRequest
	from .partners import PartnersRequest
	from .monthly_print_usage_by_user import MonthlyPrintUsageByUserRequest
	from .monthly_print_usage_by_printer import MonthlyPrintUsageByPrinterRequest
	from .managed_device_enrollment_top_failures import ManagedDeviceEnrollmentTopFailuresRequest
	from .managed_device_enrollment_failure_details import ManagedDeviceEnrollmentFailureDetailsRequest
	from .get_yammer_groups_activity_group_counts import GetYammerGroupsActivityGroupCountsRequest
	from .get_yammer_groups_activity_detail import GetYammerGroupsActivityDetailRequest
	from .get_yammer_groups_activity_counts import GetYammerGroupsActivityCountsRequest
	from .get_yammer_device_usage_user_detail import GetYammerDeviceUsageUserDetailRequest
	from .get_yammer_device_usage_user_counts import GetYammerDeviceUsageUserCountsRequest
	from .get_yammer_device_usage_distribution_user_counts import GetYammerDeviceUsageDistributionUserCountsRequest
	from .get_yammer_activity_user_detail import GetYammerActivityUserDetailRequest
	from .get_yammer_activity_user_counts import GetYammerActivityUserCountsRequest
	from .get_yammer_activity_counts import GetYammerActivityCountsRequest
	from .get_user_archived_print_jobs import GetUserArchivedPrintJobsRequest
	from .get_teams_user_activity_user_detail import GetTeamsUserActivityUserDetailRequest
	from .get_teams_user_activity_user_counts import GetTeamsUserActivityUserCountsRequest
	from .get_teams_user_activity_counts import GetTeamsUserActivityCountsRequest
	from .get_teams_team_counts import GetTeamsTeamCountsRequest
	from .get_teams_team_activity_distribution_counts import GetTeamsTeamActivityDistributionCountsRequest
	from .get_teams_team_activity_detail import GetTeamsTeamActivityDetailRequest
	from .get_teams_team_activity_counts import GetTeamsTeamActivityCountsRequest
	from .get_teams_device_usage_user_detail import GetTeamsDeviceUsageUserDetailRequest
	from .get_teams_device_usage_user_counts import GetTeamsDeviceUsageUserCountsRequest
	from .get_teams_device_usage_distribution_user_counts import GetTeamsDeviceUsageDistributionUserCountsRequest
	from .get_skype_for_business_peer_to_peer_activity_user_counts import GetSkypeForBusinessPeerToPeerActivityUserCountsRequest
	from .get_skype_for_business_peer_to_peer_activity_minute_counts import GetSkypeForBusinessPeerToPeerActivityMinuteCountsRequest
	from .get_skype_for_business_peer_to_peer_activity_counts import GetSkypeForBusinessPeerToPeerActivityCountsRequest
	from .get_skype_for_business_participant_activity_user_counts import GetSkypeForBusinessParticipantActivityUserCountsRequest
	from .get_skype_for_business_participant_activity_minute_counts import GetSkypeForBusinessParticipantActivityMinuteCountsRequest
	from .get_skype_for_business_participant_activity_counts import GetSkypeForBusinessParticipantActivityCountsRequest
	from .get_skype_for_business_organizer_activity_user_counts import GetSkypeForBusinessOrganizerActivityUserCountsRequest
	from .get_skype_for_business_organizer_activity_minute_counts import GetSkypeForBusinessOrganizerActivityMinuteCountsRequest
	from .get_skype_for_business_organizer_activity_counts import GetSkypeForBusinessOrganizerActivityCountsRequest
	from .get_skype_for_business_device_usage_user_detail import GetSkypeForBusinessDeviceUsageUserDetailRequest
	from .get_skype_for_business_device_usage_user_counts import GetSkypeForBusinessDeviceUsageUserCountsRequest
	from .get_skype_for_business_device_usage_distribution_user_counts import GetSkypeForBusinessDeviceUsageDistributionUserCountsRequest
	from .get_skype_for_business_activity_user_detail import GetSkypeForBusinessActivityUserDetailRequest
	from .get_skype_for_business_activity_user_counts import GetSkypeForBusinessActivityUserCountsRequest
	from .get_skype_for_business_activity_counts import GetSkypeForBusinessActivityCountsRequest
	from .get_share_point_site_usage_storage import GetSharePointSiteUsageStorageRequest
	from .get_share_point_site_usage_site_counts import GetSharePointSiteUsageSiteCountsRequest
	from .get_share_point_site_usage_pages import GetSharePointSiteUsagePagesRequest
	from .get_share_point_site_usage_file_counts import GetSharePointSiteUsageFileCountsRequest
	from .get_share_point_site_usage_detail import GetSharePointSiteUsageDetailRequest
	from .get_share_point_activity_user_detail import GetSharePointActivityUserDetailRequest
	from .get_share_point_activity_user_counts import GetSharePointActivityUserCountsRequest
	from .get_share_point_activity_pages import GetSharePointActivityPagesRequest
	from .get_share_point_activity_file_counts import GetSharePointActivityFileCountsRequest
	from .get_relying_party_detailed_summary import GetRelyingPartyDetailedSummaryRequest
	from .get_printer_archived_print_jobs import GetPrinterArchivedPrintJobsRequest
	from .get_one_drive_usage_storage import GetOneDriveUsageStorageRequest
	from .get_one_drive_usage_file_counts import GetOneDriveUsageFileCountsRequest
	from .get_one_drive_usage_account_detail import GetOneDriveUsageAccountDetailRequest
	from .get_one_drive_usage_account_counts import GetOneDriveUsageAccountCountsRequest
	from .get_one_drive_activity_user_detail import GetOneDriveActivityUserDetailRequest
	from .get_one_drive_activity_user_counts import GetOneDriveActivityUserCountsRequest
	from .get_one_drive_activity_file_counts import GetOneDriveActivityFileCountsRequest
	from .get_office365_services_user_counts import GetOffice365ServicesUserCountsRequest
	from .get_office365_groups_activity_storage import GetOffice365GroupsActivityStorageRequest
	from .get_office365_groups_activity_group_counts import GetOffice365GroupsActivityGroupCountsRequest
	from .get_office365_groups_activity_file_counts import GetOffice365GroupsActivityFileCountsRequest
	from .get_office365_groups_activity_detail import GetOffice365GroupsActivityDetailRequest
	from .get_office365_groups_activity_counts import GetOffice365GroupsActivityCountsRequest
	from .get_office365_active_user_detail import GetOffice365ActiveUserDetailRequest
	from .get_office365_active_user_counts import GetOffice365ActiveUserCountsRequest
	from .get_office365_activations_user_detail import GetOffice365ActivationsUserDetailRequest
	from .get_office365_activations_user_counts import GetOffice365ActivationsUserCountsRequest
	from .get_office365_activation_counts import GetOffice365ActivationCountsRequest
	from .get_mailbox_usage_storage import GetMailboxUsageStorageRequest
	from .get_mailbox_usage_quota_status_mailbox_counts import GetMailboxUsageQuotaStatusMailboxCountsRequest
	from .get_mailbox_usage_mailbox_counts import GetMailboxUsageMailboxCountsRequest
	from .get_mailbox_usage_detail import GetMailboxUsageDetailRequest
	from .get_m365_app_user_detail import GetM365AppUserDetailRequest
	from .get_m365_app_user_counts import GetM365AppUserCountsRequest
	from .get_m365_app_platform_user_counts import GetM365AppPlatformUserCountsRequest
	from .get_group_archived_print_jobs import GetGroupArchivedPrintJobsRequest
	from .get_email_app_usage_versions_user_counts import GetEmailAppUsageVersionsUserCountsRequest
	from .get_email_app_usage_user_detail import GetEmailAppUsageUserDetailRequest
	from .get_email_app_usage_user_counts import GetEmailAppUsageUserCountsRequest
	from .get_email_app_usage_apps_user_counts import GetEmailAppUsageAppsUserCountsRequest
	from .get_email_activity_user_detail import GetEmailActivityUserDetailRequest
	from .get_email_activity_user_counts import GetEmailActivityUserCountsRequest
	from .get_email_activity_counts import GetEmailActivityCountsRequest
	from .device_configuration_user_activity import DeviceConfigurationUserActivityRequest
	from .device_configuration_device_activity import DeviceConfigurationDeviceActivityRequest
	from .daily_print_usage_by_user import DailyPrintUsageByUserRequest
	from .daily_print_usage_by_printer import DailyPrintUsageByPrinterRequest
	from .authentication_methods import AuthenticationMethodsRequest
	from ...request_adapter import HttpxRequestAdapter
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.report_root import ReportRoot


class ReportsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/reports", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> ReportRoot:
		"""
		Get reportRoot
		Read properties and relationships of the reportRoot object.
		Find more info here: https://learn.microsoft.com/graph/api/intune-deviceconfig-reportroot-get?view=graph-rest-1.0
		"""
		tags = ['reports.reportRoot']

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
		return await self.request_adapter.send_async(request_info, ReportRoot, error_mapping)

	async def patch(
		self,
		body: ReportRoot,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> ReportRoot:
		"""
		Update reportRoot
		Update the properties of a reportRoot object.
		Find more info here: https://learn.microsoft.com/graph/api/intune-deviceconfig-reportroot-update?view=graph-rest-1.0
		"""
		tags = ['reports.reportRoot']

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
		return await self.request_adapter.send_async(request_info, ReportRoot, error_mapping)

	class GetQueryParams(BaseModel):
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> ReportsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ReportsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ReportsRequest(self.request_adapter, self.path_parameters)

	@property
	def authentication_methods(self,
	) -> AuthenticationMethodsRequest:
		from .authentication_methods import AuthenticationMethodsRequest
		return AuthenticationMethodsRequest(self.request_adapter, self.path_parameters)

	@property
	def daily_print_usage_by_printer(self,
	) -> DailyPrintUsageByPrinterRequest:
		from .daily_print_usage_by_printer import DailyPrintUsageByPrinterRequest
		return DailyPrintUsageByPrinterRequest(self.request_adapter, self.path_parameters)

	@property
	def daily_print_usage_by_user(self,
	) -> DailyPrintUsageByUserRequest:
		from .daily_print_usage_by_user import DailyPrintUsageByUserRequest
		return DailyPrintUsageByUserRequest(self.request_adapter, self.path_parameters)

	@property
	def device_configuration_device_activity(self,
	) -> DeviceConfigurationDeviceActivityRequest:
		from .device_configuration_device_activity import DeviceConfigurationDeviceActivityRequest
		return DeviceConfigurationDeviceActivityRequest(self.request_adapter, self.path_parameters)

	@property
	def device_configuration_user_activity(self,
	) -> DeviceConfigurationUserActivityRequest:
		from .device_configuration_user_activity import DeviceConfigurationUserActivityRequest
		return DeviceConfigurationUserActivityRequest(self.request_adapter, self.path_parameters)

	def get_email_activity_counts(self,
		period: str,
	) -> GetEmailActivityCountsRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_email_activity_counts import GetEmailActivityCountsRequest
		return GetEmailActivityCountsRequest(self.request_adapter, path_parameters)

	def get_email_activity_user_counts(self,
		period: str,
	) -> GetEmailActivityUserCountsRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_email_activity_user_counts import GetEmailActivityUserCountsRequest
		return GetEmailActivityUserCountsRequest(self.request_adapter, path_parameters)

	def get_email_activity_user_detail(self,
		date: str,
	) -> GetEmailActivityUserDetailRequest:
		if date is None:
			raise TypeError("date cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["date"] =  date

		from .get_email_activity_user_detail import GetEmailActivityUserDetailRequest
		return GetEmailActivityUserDetailRequest(self.request_adapter, path_parameters)

	def get_email_app_usage_apps_user_counts(self,
		period: str,
	) -> GetEmailAppUsageAppsUserCountsRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_email_app_usage_apps_user_counts import GetEmailAppUsageAppsUserCountsRequest
		return GetEmailAppUsageAppsUserCountsRequest(self.request_adapter, path_parameters)

	def get_email_app_usage_user_counts(self,
		period: str,
	) -> GetEmailAppUsageUserCountsRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_email_app_usage_user_counts import GetEmailAppUsageUserCountsRequest
		return GetEmailAppUsageUserCountsRequest(self.request_adapter, path_parameters)

	def get_email_app_usage_user_detail(self,
		date: str,
	) -> GetEmailAppUsageUserDetailRequest:
		if date is None:
			raise TypeError("date cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["date"] =  date

		from .get_email_app_usage_user_detail import GetEmailAppUsageUserDetailRequest
		return GetEmailAppUsageUserDetailRequest(self.request_adapter, path_parameters)

	def get_email_app_usage_versions_user_counts(self,
		period: str,
	) -> GetEmailAppUsageVersionsUserCountsRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_email_app_usage_versions_user_counts import GetEmailAppUsageVersionsUserCountsRequest
		return GetEmailAppUsageVersionsUserCountsRequest(self.request_adapter, path_parameters)

	def get_group_archived_print_jobs(self,
		groupId: str,
		startDateTime: datetime,
		endDateTime: datetime,
	) -> GetGroupArchivedPrintJobsRequest:
		if groupId is None:
			raise TypeError("groupId cannot be null.")
		if startDateTime is None:
			raise TypeError("startDateTime cannot be null.")
		if endDateTime is None:
			raise TypeError("endDateTime cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["groupId"] =  groupId
		path_parameters["startDateTime"] =  startDateTime
		path_parameters["endDateTime"] =  endDateTime

		from .get_group_archived_print_jobs import GetGroupArchivedPrintJobsRequest
		return GetGroupArchivedPrintJobsRequest(self.request_adapter, path_parameters)

	def get_m365_app_platform_user_counts(self,
		period: str,
	) -> GetM365AppPlatformUserCountsRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_m365_app_platform_user_counts import GetM365AppPlatformUserCountsRequest
		return GetM365AppPlatformUserCountsRequest(self.request_adapter, path_parameters)

	def get_m365_app_user_counts(self,
		period: str,
	) -> GetM365AppUserCountsRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_m365_app_user_counts import GetM365AppUserCountsRequest
		return GetM365AppUserCountsRequest(self.request_adapter, path_parameters)

	def get_m365_app_user_detail(self,
		date: str,
	) -> GetM365AppUserDetailRequest:
		if date is None:
			raise TypeError("date cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["date"] =  date

		from .get_m365_app_user_detail import GetM365AppUserDetailRequest
		return GetM365AppUserDetailRequest(self.request_adapter, path_parameters)

	def get_mailbox_usage_detail(self,
		period: str,
	) -> GetMailboxUsageDetailRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_mailbox_usage_detail import GetMailboxUsageDetailRequest
		return GetMailboxUsageDetailRequest(self.request_adapter, path_parameters)

	def get_mailbox_usage_mailbox_counts(self,
		period: str,
	) -> GetMailboxUsageMailboxCountsRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_mailbox_usage_mailbox_counts import GetMailboxUsageMailboxCountsRequest
		return GetMailboxUsageMailboxCountsRequest(self.request_adapter, path_parameters)

	def get_mailbox_usage_quota_status_mailbox_counts(self,
		period: str,
	) -> GetMailboxUsageQuotaStatusMailboxCountsRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_mailbox_usage_quota_status_mailbox_counts import GetMailboxUsageQuotaStatusMailboxCountsRequest
		return GetMailboxUsageQuotaStatusMailboxCountsRequest(self.request_adapter, path_parameters)

	def get_mailbox_usage_storage(self,
		period: str,
	) -> GetMailboxUsageStorageRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_mailbox_usage_storage import GetMailboxUsageStorageRequest
		return GetMailboxUsageStorageRequest(self.request_adapter, path_parameters)

	@property
	def get_office365_activation_counts(self,
	) -> GetOffice365ActivationCountsRequest:
		from .get_office365_activation_counts import GetOffice365ActivationCountsRequest
		return GetOffice365ActivationCountsRequest(self.request_adapter, self.path_parameters)

	@property
	def get_office365_activations_user_counts(self,
	) -> GetOffice365ActivationsUserCountsRequest:
		from .get_office365_activations_user_counts import GetOffice365ActivationsUserCountsRequest
		return GetOffice365ActivationsUserCountsRequest(self.request_adapter, self.path_parameters)

	@property
	def get_office365_activations_user_detail(self,
	) -> GetOffice365ActivationsUserDetailRequest:
		from .get_office365_activations_user_detail import GetOffice365ActivationsUserDetailRequest
		return GetOffice365ActivationsUserDetailRequest(self.request_adapter, self.path_parameters)

	def get_office365_active_user_counts(self,
		period: str,
	) -> GetOffice365ActiveUserCountsRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_office365_active_user_counts import GetOffice365ActiveUserCountsRequest
		return GetOffice365ActiveUserCountsRequest(self.request_adapter, path_parameters)

	def get_office365_active_user_detail(self,
		date: str,
	) -> GetOffice365ActiveUserDetailRequest:
		if date is None:
			raise TypeError("date cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["date"] =  date

		from .get_office365_active_user_detail import GetOffice365ActiveUserDetailRequest
		return GetOffice365ActiveUserDetailRequest(self.request_adapter, path_parameters)

	def get_office365_groups_activity_counts(self,
		period: str,
	) -> GetOffice365GroupsActivityCountsRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_office365_groups_activity_counts import GetOffice365GroupsActivityCountsRequest
		return GetOffice365GroupsActivityCountsRequest(self.request_adapter, path_parameters)

	def get_office365_groups_activity_detail(self,
		date: str,
	) -> GetOffice365GroupsActivityDetailRequest:
		if date is None:
			raise TypeError("date cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["date"] =  date

		from .get_office365_groups_activity_detail import GetOffice365GroupsActivityDetailRequest
		return GetOffice365GroupsActivityDetailRequest(self.request_adapter, path_parameters)

	def get_office365_groups_activity_file_counts(self,
		period: str,
	) -> GetOffice365GroupsActivityFileCountsRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_office365_groups_activity_file_counts import GetOffice365GroupsActivityFileCountsRequest
		return GetOffice365GroupsActivityFileCountsRequest(self.request_adapter, path_parameters)

	def get_office365_groups_activity_group_counts(self,
		period: str,
	) -> GetOffice365GroupsActivityGroupCountsRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_office365_groups_activity_group_counts import GetOffice365GroupsActivityGroupCountsRequest
		return GetOffice365GroupsActivityGroupCountsRequest(self.request_adapter, path_parameters)

	def get_office365_groups_activity_storage(self,
		period: str,
	) -> GetOffice365GroupsActivityStorageRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_office365_groups_activity_storage import GetOffice365GroupsActivityStorageRequest
		return GetOffice365GroupsActivityStorageRequest(self.request_adapter, path_parameters)

	def get_office365_services_user_counts(self,
		period: str,
	) -> GetOffice365ServicesUserCountsRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_office365_services_user_counts import GetOffice365ServicesUserCountsRequest
		return GetOffice365ServicesUserCountsRequest(self.request_adapter, path_parameters)

	def get_one_drive_activity_file_counts(self,
		period: str,
	) -> GetOneDriveActivityFileCountsRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_one_drive_activity_file_counts import GetOneDriveActivityFileCountsRequest
		return GetOneDriveActivityFileCountsRequest(self.request_adapter, path_parameters)

	def get_one_drive_activity_user_counts(self,
		period: str,
	) -> GetOneDriveActivityUserCountsRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_one_drive_activity_user_counts import GetOneDriveActivityUserCountsRequest
		return GetOneDriveActivityUserCountsRequest(self.request_adapter, path_parameters)

	def get_one_drive_activity_user_detail(self,
		date: str,
	) -> GetOneDriveActivityUserDetailRequest:
		if date is None:
			raise TypeError("date cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["date"] =  date

		from .get_one_drive_activity_user_detail import GetOneDriveActivityUserDetailRequest
		return GetOneDriveActivityUserDetailRequest(self.request_adapter, path_parameters)

	def get_one_drive_usage_account_counts(self,
		period: str,
	) -> GetOneDriveUsageAccountCountsRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_one_drive_usage_account_counts import GetOneDriveUsageAccountCountsRequest
		return GetOneDriveUsageAccountCountsRequest(self.request_adapter, path_parameters)

	def get_one_drive_usage_account_detail(self,
		date: str,
	) -> GetOneDriveUsageAccountDetailRequest:
		if date is None:
			raise TypeError("date cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["date"] =  date

		from .get_one_drive_usage_account_detail import GetOneDriveUsageAccountDetailRequest
		return GetOneDriveUsageAccountDetailRequest(self.request_adapter, path_parameters)

	def get_one_drive_usage_file_counts(self,
		period: str,
	) -> GetOneDriveUsageFileCountsRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_one_drive_usage_file_counts import GetOneDriveUsageFileCountsRequest
		return GetOneDriveUsageFileCountsRequest(self.request_adapter, path_parameters)

	def get_one_drive_usage_storage(self,
		period: str,
	) -> GetOneDriveUsageStorageRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_one_drive_usage_storage import GetOneDriveUsageStorageRequest
		return GetOneDriveUsageStorageRequest(self.request_adapter, path_parameters)

	def get_printer_archived_print_jobs(self,
		printerId: str,
		startDateTime: datetime,
		endDateTime: datetime,
	) -> GetPrinterArchivedPrintJobsRequest:
		if printerId is None:
			raise TypeError("printerId cannot be null.")
		if startDateTime is None:
			raise TypeError("startDateTime cannot be null.")
		if endDateTime is None:
			raise TypeError("endDateTime cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["printerId"] =  printerId
		path_parameters["startDateTime"] =  startDateTime
		path_parameters["endDateTime"] =  endDateTime

		from .get_printer_archived_print_jobs import GetPrinterArchivedPrintJobsRequest
		return GetPrinterArchivedPrintJobsRequest(self.request_adapter, path_parameters)

	def get_relying_party_detailed_summary(self,
		period: str,
	) -> GetRelyingPartyDetailedSummaryRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_relying_party_detailed_summary import GetRelyingPartyDetailedSummaryRequest
		return GetRelyingPartyDetailedSummaryRequest(self.request_adapter, path_parameters)

	def get_share_point_activity_file_counts(self,
		period: str,
	) -> GetSharePointActivityFileCountsRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_share_point_activity_file_counts import GetSharePointActivityFileCountsRequest
		return GetSharePointActivityFileCountsRequest(self.request_adapter, path_parameters)

	def get_share_point_activity_pages(self,
		period: str,
	) -> GetSharePointActivityPagesRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_share_point_activity_pages import GetSharePointActivityPagesRequest
		return GetSharePointActivityPagesRequest(self.request_adapter, path_parameters)

	def get_share_point_activity_user_counts(self,
		period: str,
	) -> GetSharePointActivityUserCountsRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_share_point_activity_user_counts import GetSharePointActivityUserCountsRequest
		return GetSharePointActivityUserCountsRequest(self.request_adapter, path_parameters)

	def get_share_point_activity_user_detail(self,
		date: str,
	) -> GetSharePointActivityUserDetailRequest:
		if date is None:
			raise TypeError("date cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["date"] =  date

		from .get_share_point_activity_user_detail import GetSharePointActivityUserDetailRequest
		return GetSharePointActivityUserDetailRequest(self.request_adapter, path_parameters)

	def get_share_point_site_usage_detail(self,
		date: str,
	) -> GetSharePointSiteUsageDetailRequest:
		if date is None:
			raise TypeError("date cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["date"] =  date

		from .get_share_point_site_usage_detail import GetSharePointSiteUsageDetailRequest
		return GetSharePointSiteUsageDetailRequest(self.request_adapter, path_parameters)

	def get_share_point_site_usage_file_counts(self,
		period: str,
	) -> GetSharePointSiteUsageFileCountsRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_share_point_site_usage_file_counts import GetSharePointSiteUsageFileCountsRequest
		return GetSharePointSiteUsageFileCountsRequest(self.request_adapter, path_parameters)

	def get_share_point_site_usage_pages(self,
		period: str,
	) -> GetSharePointSiteUsagePagesRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_share_point_site_usage_pages import GetSharePointSiteUsagePagesRequest
		return GetSharePointSiteUsagePagesRequest(self.request_adapter, path_parameters)

	def get_share_point_site_usage_site_counts(self,
		period: str,
	) -> GetSharePointSiteUsageSiteCountsRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_share_point_site_usage_site_counts import GetSharePointSiteUsageSiteCountsRequest
		return GetSharePointSiteUsageSiteCountsRequest(self.request_adapter, path_parameters)

	def get_share_point_site_usage_storage(self,
		period: str,
	) -> GetSharePointSiteUsageStorageRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_share_point_site_usage_storage import GetSharePointSiteUsageStorageRequest
		return GetSharePointSiteUsageStorageRequest(self.request_adapter, path_parameters)

	def get_skype_for_business_activity_counts(self,
		period: str,
	) -> GetSkypeForBusinessActivityCountsRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_skype_for_business_activity_counts import GetSkypeForBusinessActivityCountsRequest
		return GetSkypeForBusinessActivityCountsRequest(self.request_adapter, path_parameters)

	def get_skype_for_business_activity_user_counts(self,
		period: str,
	) -> GetSkypeForBusinessActivityUserCountsRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_skype_for_business_activity_user_counts import GetSkypeForBusinessActivityUserCountsRequest
		return GetSkypeForBusinessActivityUserCountsRequest(self.request_adapter, path_parameters)

	def get_skype_for_business_activity_user_detail(self,
		date: str,
	) -> GetSkypeForBusinessActivityUserDetailRequest:
		if date is None:
			raise TypeError("date cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["date"] =  date

		from .get_skype_for_business_activity_user_detail import GetSkypeForBusinessActivityUserDetailRequest
		return GetSkypeForBusinessActivityUserDetailRequest(self.request_adapter, path_parameters)

	def get_skype_for_business_device_usage_distribution_user_counts(self,
		period: str,
	) -> GetSkypeForBusinessDeviceUsageDistributionUserCountsRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_skype_for_business_device_usage_distribution_user_counts import GetSkypeForBusinessDeviceUsageDistributionUserCountsRequest
		return GetSkypeForBusinessDeviceUsageDistributionUserCountsRequest(self.request_adapter, path_parameters)

	def get_skype_for_business_device_usage_user_counts(self,
		period: str,
	) -> GetSkypeForBusinessDeviceUsageUserCountsRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_skype_for_business_device_usage_user_counts import GetSkypeForBusinessDeviceUsageUserCountsRequest
		return GetSkypeForBusinessDeviceUsageUserCountsRequest(self.request_adapter, path_parameters)

	def get_skype_for_business_device_usage_user_detail(self,
		date: str,
	) -> GetSkypeForBusinessDeviceUsageUserDetailRequest:
		if date is None:
			raise TypeError("date cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["date"] =  date

		from .get_skype_for_business_device_usage_user_detail import GetSkypeForBusinessDeviceUsageUserDetailRequest
		return GetSkypeForBusinessDeviceUsageUserDetailRequest(self.request_adapter, path_parameters)

	def get_skype_for_business_organizer_activity_counts(self,
		period: str,
	) -> GetSkypeForBusinessOrganizerActivityCountsRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_skype_for_business_organizer_activity_counts import GetSkypeForBusinessOrganizerActivityCountsRequest
		return GetSkypeForBusinessOrganizerActivityCountsRequest(self.request_adapter, path_parameters)

	def get_skype_for_business_organizer_activity_minute_counts(self,
		period: str,
	) -> GetSkypeForBusinessOrganizerActivityMinuteCountsRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_skype_for_business_organizer_activity_minute_counts import GetSkypeForBusinessOrganizerActivityMinuteCountsRequest
		return GetSkypeForBusinessOrganizerActivityMinuteCountsRequest(self.request_adapter, path_parameters)

	def get_skype_for_business_organizer_activity_user_counts(self,
		period: str,
	) -> GetSkypeForBusinessOrganizerActivityUserCountsRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_skype_for_business_organizer_activity_user_counts import GetSkypeForBusinessOrganizerActivityUserCountsRequest
		return GetSkypeForBusinessOrganizerActivityUserCountsRequest(self.request_adapter, path_parameters)

	def get_skype_for_business_participant_activity_counts(self,
		period: str,
	) -> GetSkypeForBusinessParticipantActivityCountsRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_skype_for_business_participant_activity_counts import GetSkypeForBusinessParticipantActivityCountsRequest
		return GetSkypeForBusinessParticipantActivityCountsRequest(self.request_adapter, path_parameters)

	def get_skype_for_business_participant_activity_minute_counts(self,
		period: str,
	) -> GetSkypeForBusinessParticipantActivityMinuteCountsRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_skype_for_business_participant_activity_minute_counts import GetSkypeForBusinessParticipantActivityMinuteCountsRequest
		return GetSkypeForBusinessParticipantActivityMinuteCountsRequest(self.request_adapter, path_parameters)

	def get_skype_for_business_participant_activity_user_counts(self,
		period: str,
	) -> GetSkypeForBusinessParticipantActivityUserCountsRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_skype_for_business_participant_activity_user_counts import GetSkypeForBusinessParticipantActivityUserCountsRequest
		return GetSkypeForBusinessParticipantActivityUserCountsRequest(self.request_adapter, path_parameters)

	def get_skype_for_business_peer_to_peer_activity_counts(self,
		period: str,
	) -> GetSkypeForBusinessPeerToPeerActivityCountsRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_skype_for_business_peer_to_peer_activity_counts import GetSkypeForBusinessPeerToPeerActivityCountsRequest
		return GetSkypeForBusinessPeerToPeerActivityCountsRequest(self.request_adapter, path_parameters)

	def get_skype_for_business_peer_to_peer_activity_minute_counts(self,
		period: str,
	) -> GetSkypeForBusinessPeerToPeerActivityMinuteCountsRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_skype_for_business_peer_to_peer_activity_minute_counts import GetSkypeForBusinessPeerToPeerActivityMinuteCountsRequest
		return GetSkypeForBusinessPeerToPeerActivityMinuteCountsRequest(self.request_adapter, path_parameters)

	def get_skype_for_business_peer_to_peer_activity_user_counts(self,
		period: str,
	) -> GetSkypeForBusinessPeerToPeerActivityUserCountsRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_skype_for_business_peer_to_peer_activity_user_counts import GetSkypeForBusinessPeerToPeerActivityUserCountsRequest
		return GetSkypeForBusinessPeerToPeerActivityUserCountsRequest(self.request_adapter, path_parameters)

	def get_teams_device_usage_distribution_user_counts(self,
		period: str,
	) -> GetTeamsDeviceUsageDistributionUserCountsRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_teams_device_usage_distribution_user_counts import GetTeamsDeviceUsageDistributionUserCountsRequest
		return GetTeamsDeviceUsageDistributionUserCountsRequest(self.request_adapter, path_parameters)

	def get_teams_device_usage_user_counts(self,
		period: str,
	) -> GetTeamsDeviceUsageUserCountsRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_teams_device_usage_user_counts import GetTeamsDeviceUsageUserCountsRequest
		return GetTeamsDeviceUsageUserCountsRequest(self.request_adapter, path_parameters)

	def get_teams_device_usage_user_detail(self,
		date: str,
	) -> GetTeamsDeviceUsageUserDetailRequest:
		if date is None:
			raise TypeError("date cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["date"] =  date

		from .get_teams_device_usage_user_detail import GetTeamsDeviceUsageUserDetailRequest
		return GetTeamsDeviceUsageUserDetailRequest(self.request_adapter, path_parameters)

	def get_teams_team_activity_counts(self,
		period: str,
	) -> GetTeamsTeamActivityCountsRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_teams_team_activity_counts import GetTeamsTeamActivityCountsRequest
		return GetTeamsTeamActivityCountsRequest(self.request_adapter, path_parameters)

	def get_teams_team_activity_detail(self,
		date: str,
	) -> GetTeamsTeamActivityDetailRequest:
		if date is None:
			raise TypeError("date cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["date"] =  date

		from .get_teams_team_activity_detail import GetTeamsTeamActivityDetailRequest
		return GetTeamsTeamActivityDetailRequest(self.request_adapter, path_parameters)

	def get_teams_team_activity_distribution_counts(self,
		period: str,
	) -> GetTeamsTeamActivityDistributionCountsRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_teams_team_activity_distribution_counts import GetTeamsTeamActivityDistributionCountsRequest
		return GetTeamsTeamActivityDistributionCountsRequest(self.request_adapter, path_parameters)

	def get_teams_team_counts(self,
		period: str,
	) -> GetTeamsTeamCountsRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_teams_team_counts import GetTeamsTeamCountsRequest
		return GetTeamsTeamCountsRequest(self.request_adapter, path_parameters)

	def get_teams_user_activity_counts(self,
		period: str,
	) -> GetTeamsUserActivityCountsRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_teams_user_activity_counts import GetTeamsUserActivityCountsRequest
		return GetTeamsUserActivityCountsRequest(self.request_adapter, path_parameters)

	def get_teams_user_activity_user_counts(self,
		period: str,
	) -> GetTeamsUserActivityUserCountsRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_teams_user_activity_user_counts import GetTeamsUserActivityUserCountsRequest
		return GetTeamsUserActivityUserCountsRequest(self.request_adapter, path_parameters)

	def get_teams_user_activity_user_detail(self,
		date: str,
	) -> GetTeamsUserActivityUserDetailRequest:
		if date is None:
			raise TypeError("date cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["date"] =  date

		from .get_teams_user_activity_user_detail import GetTeamsUserActivityUserDetailRequest
		return GetTeamsUserActivityUserDetailRequest(self.request_adapter, path_parameters)

	def get_user_archived_print_jobs(self,
		userId: str,
		startDateTime: datetime,
		endDateTime: datetime,
	) -> GetUserArchivedPrintJobsRequest:
		if userId is None:
			raise TypeError("userId cannot be null.")
		if startDateTime is None:
			raise TypeError("startDateTime cannot be null.")
		if endDateTime is None:
			raise TypeError("endDateTime cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["userId"] =  userId
		path_parameters["startDateTime"] =  startDateTime
		path_parameters["endDateTime"] =  endDateTime

		from .get_user_archived_print_jobs import GetUserArchivedPrintJobsRequest
		return GetUserArchivedPrintJobsRequest(self.request_adapter, path_parameters)

	def get_yammer_activity_counts(self,
		period: str,
	) -> GetYammerActivityCountsRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_yammer_activity_counts import GetYammerActivityCountsRequest
		return GetYammerActivityCountsRequest(self.request_adapter, path_parameters)

	def get_yammer_activity_user_counts(self,
		period: str,
	) -> GetYammerActivityUserCountsRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_yammer_activity_user_counts import GetYammerActivityUserCountsRequest
		return GetYammerActivityUserCountsRequest(self.request_adapter, path_parameters)

	def get_yammer_activity_user_detail(self,
		date: str,
	) -> GetYammerActivityUserDetailRequest:
		if date is None:
			raise TypeError("date cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["date"] =  date

		from .get_yammer_activity_user_detail import GetYammerActivityUserDetailRequest
		return GetYammerActivityUserDetailRequest(self.request_adapter, path_parameters)

	def get_yammer_device_usage_distribution_user_counts(self,
		period: str,
	) -> GetYammerDeviceUsageDistributionUserCountsRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_yammer_device_usage_distribution_user_counts import GetYammerDeviceUsageDistributionUserCountsRequest
		return GetYammerDeviceUsageDistributionUserCountsRequest(self.request_adapter, path_parameters)

	def get_yammer_device_usage_user_counts(self,
		period: str,
	) -> GetYammerDeviceUsageUserCountsRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_yammer_device_usage_user_counts import GetYammerDeviceUsageUserCountsRequest
		return GetYammerDeviceUsageUserCountsRequest(self.request_adapter, path_parameters)

	def get_yammer_device_usage_user_detail(self,
		date: str,
	) -> GetYammerDeviceUsageUserDetailRequest:
		if date is None:
			raise TypeError("date cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["date"] =  date

		from .get_yammer_device_usage_user_detail import GetYammerDeviceUsageUserDetailRequest
		return GetYammerDeviceUsageUserDetailRequest(self.request_adapter, path_parameters)

	def get_yammer_groups_activity_counts(self,
		period: str,
	) -> GetYammerGroupsActivityCountsRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_yammer_groups_activity_counts import GetYammerGroupsActivityCountsRequest
		return GetYammerGroupsActivityCountsRequest(self.request_adapter, path_parameters)

	def get_yammer_groups_activity_detail(self,
		date: str,
	) -> GetYammerGroupsActivityDetailRequest:
		if date is None:
			raise TypeError("date cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["date"] =  date

		from .get_yammer_groups_activity_detail import GetYammerGroupsActivityDetailRequest
		return GetYammerGroupsActivityDetailRequest(self.request_adapter, path_parameters)

	def get_yammer_groups_activity_group_counts(self,
		period: str,
	) -> GetYammerGroupsActivityGroupCountsRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_yammer_groups_activity_group_counts import GetYammerGroupsActivityGroupCountsRequest
		return GetYammerGroupsActivityGroupCountsRequest(self.request_adapter, path_parameters)

	@property
	def managed_device_enrollment_failure_details(self,
	) -> ManagedDeviceEnrollmentFailureDetailsRequest:
		from .managed_device_enrollment_failure_details import ManagedDeviceEnrollmentFailureDetailsRequest
		return ManagedDeviceEnrollmentFailureDetailsRequest(self.request_adapter, self.path_parameters)

	@property
	def managed_device_enrollment_top_failures(self,
	) -> ManagedDeviceEnrollmentTopFailuresRequest:
		from .managed_device_enrollment_top_failures import ManagedDeviceEnrollmentTopFailuresRequest
		return ManagedDeviceEnrollmentTopFailuresRequest(self.request_adapter, self.path_parameters)

	@property
	def monthly_print_usage_by_printer(self,
	) -> MonthlyPrintUsageByPrinterRequest:
		from .monthly_print_usage_by_printer import MonthlyPrintUsageByPrinterRequest
		return MonthlyPrintUsageByPrinterRequest(self.request_adapter, self.path_parameters)

	@property
	def monthly_print_usage_by_user(self,
	) -> MonthlyPrintUsageByUserRequest:
		from .monthly_print_usage_by_user import MonthlyPrintUsageByUserRequest
		return MonthlyPrintUsageByUserRequest(self.request_adapter, self.path_parameters)

	@property
	def partners(self,
	) -> PartnersRequest:
		from .partners import PartnersRequest
		return PartnersRequest(self.request_adapter, self.path_parameters)

	@property
	def security(self,
	) -> SecurityRequest:
		from .security import SecurityRequest
		return SecurityRequest(self.request_adapter, self.path_parameters)

