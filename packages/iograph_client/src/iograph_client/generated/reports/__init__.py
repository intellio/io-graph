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
	from .managed_device_enrollment_top_failures_with_period import ManagedDeviceEnrollmentTopFailuresWithPeriodRequest
	from .managed_device_enrollment_top_failures import ManagedDeviceEnrollmentTopFailuresRequest
	from .managed_device_enrollment_failure_details_with_skip_top_filter_skiptoken import ManagedDeviceEnrollmentFailureDetailsWithSkipTopFilterSkipTokenRequest
	from .managed_device_enrollment_failure_details import ManagedDeviceEnrollmentFailureDetailsRequest
	from .get_yammer_groups_activity_group_counts_with_period import GetYammerGroupsActivityGroupCountsWithPeriodRequest
	from .get_yammer_groups_activity_detail_with_period import GetYammerGroupsActivityDetailWithPeriodRequest
	from .get_yammer_groups_activity_detail_with_date import GetYammerGroupsActivityDetailWithDateRequest
	from .get_yammer_groups_activity_counts_with_period import GetYammerGroupsActivityCountsWithPeriodRequest
	from .get_yammer_device_usage_user_detail_with_period import GetYammerDeviceUsageUserDetailWithPeriodRequest
	from .get_yammer_device_usage_user_detail_with_date import GetYammerDeviceUsageUserDetailWithDateRequest
	from .get_yammer_device_usage_user_counts_with_period import GetYammerDeviceUsageUserCountsWithPeriodRequest
	from .get_yammer_device_usage_distribution_user_counts_with_period import GetYammerDeviceUsageDistributionUserCountsWithPeriodRequest
	from .get_yammer_activity_user_detail_with_period import GetYammerActivityUserDetailWithPeriodRequest
	from .get_yammer_activity_user_detail_with_date import GetYammerActivityUserDetailWithDateRequest
	from .get_yammer_activity_user_counts_with_period import GetYammerActivityUserCountsWithPeriodRequest
	from .get_yammer_activity_counts_with_period import GetYammerActivityCountsWithPeriodRequest
	from .get_user_archived_print_jobs_with_userid_startdatetime_enddatetime import GetUserArchivedPrintJobsWithUserIdStartDateTimeEndDateTimeRequest
	from .get_teams_user_activity_user_detail_with_period import GetTeamsUserActivityUserDetailWithPeriodRequest
	from .get_teams_user_activity_user_detail_with_date import GetTeamsUserActivityUserDetailWithDateRequest
	from .get_teams_user_activity_user_counts_with_period import GetTeamsUserActivityUserCountsWithPeriodRequest
	from .get_teams_user_activity_counts_with_period import GetTeamsUserActivityCountsWithPeriodRequest
	from .get_teams_team_counts_with_period import GetTeamsTeamCountsWithPeriodRequest
	from .get_teams_team_activity_distribution_counts_with_period import GetTeamsTeamActivityDistributionCountsWithPeriodRequest
	from .get_teams_team_activity_detail_with_period import GetTeamsTeamActivityDetailWithPeriodRequest
	from .get_teams_team_activity_detail_with_date import GetTeamsTeamActivityDetailWithDateRequest
	from .get_teams_team_activity_counts_with_period import GetTeamsTeamActivityCountsWithPeriodRequest
	from .get_teams_device_usage_user_detail_with_period import GetTeamsDeviceUsageUserDetailWithPeriodRequest
	from .get_teams_device_usage_user_detail_with_date import GetTeamsDeviceUsageUserDetailWithDateRequest
	from .get_teams_device_usage_user_counts_with_period import GetTeamsDeviceUsageUserCountsWithPeriodRequest
	from .get_teams_device_usage_distribution_user_counts_with_period import GetTeamsDeviceUsageDistributionUserCountsWithPeriodRequest
	from .get_skype_for_business_peer_to_peer_activity_user_counts_with_period import GetSkypeForBusinessPeerToPeerActivityUserCountsWithPeriodRequest
	from .get_skype_for_business_peer_to_peer_activity_minute_counts_with_period import GetSkypeForBusinessPeerToPeerActivityMinuteCountsWithPeriodRequest
	from .get_skype_for_business_peer_to_peer_activity_counts_with_period import GetSkypeForBusinessPeerToPeerActivityCountsWithPeriodRequest
	from .get_skype_for_business_participant_activity_user_counts_with_period import GetSkypeForBusinessParticipantActivityUserCountsWithPeriodRequest
	from .get_skype_for_business_participant_activity_minute_counts_with_period import GetSkypeForBusinessParticipantActivityMinuteCountsWithPeriodRequest
	from .get_skype_for_business_participant_activity_counts_with_period import GetSkypeForBusinessParticipantActivityCountsWithPeriodRequest
	from .get_skype_for_business_organizer_activity_user_counts_with_period import GetSkypeForBusinessOrganizerActivityUserCountsWithPeriodRequest
	from .get_skype_for_business_organizer_activity_minute_counts_with_period import GetSkypeForBusinessOrganizerActivityMinuteCountsWithPeriodRequest
	from .get_skype_for_business_organizer_activity_counts_with_period import GetSkypeForBusinessOrganizerActivityCountsWithPeriodRequest
	from .get_skype_for_business_device_usage_user_detail_with_period import GetSkypeForBusinessDeviceUsageUserDetailWithPeriodRequest
	from .get_skype_for_business_device_usage_user_detail_with_date import GetSkypeForBusinessDeviceUsageUserDetailWithDateRequest
	from .get_skype_for_business_device_usage_user_counts_with_period import GetSkypeForBusinessDeviceUsageUserCountsWithPeriodRequest
	from .get_skype_for_business_device_usage_distribution_user_counts_with_period import GetSkypeForBusinessDeviceUsageDistributionUserCountsWithPeriodRequest
	from .get_skype_for_business_activity_user_detail_with_period import GetSkypeForBusinessActivityUserDetailWithPeriodRequest
	from .get_skype_for_business_activity_user_detail_with_date import GetSkypeForBusinessActivityUserDetailWithDateRequest
	from .get_skype_for_business_activity_user_counts_with_period import GetSkypeForBusinessActivityUserCountsWithPeriodRequest
	from .get_skype_for_business_activity_counts_with_period import GetSkypeForBusinessActivityCountsWithPeriodRequest
	from .get_share_point_site_usage_storage_with_period import GetSharePointSiteUsageStorageWithPeriodRequest
	from .get_share_point_site_usage_site_counts_with_period import GetSharePointSiteUsageSiteCountsWithPeriodRequest
	from .get_share_point_site_usage_pages_with_period import GetSharePointSiteUsagePagesWithPeriodRequest
	from .get_share_point_site_usage_file_counts_with_period import GetSharePointSiteUsageFileCountsWithPeriodRequest
	from .get_share_point_site_usage_detail_with_period import GetSharePointSiteUsageDetailWithPeriodRequest
	from .get_share_point_site_usage_detail_with_date import GetSharePointSiteUsageDetailWithDateRequest
	from .get_share_point_activity_user_detail_with_period import GetSharePointActivityUserDetailWithPeriodRequest
	from .get_share_point_activity_user_detail_with_date import GetSharePointActivityUserDetailWithDateRequest
	from .get_share_point_activity_user_counts_with_period import GetSharePointActivityUserCountsWithPeriodRequest
	from .get_share_point_activity_pages_with_period import GetSharePointActivityPagesWithPeriodRequest
	from .get_share_point_activity_file_counts_with_period import GetSharePointActivityFileCountsWithPeriodRequest
	from .get_relying_party_detailed_summary_with_period import GetRelyingPartyDetailedSummaryWithPeriodRequest
	from .get_printer_archived_print_jobs_with_printerid_startdatetime_enddatetime import GetPrinterArchivedPrintJobsWithPrinterIdStartDateTimeEndDateTimeRequest
	from .get_one_drive_usage_storage_with_period import GetOneDriveUsageStorageWithPeriodRequest
	from .get_one_drive_usage_file_counts_with_period import GetOneDriveUsageFileCountsWithPeriodRequest
	from .get_one_drive_usage_account_detail_with_period import GetOneDriveUsageAccountDetailWithPeriodRequest
	from .get_one_drive_usage_account_detail_with_date import GetOneDriveUsageAccountDetailWithDateRequest
	from .get_one_drive_usage_account_counts_with_period import GetOneDriveUsageAccountCountsWithPeriodRequest
	from .get_one_drive_activity_user_detail_with_period import GetOneDriveActivityUserDetailWithPeriodRequest
	from .get_one_drive_activity_user_detail_with_date import GetOneDriveActivityUserDetailWithDateRequest
	from .get_one_drive_activity_user_counts_with_period import GetOneDriveActivityUserCountsWithPeriodRequest
	from .get_one_drive_activity_file_counts_with_period import GetOneDriveActivityFileCountsWithPeriodRequest
	from .get_office365_services_user_counts_with_period import GetOffice365ServicesUserCountsWithPeriodRequest
	from .get_office365_groups_activity_storage_with_period import GetOffice365GroupsActivityStorageWithPeriodRequest
	from .get_office365_groups_activity_group_counts_with_period import GetOffice365GroupsActivityGroupCountsWithPeriodRequest
	from .get_office365_groups_activity_file_counts_with_period import GetOffice365GroupsActivityFileCountsWithPeriodRequest
	from .get_office365_groups_activity_detail_with_period import GetOffice365GroupsActivityDetailWithPeriodRequest
	from .get_office365_groups_activity_detail_with_date import GetOffice365GroupsActivityDetailWithDateRequest
	from .get_office365_groups_activity_counts_with_period import GetOffice365GroupsActivityCountsWithPeriodRequest
	from .get_office365_active_user_detail_with_period import GetOffice365ActiveUserDetailWithPeriodRequest
	from .get_office365_active_user_detail_with_date import GetOffice365ActiveUserDetailWithDateRequest
	from .get_office365_active_user_counts_with_period import GetOffice365ActiveUserCountsWithPeriodRequest
	from .get_office365_activations_user_detail import GetOffice365ActivationsUserDetailRequest
	from .get_office365_activations_user_counts import GetOffice365ActivationsUserCountsRequest
	from .get_office365_activation_counts import GetOffice365ActivationCountsRequest
	from .get_mailbox_usage_storage_with_period import GetMailboxUsageStorageWithPeriodRequest
	from .get_mailbox_usage_quota_status_mailbox_counts_with_period import GetMailboxUsageQuotaStatusMailboxCountsWithPeriodRequest
	from .get_mailbox_usage_mailbox_counts_with_period import GetMailboxUsageMailboxCountsWithPeriodRequest
	from .get_mailbox_usage_detail_with_period import GetMailboxUsageDetailWithPeriodRequest
	from .get_m365_app_user_detail_with_period import GetM365AppUserDetailWithPeriodRequest
	from .get_m365_app_user_detail_with_date import GetM365AppUserDetailWithDateRequest
	from .get_m365_app_user_counts_with_period import GetM365AppUserCountsWithPeriodRequest
	from .get_m365_app_platform_user_counts_with_period import GetM365AppPlatformUserCountsWithPeriodRequest
	from .get_group_archived_print_jobs_with_groupid_startdatetime_enddatetime import GetGroupArchivedPrintJobsWithGroupIdStartDateTimeEndDateTimeRequest
	from .get_email_app_usage_versions_user_counts_with_period import GetEmailAppUsageVersionsUserCountsWithPeriodRequest
	from .get_email_app_usage_user_detail_with_period import GetEmailAppUsageUserDetailWithPeriodRequest
	from .get_email_app_usage_user_detail_with_date import GetEmailAppUsageUserDetailWithDateRequest
	from .get_email_app_usage_user_counts_with_period import GetEmailAppUsageUserCountsWithPeriodRequest
	from .get_email_app_usage_apps_user_counts_with_period import GetEmailAppUsageAppsUserCountsWithPeriodRequest
	from .get_email_activity_user_detail_with_period import GetEmailActivityUserDetailWithPeriodRequest
	from .get_email_activity_user_detail_with_date import GetEmailActivityUserDetailWithDateRequest
	from .get_email_activity_user_counts_with_period import GetEmailActivityUserCountsWithPeriodRequest
	from .get_email_activity_counts_with_period import GetEmailActivityCountsWithPeriodRequest
	from .device_configuration_user_activity import DeviceConfigurationUserActivityRequest
	from .device_configuration_device_activity import DeviceConfigurationDeviceActivityRequest
	from .daily_print_usage_by_user import DailyPrintUsageByUserRequest
	from .daily_print_usage_by_printer import DailyPrintUsageByPrinterRequest
	from .authentication_methods import AuthenticationMethodsRequest
	from ...request_adapter import HttpxRequestAdapter
from iograph_models.models.report_root import ReportRoot
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


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

	def get_email_activity_counts_with_period(self,
		period: str,
	) -> GetEmailActivityCountsWithPeriodRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_email_activity_counts_with_period import GetEmailActivityCountsWithPeriodRequest
		return GetEmailActivityCountsWithPeriodRequest(self.request_adapter, path_parameters)

	def get_email_activity_user_counts_with_period(self,
		period: str,
	) -> GetEmailActivityUserCountsWithPeriodRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_email_activity_user_counts_with_period import GetEmailActivityUserCountsWithPeriodRequest
		return GetEmailActivityUserCountsWithPeriodRequest(self.request_adapter, path_parameters)

	def get_email_activity_user_detail_with_date(self,
		date: str,
	) -> GetEmailActivityUserDetailWithDateRequest:
		if date is None:
			raise TypeError("date cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["date"] =  date

		from .get_email_activity_user_detail_with_date import GetEmailActivityUserDetailWithDateRequest
		return GetEmailActivityUserDetailWithDateRequest(self.request_adapter, path_parameters)

	def get_email_activity_user_detail_with_period(self,
		period: str,
	) -> GetEmailActivityUserDetailWithPeriodRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_email_activity_user_detail_with_period import GetEmailActivityUserDetailWithPeriodRequest
		return GetEmailActivityUserDetailWithPeriodRequest(self.request_adapter, path_parameters)

	def get_email_app_usage_apps_user_counts_with_period(self,
		period: str,
	) -> GetEmailAppUsageAppsUserCountsWithPeriodRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_email_app_usage_apps_user_counts_with_period import GetEmailAppUsageAppsUserCountsWithPeriodRequest
		return GetEmailAppUsageAppsUserCountsWithPeriodRequest(self.request_adapter, path_parameters)

	def get_email_app_usage_user_counts_with_period(self,
		period: str,
	) -> GetEmailAppUsageUserCountsWithPeriodRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_email_app_usage_user_counts_with_period import GetEmailAppUsageUserCountsWithPeriodRequest
		return GetEmailAppUsageUserCountsWithPeriodRequest(self.request_adapter, path_parameters)

	def get_email_app_usage_user_detail_with_date(self,
		date: str,
	) -> GetEmailAppUsageUserDetailWithDateRequest:
		if date is None:
			raise TypeError("date cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["date"] =  date

		from .get_email_app_usage_user_detail_with_date import GetEmailAppUsageUserDetailWithDateRequest
		return GetEmailAppUsageUserDetailWithDateRequest(self.request_adapter, path_parameters)

	def get_email_app_usage_user_detail_with_period(self,
		period: str,
	) -> GetEmailAppUsageUserDetailWithPeriodRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_email_app_usage_user_detail_with_period import GetEmailAppUsageUserDetailWithPeriodRequest
		return GetEmailAppUsageUserDetailWithPeriodRequest(self.request_adapter, path_parameters)

	def get_email_app_usage_versions_user_counts_with_period(self,
		period: str,
	) -> GetEmailAppUsageVersionsUserCountsWithPeriodRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_email_app_usage_versions_user_counts_with_period import GetEmailAppUsageVersionsUserCountsWithPeriodRequest
		return GetEmailAppUsageVersionsUserCountsWithPeriodRequest(self.request_adapter, path_parameters)

	def get_group_archived_print_jobs_with_groupid_startdatetime_enddatetime(self,
		groupId: str,
		startDateTime: datetime,
		endDateTime: datetime,
	) -> GetGroupArchivedPrintJobsWithGroupIdStartDateTimeEndDateTimeRequest:
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

		from .get_group_archived_print_jobs_with_groupid_startdatetime_enddatetime import GetGroupArchivedPrintJobsWithGroupIdStartDateTimeEndDateTimeRequest
		return GetGroupArchivedPrintJobsWithGroupIdStartDateTimeEndDateTimeRequest(self.request_adapter, path_parameters)

	def get_m365_app_platform_user_counts_with_period(self,
		period: str,
	) -> GetM365AppPlatformUserCountsWithPeriodRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_m365_app_platform_user_counts_with_period import GetM365AppPlatformUserCountsWithPeriodRequest
		return GetM365AppPlatformUserCountsWithPeriodRequest(self.request_adapter, path_parameters)

	def get_m365_app_user_counts_with_period(self,
		period: str,
	) -> GetM365AppUserCountsWithPeriodRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_m365_app_user_counts_with_period import GetM365AppUserCountsWithPeriodRequest
		return GetM365AppUserCountsWithPeriodRequest(self.request_adapter, path_parameters)

	def get_m365_app_user_detail_with_date(self,
		date: str,
	) -> GetM365AppUserDetailWithDateRequest:
		if date is None:
			raise TypeError("date cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["date"] =  date

		from .get_m365_app_user_detail_with_date import GetM365AppUserDetailWithDateRequest
		return GetM365AppUserDetailWithDateRequest(self.request_adapter, path_parameters)

	def get_m365_app_user_detail_with_period(self,
		period: str,
	) -> GetM365AppUserDetailWithPeriodRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_m365_app_user_detail_with_period import GetM365AppUserDetailWithPeriodRequest
		return GetM365AppUserDetailWithPeriodRequest(self.request_adapter, path_parameters)

	def get_mailbox_usage_detail_with_period(self,
		period: str,
	) -> GetMailboxUsageDetailWithPeriodRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_mailbox_usage_detail_with_period import GetMailboxUsageDetailWithPeriodRequest
		return GetMailboxUsageDetailWithPeriodRequest(self.request_adapter, path_parameters)

	def get_mailbox_usage_mailbox_counts_with_period(self,
		period: str,
	) -> GetMailboxUsageMailboxCountsWithPeriodRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_mailbox_usage_mailbox_counts_with_period import GetMailboxUsageMailboxCountsWithPeriodRequest
		return GetMailboxUsageMailboxCountsWithPeriodRequest(self.request_adapter, path_parameters)

	def get_mailbox_usage_quota_status_mailbox_counts_with_period(self,
		period: str,
	) -> GetMailboxUsageQuotaStatusMailboxCountsWithPeriodRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_mailbox_usage_quota_status_mailbox_counts_with_period import GetMailboxUsageQuotaStatusMailboxCountsWithPeriodRequest
		return GetMailboxUsageQuotaStatusMailboxCountsWithPeriodRequest(self.request_adapter, path_parameters)

	def get_mailbox_usage_storage_with_period(self,
		period: str,
	) -> GetMailboxUsageStorageWithPeriodRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_mailbox_usage_storage_with_period import GetMailboxUsageStorageWithPeriodRequest
		return GetMailboxUsageStorageWithPeriodRequest(self.request_adapter, path_parameters)

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

	def get_office365_active_user_counts_with_period(self,
		period: str,
	) -> GetOffice365ActiveUserCountsWithPeriodRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_office365_active_user_counts_with_period import GetOffice365ActiveUserCountsWithPeriodRequest
		return GetOffice365ActiveUserCountsWithPeriodRequest(self.request_adapter, path_parameters)

	def get_office365_active_user_detail_with_date(self,
		date: str,
	) -> GetOffice365ActiveUserDetailWithDateRequest:
		if date is None:
			raise TypeError("date cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["date"] =  date

		from .get_office365_active_user_detail_with_date import GetOffice365ActiveUserDetailWithDateRequest
		return GetOffice365ActiveUserDetailWithDateRequest(self.request_adapter, path_parameters)

	def get_office365_active_user_detail_with_period(self,
		period: str,
	) -> GetOffice365ActiveUserDetailWithPeriodRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_office365_active_user_detail_with_period import GetOffice365ActiveUserDetailWithPeriodRequest
		return GetOffice365ActiveUserDetailWithPeriodRequest(self.request_adapter, path_parameters)

	def get_office365_groups_activity_counts_with_period(self,
		period: str,
	) -> GetOffice365GroupsActivityCountsWithPeriodRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_office365_groups_activity_counts_with_period import GetOffice365GroupsActivityCountsWithPeriodRequest
		return GetOffice365GroupsActivityCountsWithPeriodRequest(self.request_adapter, path_parameters)

	def get_office365_groups_activity_detail_with_date(self,
		date: str,
	) -> GetOffice365GroupsActivityDetailWithDateRequest:
		if date is None:
			raise TypeError("date cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["date"] =  date

		from .get_office365_groups_activity_detail_with_date import GetOffice365GroupsActivityDetailWithDateRequest
		return GetOffice365GroupsActivityDetailWithDateRequest(self.request_adapter, path_parameters)

	def get_office365_groups_activity_detail_with_period(self,
		period: str,
	) -> GetOffice365GroupsActivityDetailWithPeriodRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_office365_groups_activity_detail_with_period import GetOffice365GroupsActivityDetailWithPeriodRequest
		return GetOffice365GroupsActivityDetailWithPeriodRequest(self.request_adapter, path_parameters)

	def get_office365_groups_activity_file_counts_with_period(self,
		period: str,
	) -> GetOffice365GroupsActivityFileCountsWithPeriodRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_office365_groups_activity_file_counts_with_period import GetOffice365GroupsActivityFileCountsWithPeriodRequest
		return GetOffice365GroupsActivityFileCountsWithPeriodRequest(self.request_adapter, path_parameters)

	def get_office365_groups_activity_group_counts_with_period(self,
		period: str,
	) -> GetOffice365GroupsActivityGroupCountsWithPeriodRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_office365_groups_activity_group_counts_with_period import GetOffice365GroupsActivityGroupCountsWithPeriodRequest
		return GetOffice365GroupsActivityGroupCountsWithPeriodRequest(self.request_adapter, path_parameters)

	def get_office365_groups_activity_storage_with_period(self,
		period: str,
	) -> GetOffice365GroupsActivityStorageWithPeriodRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_office365_groups_activity_storage_with_period import GetOffice365GroupsActivityStorageWithPeriodRequest
		return GetOffice365GroupsActivityStorageWithPeriodRequest(self.request_adapter, path_parameters)

	def get_office365_services_user_counts_with_period(self,
		period: str,
	) -> GetOffice365ServicesUserCountsWithPeriodRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_office365_services_user_counts_with_period import GetOffice365ServicesUserCountsWithPeriodRequest
		return GetOffice365ServicesUserCountsWithPeriodRequest(self.request_adapter, path_parameters)

	def get_one_drive_activity_file_counts_with_period(self,
		period: str,
	) -> GetOneDriveActivityFileCountsWithPeriodRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_one_drive_activity_file_counts_with_period import GetOneDriveActivityFileCountsWithPeriodRequest
		return GetOneDriveActivityFileCountsWithPeriodRequest(self.request_adapter, path_parameters)

	def get_one_drive_activity_user_counts_with_period(self,
		period: str,
	) -> GetOneDriveActivityUserCountsWithPeriodRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_one_drive_activity_user_counts_with_period import GetOneDriveActivityUserCountsWithPeriodRequest
		return GetOneDriveActivityUserCountsWithPeriodRequest(self.request_adapter, path_parameters)

	def get_one_drive_activity_user_detail_with_date(self,
		date: str,
	) -> GetOneDriveActivityUserDetailWithDateRequest:
		if date is None:
			raise TypeError("date cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["date"] =  date

		from .get_one_drive_activity_user_detail_with_date import GetOneDriveActivityUserDetailWithDateRequest
		return GetOneDriveActivityUserDetailWithDateRequest(self.request_adapter, path_parameters)

	def get_one_drive_activity_user_detail_with_period(self,
		period: str,
	) -> GetOneDriveActivityUserDetailWithPeriodRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_one_drive_activity_user_detail_with_period import GetOneDriveActivityUserDetailWithPeriodRequest
		return GetOneDriveActivityUserDetailWithPeriodRequest(self.request_adapter, path_parameters)

	def get_one_drive_usage_account_counts_with_period(self,
		period: str,
	) -> GetOneDriveUsageAccountCountsWithPeriodRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_one_drive_usage_account_counts_with_period import GetOneDriveUsageAccountCountsWithPeriodRequest
		return GetOneDriveUsageAccountCountsWithPeriodRequest(self.request_adapter, path_parameters)

	def get_one_drive_usage_account_detail_with_date(self,
		date: str,
	) -> GetOneDriveUsageAccountDetailWithDateRequest:
		if date is None:
			raise TypeError("date cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["date"] =  date

		from .get_one_drive_usage_account_detail_with_date import GetOneDriveUsageAccountDetailWithDateRequest
		return GetOneDriveUsageAccountDetailWithDateRequest(self.request_adapter, path_parameters)

	def get_one_drive_usage_account_detail_with_period(self,
		period: str,
	) -> GetOneDriveUsageAccountDetailWithPeriodRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_one_drive_usage_account_detail_with_period import GetOneDriveUsageAccountDetailWithPeriodRequest
		return GetOneDriveUsageAccountDetailWithPeriodRequest(self.request_adapter, path_parameters)

	def get_one_drive_usage_file_counts_with_period(self,
		period: str,
	) -> GetOneDriveUsageFileCountsWithPeriodRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_one_drive_usage_file_counts_with_period import GetOneDriveUsageFileCountsWithPeriodRequest
		return GetOneDriveUsageFileCountsWithPeriodRequest(self.request_adapter, path_parameters)

	def get_one_drive_usage_storage_with_period(self,
		period: str,
	) -> GetOneDriveUsageStorageWithPeriodRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_one_drive_usage_storage_with_period import GetOneDriveUsageStorageWithPeriodRequest
		return GetOneDriveUsageStorageWithPeriodRequest(self.request_adapter, path_parameters)

	def get_printer_archived_print_jobs_with_printerid_startdatetime_enddatetime(self,
		printerId: str,
		startDateTime: datetime,
		endDateTime: datetime,
	) -> GetPrinterArchivedPrintJobsWithPrinterIdStartDateTimeEndDateTimeRequest:
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

		from .get_printer_archived_print_jobs_with_printerid_startdatetime_enddatetime import GetPrinterArchivedPrintJobsWithPrinterIdStartDateTimeEndDateTimeRequest
		return GetPrinterArchivedPrintJobsWithPrinterIdStartDateTimeEndDateTimeRequest(self.request_adapter, path_parameters)

	def get_relying_party_detailed_summary_with_period(self,
		period: str,
	) -> GetRelyingPartyDetailedSummaryWithPeriodRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_relying_party_detailed_summary_with_period import GetRelyingPartyDetailedSummaryWithPeriodRequest
		return GetRelyingPartyDetailedSummaryWithPeriodRequest(self.request_adapter, path_parameters)

	def get_share_point_activity_file_counts_with_period(self,
		period: str,
	) -> GetSharePointActivityFileCountsWithPeriodRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_share_point_activity_file_counts_with_period import GetSharePointActivityFileCountsWithPeriodRequest
		return GetSharePointActivityFileCountsWithPeriodRequest(self.request_adapter, path_parameters)

	def get_share_point_activity_pages_with_period(self,
		period: str,
	) -> GetSharePointActivityPagesWithPeriodRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_share_point_activity_pages_with_period import GetSharePointActivityPagesWithPeriodRequest
		return GetSharePointActivityPagesWithPeriodRequest(self.request_adapter, path_parameters)

	def get_share_point_activity_user_counts_with_period(self,
		period: str,
	) -> GetSharePointActivityUserCountsWithPeriodRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_share_point_activity_user_counts_with_period import GetSharePointActivityUserCountsWithPeriodRequest
		return GetSharePointActivityUserCountsWithPeriodRequest(self.request_adapter, path_parameters)

	def get_share_point_activity_user_detail_with_date(self,
		date: str,
	) -> GetSharePointActivityUserDetailWithDateRequest:
		if date is None:
			raise TypeError("date cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["date"] =  date

		from .get_share_point_activity_user_detail_with_date import GetSharePointActivityUserDetailWithDateRequest
		return GetSharePointActivityUserDetailWithDateRequest(self.request_adapter, path_parameters)

	def get_share_point_activity_user_detail_with_period(self,
		period: str,
	) -> GetSharePointActivityUserDetailWithPeriodRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_share_point_activity_user_detail_with_period import GetSharePointActivityUserDetailWithPeriodRequest
		return GetSharePointActivityUserDetailWithPeriodRequest(self.request_adapter, path_parameters)

	def get_share_point_site_usage_detail_with_date(self,
		date: str,
	) -> GetSharePointSiteUsageDetailWithDateRequest:
		if date is None:
			raise TypeError("date cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["date"] =  date

		from .get_share_point_site_usage_detail_with_date import GetSharePointSiteUsageDetailWithDateRequest
		return GetSharePointSiteUsageDetailWithDateRequest(self.request_adapter, path_parameters)

	def get_share_point_site_usage_detail_with_period(self,
		period: str,
	) -> GetSharePointSiteUsageDetailWithPeriodRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_share_point_site_usage_detail_with_period import GetSharePointSiteUsageDetailWithPeriodRequest
		return GetSharePointSiteUsageDetailWithPeriodRequest(self.request_adapter, path_parameters)

	def get_share_point_site_usage_file_counts_with_period(self,
		period: str,
	) -> GetSharePointSiteUsageFileCountsWithPeriodRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_share_point_site_usage_file_counts_with_period import GetSharePointSiteUsageFileCountsWithPeriodRequest
		return GetSharePointSiteUsageFileCountsWithPeriodRequest(self.request_adapter, path_parameters)

	def get_share_point_site_usage_pages_with_period(self,
		period: str,
	) -> GetSharePointSiteUsagePagesWithPeriodRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_share_point_site_usage_pages_with_period import GetSharePointSiteUsagePagesWithPeriodRequest
		return GetSharePointSiteUsagePagesWithPeriodRequest(self.request_adapter, path_parameters)

	def get_share_point_site_usage_site_counts_with_period(self,
		period: str,
	) -> GetSharePointSiteUsageSiteCountsWithPeriodRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_share_point_site_usage_site_counts_with_period import GetSharePointSiteUsageSiteCountsWithPeriodRequest
		return GetSharePointSiteUsageSiteCountsWithPeriodRequest(self.request_adapter, path_parameters)

	def get_share_point_site_usage_storage_with_period(self,
		period: str,
	) -> GetSharePointSiteUsageStorageWithPeriodRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_share_point_site_usage_storage_with_period import GetSharePointSiteUsageStorageWithPeriodRequest
		return GetSharePointSiteUsageStorageWithPeriodRequest(self.request_adapter, path_parameters)

	def get_skype_for_business_activity_counts_with_period(self,
		period: str,
	) -> GetSkypeForBusinessActivityCountsWithPeriodRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_skype_for_business_activity_counts_with_period import GetSkypeForBusinessActivityCountsWithPeriodRequest
		return GetSkypeForBusinessActivityCountsWithPeriodRequest(self.request_adapter, path_parameters)

	def get_skype_for_business_activity_user_counts_with_period(self,
		period: str,
	) -> GetSkypeForBusinessActivityUserCountsWithPeriodRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_skype_for_business_activity_user_counts_with_period import GetSkypeForBusinessActivityUserCountsWithPeriodRequest
		return GetSkypeForBusinessActivityUserCountsWithPeriodRequest(self.request_adapter, path_parameters)

	def get_skype_for_business_activity_user_detail_with_date(self,
		date: str,
	) -> GetSkypeForBusinessActivityUserDetailWithDateRequest:
		if date is None:
			raise TypeError("date cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["date"] =  date

		from .get_skype_for_business_activity_user_detail_with_date import GetSkypeForBusinessActivityUserDetailWithDateRequest
		return GetSkypeForBusinessActivityUserDetailWithDateRequest(self.request_adapter, path_parameters)

	def get_skype_for_business_activity_user_detail_with_period(self,
		period: str,
	) -> GetSkypeForBusinessActivityUserDetailWithPeriodRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_skype_for_business_activity_user_detail_with_period import GetSkypeForBusinessActivityUserDetailWithPeriodRequest
		return GetSkypeForBusinessActivityUserDetailWithPeriodRequest(self.request_adapter, path_parameters)

	def get_skype_for_business_device_usage_distribution_user_counts_with_period(self,
		period: str,
	) -> GetSkypeForBusinessDeviceUsageDistributionUserCountsWithPeriodRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_skype_for_business_device_usage_distribution_user_counts_with_period import GetSkypeForBusinessDeviceUsageDistributionUserCountsWithPeriodRequest
		return GetSkypeForBusinessDeviceUsageDistributionUserCountsWithPeriodRequest(self.request_adapter, path_parameters)

	def get_skype_for_business_device_usage_user_counts_with_period(self,
		period: str,
	) -> GetSkypeForBusinessDeviceUsageUserCountsWithPeriodRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_skype_for_business_device_usage_user_counts_with_period import GetSkypeForBusinessDeviceUsageUserCountsWithPeriodRequest
		return GetSkypeForBusinessDeviceUsageUserCountsWithPeriodRequest(self.request_adapter, path_parameters)

	def get_skype_for_business_device_usage_user_detail_with_date(self,
		date: str,
	) -> GetSkypeForBusinessDeviceUsageUserDetailWithDateRequest:
		if date is None:
			raise TypeError("date cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["date"] =  date

		from .get_skype_for_business_device_usage_user_detail_with_date import GetSkypeForBusinessDeviceUsageUserDetailWithDateRequest
		return GetSkypeForBusinessDeviceUsageUserDetailWithDateRequest(self.request_adapter, path_parameters)

	def get_skype_for_business_device_usage_user_detail_with_period(self,
		period: str,
	) -> GetSkypeForBusinessDeviceUsageUserDetailWithPeriodRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_skype_for_business_device_usage_user_detail_with_period import GetSkypeForBusinessDeviceUsageUserDetailWithPeriodRequest
		return GetSkypeForBusinessDeviceUsageUserDetailWithPeriodRequest(self.request_adapter, path_parameters)

	def get_skype_for_business_organizer_activity_counts_with_period(self,
		period: str,
	) -> GetSkypeForBusinessOrganizerActivityCountsWithPeriodRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_skype_for_business_organizer_activity_counts_with_period import GetSkypeForBusinessOrganizerActivityCountsWithPeriodRequest
		return GetSkypeForBusinessOrganizerActivityCountsWithPeriodRequest(self.request_adapter, path_parameters)

	def get_skype_for_business_organizer_activity_minute_counts_with_period(self,
		period: str,
	) -> GetSkypeForBusinessOrganizerActivityMinuteCountsWithPeriodRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_skype_for_business_organizer_activity_minute_counts_with_period import GetSkypeForBusinessOrganizerActivityMinuteCountsWithPeriodRequest
		return GetSkypeForBusinessOrganizerActivityMinuteCountsWithPeriodRequest(self.request_adapter, path_parameters)

	def get_skype_for_business_organizer_activity_user_counts_with_period(self,
		period: str,
	) -> GetSkypeForBusinessOrganizerActivityUserCountsWithPeriodRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_skype_for_business_organizer_activity_user_counts_with_period import GetSkypeForBusinessOrganizerActivityUserCountsWithPeriodRequest
		return GetSkypeForBusinessOrganizerActivityUserCountsWithPeriodRequest(self.request_adapter, path_parameters)

	def get_skype_for_business_participant_activity_counts_with_period(self,
		period: str,
	) -> GetSkypeForBusinessParticipantActivityCountsWithPeriodRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_skype_for_business_participant_activity_counts_with_period import GetSkypeForBusinessParticipantActivityCountsWithPeriodRequest
		return GetSkypeForBusinessParticipantActivityCountsWithPeriodRequest(self.request_adapter, path_parameters)

	def get_skype_for_business_participant_activity_minute_counts_with_period(self,
		period: str,
	) -> GetSkypeForBusinessParticipantActivityMinuteCountsWithPeriodRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_skype_for_business_participant_activity_minute_counts_with_period import GetSkypeForBusinessParticipantActivityMinuteCountsWithPeriodRequest
		return GetSkypeForBusinessParticipantActivityMinuteCountsWithPeriodRequest(self.request_adapter, path_parameters)

	def get_skype_for_business_participant_activity_user_counts_with_period(self,
		period: str,
	) -> GetSkypeForBusinessParticipantActivityUserCountsWithPeriodRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_skype_for_business_participant_activity_user_counts_with_period import GetSkypeForBusinessParticipantActivityUserCountsWithPeriodRequest
		return GetSkypeForBusinessParticipantActivityUserCountsWithPeriodRequest(self.request_adapter, path_parameters)

	def get_skype_for_business_peer_to_peer_activity_counts_with_period(self,
		period: str,
	) -> GetSkypeForBusinessPeerToPeerActivityCountsWithPeriodRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_skype_for_business_peer_to_peer_activity_counts_with_period import GetSkypeForBusinessPeerToPeerActivityCountsWithPeriodRequest
		return GetSkypeForBusinessPeerToPeerActivityCountsWithPeriodRequest(self.request_adapter, path_parameters)

	def get_skype_for_business_peer_to_peer_activity_minute_counts_with_period(self,
		period: str,
	) -> GetSkypeForBusinessPeerToPeerActivityMinuteCountsWithPeriodRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_skype_for_business_peer_to_peer_activity_minute_counts_with_period import GetSkypeForBusinessPeerToPeerActivityMinuteCountsWithPeriodRequest
		return GetSkypeForBusinessPeerToPeerActivityMinuteCountsWithPeriodRequest(self.request_adapter, path_parameters)

	def get_skype_for_business_peer_to_peer_activity_user_counts_with_period(self,
		period: str,
	) -> GetSkypeForBusinessPeerToPeerActivityUserCountsWithPeriodRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_skype_for_business_peer_to_peer_activity_user_counts_with_period import GetSkypeForBusinessPeerToPeerActivityUserCountsWithPeriodRequest
		return GetSkypeForBusinessPeerToPeerActivityUserCountsWithPeriodRequest(self.request_adapter, path_parameters)

	def get_teams_device_usage_distribution_user_counts_with_period(self,
		period: str,
	) -> GetTeamsDeviceUsageDistributionUserCountsWithPeriodRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_teams_device_usage_distribution_user_counts_with_period import GetTeamsDeviceUsageDistributionUserCountsWithPeriodRequest
		return GetTeamsDeviceUsageDistributionUserCountsWithPeriodRequest(self.request_adapter, path_parameters)

	def get_teams_device_usage_user_counts_with_period(self,
		period: str,
	) -> GetTeamsDeviceUsageUserCountsWithPeriodRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_teams_device_usage_user_counts_with_period import GetTeamsDeviceUsageUserCountsWithPeriodRequest
		return GetTeamsDeviceUsageUserCountsWithPeriodRequest(self.request_adapter, path_parameters)

	def get_teams_device_usage_user_detail_with_date(self,
		date: str,
	) -> GetTeamsDeviceUsageUserDetailWithDateRequest:
		if date is None:
			raise TypeError("date cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["date"] =  date

		from .get_teams_device_usage_user_detail_with_date import GetTeamsDeviceUsageUserDetailWithDateRequest
		return GetTeamsDeviceUsageUserDetailWithDateRequest(self.request_adapter, path_parameters)

	def get_teams_device_usage_user_detail_with_period(self,
		period: str,
	) -> GetTeamsDeviceUsageUserDetailWithPeriodRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_teams_device_usage_user_detail_with_period import GetTeamsDeviceUsageUserDetailWithPeriodRequest
		return GetTeamsDeviceUsageUserDetailWithPeriodRequest(self.request_adapter, path_parameters)

	def get_teams_team_activity_counts_with_period(self,
		period: str,
	) -> GetTeamsTeamActivityCountsWithPeriodRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_teams_team_activity_counts_with_period import GetTeamsTeamActivityCountsWithPeriodRequest
		return GetTeamsTeamActivityCountsWithPeriodRequest(self.request_adapter, path_parameters)

	def get_teams_team_activity_detail_with_date(self,
		date: str,
	) -> GetTeamsTeamActivityDetailWithDateRequest:
		if date is None:
			raise TypeError("date cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["date"] =  date

		from .get_teams_team_activity_detail_with_date import GetTeamsTeamActivityDetailWithDateRequest
		return GetTeamsTeamActivityDetailWithDateRequest(self.request_adapter, path_parameters)

	def get_teams_team_activity_detail_with_period(self,
		period: str,
	) -> GetTeamsTeamActivityDetailWithPeriodRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_teams_team_activity_detail_with_period import GetTeamsTeamActivityDetailWithPeriodRequest
		return GetTeamsTeamActivityDetailWithPeriodRequest(self.request_adapter, path_parameters)

	def get_teams_team_activity_distribution_counts_with_period(self,
		period: str,
	) -> GetTeamsTeamActivityDistributionCountsWithPeriodRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_teams_team_activity_distribution_counts_with_period import GetTeamsTeamActivityDistributionCountsWithPeriodRequest
		return GetTeamsTeamActivityDistributionCountsWithPeriodRequest(self.request_adapter, path_parameters)

	def get_teams_team_counts_with_period(self,
		period: str,
	) -> GetTeamsTeamCountsWithPeriodRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_teams_team_counts_with_period import GetTeamsTeamCountsWithPeriodRequest
		return GetTeamsTeamCountsWithPeriodRequest(self.request_adapter, path_parameters)

	def get_teams_user_activity_counts_with_period(self,
		period: str,
	) -> GetTeamsUserActivityCountsWithPeriodRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_teams_user_activity_counts_with_period import GetTeamsUserActivityCountsWithPeriodRequest
		return GetTeamsUserActivityCountsWithPeriodRequest(self.request_adapter, path_parameters)

	def get_teams_user_activity_user_counts_with_period(self,
		period: str,
	) -> GetTeamsUserActivityUserCountsWithPeriodRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_teams_user_activity_user_counts_with_period import GetTeamsUserActivityUserCountsWithPeriodRequest
		return GetTeamsUserActivityUserCountsWithPeriodRequest(self.request_adapter, path_parameters)

	def get_teams_user_activity_user_detail_with_date(self,
		date: str,
	) -> GetTeamsUserActivityUserDetailWithDateRequest:
		if date is None:
			raise TypeError("date cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["date"] =  date

		from .get_teams_user_activity_user_detail_with_date import GetTeamsUserActivityUserDetailWithDateRequest
		return GetTeamsUserActivityUserDetailWithDateRequest(self.request_adapter, path_parameters)

	def get_teams_user_activity_user_detail_with_period(self,
		period: str,
	) -> GetTeamsUserActivityUserDetailWithPeriodRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_teams_user_activity_user_detail_with_period import GetTeamsUserActivityUserDetailWithPeriodRequest
		return GetTeamsUserActivityUserDetailWithPeriodRequest(self.request_adapter, path_parameters)

	def get_user_archived_print_jobs_with_userid_startdatetime_enddatetime(self,
		userId: str,
		startDateTime: datetime,
		endDateTime: datetime,
	) -> GetUserArchivedPrintJobsWithUserIdStartDateTimeEndDateTimeRequest:
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

		from .get_user_archived_print_jobs_with_userid_startdatetime_enddatetime import GetUserArchivedPrintJobsWithUserIdStartDateTimeEndDateTimeRequest
		return GetUserArchivedPrintJobsWithUserIdStartDateTimeEndDateTimeRequest(self.request_adapter, path_parameters)

	def get_yammer_activity_counts_with_period(self,
		period: str,
	) -> GetYammerActivityCountsWithPeriodRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_yammer_activity_counts_with_period import GetYammerActivityCountsWithPeriodRequest
		return GetYammerActivityCountsWithPeriodRequest(self.request_adapter, path_parameters)

	def get_yammer_activity_user_counts_with_period(self,
		period: str,
	) -> GetYammerActivityUserCountsWithPeriodRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_yammer_activity_user_counts_with_period import GetYammerActivityUserCountsWithPeriodRequest
		return GetYammerActivityUserCountsWithPeriodRequest(self.request_adapter, path_parameters)

	def get_yammer_activity_user_detail_with_date(self,
		date: str,
	) -> GetYammerActivityUserDetailWithDateRequest:
		if date is None:
			raise TypeError("date cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["date"] =  date

		from .get_yammer_activity_user_detail_with_date import GetYammerActivityUserDetailWithDateRequest
		return GetYammerActivityUserDetailWithDateRequest(self.request_adapter, path_parameters)

	def get_yammer_activity_user_detail_with_period(self,
		period: str,
	) -> GetYammerActivityUserDetailWithPeriodRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_yammer_activity_user_detail_with_period import GetYammerActivityUserDetailWithPeriodRequest
		return GetYammerActivityUserDetailWithPeriodRequest(self.request_adapter, path_parameters)

	def get_yammer_device_usage_distribution_user_counts_with_period(self,
		period: str,
	) -> GetYammerDeviceUsageDistributionUserCountsWithPeriodRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_yammer_device_usage_distribution_user_counts_with_period import GetYammerDeviceUsageDistributionUserCountsWithPeriodRequest
		return GetYammerDeviceUsageDistributionUserCountsWithPeriodRequest(self.request_adapter, path_parameters)

	def get_yammer_device_usage_user_counts_with_period(self,
		period: str,
	) -> GetYammerDeviceUsageUserCountsWithPeriodRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_yammer_device_usage_user_counts_with_period import GetYammerDeviceUsageUserCountsWithPeriodRequest
		return GetYammerDeviceUsageUserCountsWithPeriodRequest(self.request_adapter, path_parameters)

	def get_yammer_device_usage_user_detail_with_date(self,
		date: str,
	) -> GetYammerDeviceUsageUserDetailWithDateRequest:
		if date is None:
			raise TypeError("date cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["date"] =  date

		from .get_yammer_device_usage_user_detail_with_date import GetYammerDeviceUsageUserDetailWithDateRequest
		return GetYammerDeviceUsageUserDetailWithDateRequest(self.request_adapter, path_parameters)

	def get_yammer_device_usage_user_detail_with_period(self,
		period: str,
	) -> GetYammerDeviceUsageUserDetailWithPeriodRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_yammer_device_usage_user_detail_with_period import GetYammerDeviceUsageUserDetailWithPeriodRequest
		return GetYammerDeviceUsageUserDetailWithPeriodRequest(self.request_adapter, path_parameters)

	def get_yammer_groups_activity_counts_with_period(self,
		period: str,
	) -> GetYammerGroupsActivityCountsWithPeriodRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_yammer_groups_activity_counts_with_period import GetYammerGroupsActivityCountsWithPeriodRequest
		return GetYammerGroupsActivityCountsWithPeriodRequest(self.request_adapter, path_parameters)

	def get_yammer_groups_activity_detail_with_date(self,
		date: str,
	) -> GetYammerGroupsActivityDetailWithDateRequest:
		if date is None:
			raise TypeError("date cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["date"] =  date

		from .get_yammer_groups_activity_detail_with_date import GetYammerGroupsActivityDetailWithDateRequest
		return GetYammerGroupsActivityDetailWithDateRequest(self.request_adapter, path_parameters)

	def get_yammer_groups_activity_detail_with_period(self,
		period: str,
	) -> GetYammerGroupsActivityDetailWithPeriodRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_yammer_groups_activity_detail_with_period import GetYammerGroupsActivityDetailWithPeriodRequest
		return GetYammerGroupsActivityDetailWithPeriodRequest(self.request_adapter, path_parameters)

	def get_yammer_groups_activity_group_counts_with_period(self,
		period: str,
	) -> GetYammerGroupsActivityGroupCountsWithPeriodRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .get_yammer_groups_activity_group_counts_with_period import GetYammerGroupsActivityGroupCountsWithPeriodRequest
		return GetYammerGroupsActivityGroupCountsWithPeriodRequest(self.request_adapter, path_parameters)

	@property
	def managed_device_enrollment_failure_details(self,
	) -> ManagedDeviceEnrollmentFailureDetailsRequest:
		from .managed_device_enrollment_failure_details import ManagedDeviceEnrollmentFailureDetailsRequest
		return ManagedDeviceEnrollmentFailureDetailsRequest(self.request_adapter, self.path_parameters)

	def managed_device_enrollment_failure_details_with_skip_top_filter_skiptoken(self,
		skip: int,
		top: int,
		filter: str,
		skipToken: str,
	) -> ManagedDeviceEnrollmentFailureDetailsWithSkipTopFilterSkipTokenRequest:
		if skip is None:
			raise TypeError("skip cannot be null.")
		if top is None:
			raise TypeError("top cannot be null.")
		if filter is None:
			raise TypeError("filter cannot be null.")
		if skipToken is None:
			raise TypeError("skipToken cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["skip"] =  skip
		path_parameters["top"] =  top
		path_parameters["filter"] =  filter
		path_parameters["skipToken"] =  skipToken

		from .managed_device_enrollment_failure_details_with_skip_top_filter_skiptoken import ManagedDeviceEnrollmentFailureDetailsWithSkipTopFilterSkipTokenRequest
		return ManagedDeviceEnrollmentFailureDetailsWithSkipTopFilterSkipTokenRequest(self.request_adapter, path_parameters)

	@property
	def managed_device_enrollment_top_failures(self,
	) -> ManagedDeviceEnrollmentTopFailuresRequest:
		from .managed_device_enrollment_top_failures import ManagedDeviceEnrollmentTopFailuresRequest
		return ManagedDeviceEnrollmentTopFailuresRequest(self.request_adapter, self.path_parameters)

	def managed_device_enrollment_top_failures_with_period(self,
		period: str,
	) -> ManagedDeviceEnrollmentTopFailuresWithPeriodRequest:
		if period is None:
			raise TypeError("period cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["period"] =  period

		from .managed_device_enrollment_top_failures_with_period import ManagedDeviceEnrollmentTopFailuresWithPeriodRequest
		return ManagedDeviceEnrollmentTopFailuresWithPeriodRequest(self.request_adapter, path_parameters)

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

