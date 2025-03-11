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
	from .retrieve_win32_catalog_apps_update_report import RetrieveWin32CatalogAppsUpdateReportRequest
	from .retrieve_security_task_apps_report import RetrieveSecurityTaskAppsReportRequest
	from .retrieve_device_app_installation_status_report import RetrieveDeviceAppInstallationStatusReportRequest
	from .retrieve_cloud_pki_leaf_certificate_summary_report import RetrieveCloudPkiLeafCertificateSummaryReportRequest
	from .retrieve_cloud_pki_leaf_certificate_report import RetrieveCloudPkiLeafCertificateReportRequest
	from .get_zebra_fota_deployment_report import GetZebraFotaDeploymentReportRequest
	from .get_windows_update_alert_summary_report import GetWindowsUpdateAlertSummaryReportRequest
	from .get_windows_update_alerts_per_policy_per_device_report import GetWindowsUpdateAlertsPerPolicyPerDeviceReportRequest
	from .get_windows_quality_update_alert_summary_report import GetWindowsQualityUpdateAlertSummaryReportRequest
	from .get_windows_quality_update_alerts_per_policy_per_device_report import GetWindowsQualityUpdateAlertsPerPolicyPerDeviceReportRequest
	from .get_windows_driver_update_alert_summary_report import GetWindowsDriverUpdateAlertSummaryReportRequest
	from .get_windows_driver_update_alerts_per_policy_per_device_report import GetWindowsDriverUpdateAlertsPerPolicyPerDeviceReportRequest
	from .get_user_install_status_report import GetUserInstallStatusReportRequest
	from .get_unhealthy_firewall_summary_report import GetUnhealthyFirewallSummaryReportRequest
	from .get_unhealthy_firewall_report import GetUnhealthyFirewallReportRequest
	from .get_unhealthy_defender_agents_report import GetUnhealthyDefenderAgentsReportRequest
	from .get_setting_non_compliance_report import GetSettingNonComplianceReportRequest
	from .get_report_filters import GetReportFiltersRequest
	from .get_remote_assistance_sessions_report import GetRemoteAssistanceSessionsReportRequest
	from .get_related_apps_status_report import GetRelatedAppsStatusReportRequest
	from .get_quiet_time_policy_user_summary_report import GetQuietTimePolicyUserSummaryReportRequest
	from .get_quiet_time_policy_users_report import GetQuietTimePolicyUsersReportRequest
	from .get_policy_non_compliance_summary_report import GetPolicyNonComplianceSummaryReportRequest
	from .get_policy_non_compliance_report import GetPolicyNonComplianceReportRequest
	from .get_policy_non_compliance_metadata import GetPolicyNonComplianceMetadataRequest
	from .get_noncompliant_devices_and_settings_report import GetNoncompliantDevicesAndSettingsReportRequest
	from .get_mobile_application_management_app_registration_summary_report import GetMobileApplicationManagementAppRegistrationSummaryReportRequest
	from .get_mobile_application_management_app_configuration_report import GetMobileApplicationManagementAppConfigurationReportRequest
	from .get_malware_summary_report import GetMalwareSummaryReportRequest
	from .get_historical_report import GetHistoricalReportRequest
	from .get_group_policy_settings_device_settings_report import GetGroupPolicySettingsDeviceSettingsReportRequest
	from .get_failed_mobile_apps_summary_report import GetFailedMobileAppsSummaryReportRequest
	from .get_failed_mobile_apps_report import GetFailedMobileAppsReportRequest
	from .get_enrollment_configuration_policies_by_device import GetEnrollmentConfigurationPoliciesByDeviceRequest
	from .get_encryption_report_for_devices import GetEncryptionReportForDevicesRequest
	from .get_devices_without_compliance_policy_report import GetDevicesWithoutCompliancePolicyReportRequest
	from .get_device_status_summary_by_compliance_policy_settings_report import GetDeviceStatusSummaryByCompliancePolicySettingsReportRequest
	from .get_device_status_summary_by_compliace_policy_report import GetDeviceStatusSummaryByCompliacePolicyReportRequest
	from .get_device_status_by_compliance_policy_setting_report import GetDeviceStatusByCompliancePolicySettingReportRequest
	from .get_device_status_by_compliace_policy_report import GetDeviceStatusByCompliacePolicyReportRequest
	from .get_devices_status_by_setting_report import GetDevicesStatusBySettingReportRequest
	from .get_devices_status_by_policy_platform_compliance_report import GetDevicesStatusByPolicyPlatformComplianceReportRequest
	from .get_device_policy_settings_compliance_report import GetDevicePolicySettingsComplianceReportRequest
	from .get_device_policies_compliance_report import GetDevicePoliciesComplianceReportRequest
	from .get_device_non_compliance_report import GetDeviceNonComplianceReportRequest
	from .get_device_management_intent_settings_report import GetDeviceManagementIntentSettingsReportRequest
	from .get_device_management_intent_per_setting_contributing_profiles import GetDeviceManagementIntentPerSettingContributingProfilesRequest
	from .get_device_install_status_report import GetDeviceInstallStatusReportRequest
	from .get_device_configuration_policy_status_summary import GetDeviceConfigurationPolicyStatusSummaryRequest
	from .get_device_configuration_policy_settings_summary_report import GetDeviceConfigurationPolicySettingsSummaryReportRequest
	from .get_configuration_settings_report import GetConfigurationSettingsReportRequest
	from .get_configuration_setting_non_compliance_report import GetConfigurationSettingNonComplianceReportRequest
	from .get_configuration_setting_details_report import GetConfigurationSettingDetailsReportRequest
	from .get_configuration_policy_settings_device_summary_report import GetConfigurationPolicySettingsDeviceSummaryReportRequest
	from .get_configuration_policy_non_compliance_summary_report import GetConfigurationPolicyNonComplianceSummaryReportRequest
	from .get_configuration_policy_non_compliance_report import GetConfigurationPolicyNonComplianceReportRequest
	from .get_configuration_policy_device_summary_report import GetConfigurationPolicyDeviceSummaryReportRequest
	from .get_configuration_policy_devices_report import GetConfigurationPolicyDevicesReportRequest
	from .get_configuration_policies_report_for_device import GetConfigurationPoliciesReportForDeviceRequest
	from .get_config_manager_device_policy_status_report import GetConfigManagerDevicePolicyStatusReportRequest
	from .get_compliance_settings_report import GetComplianceSettingsReportRequest
	from .get_compliance_setting_non_compliance_report import GetComplianceSettingNonComplianceReportRequest
	from .get_compliance_setting_details_report import GetComplianceSettingDetailsReportRequest
	from .get_compliance_policy_non_compliance_summary_report import GetCompliancePolicyNonComplianceSummaryReportRequest
	from .get_compliance_policy_non_compliance_report import GetCompliancePolicyNonComplianceReportRequest
	from .get_compliance_policy_device_summary_report import GetCompliancePolicyDeviceSummaryReportRequest
	from .get_compliance_policy_devices_report import GetCompliancePolicyDevicesReportRequest
	from .get_compliance_policies_report_for_device import GetCompliancePoliciesReportForDeviceRequest
	from .get_certificates_report import GetCertificatesReportRequest
	from .get_cached_report import GetCachedReportRequest
	from .get_app_status_overview_report import GetAppStatusOverviewReportRequest
	from .get_apps_install_summary_report import GetAppsInstallSummaryReportRequest
	from .get_all_certificates_report import GetAllCertificatesReportRequest
	from .get_active_malware_summary_report import GetActiveMalwareSummaryReportRequest
	from .get_active_malware_report import GetActiveMalwareReportRequest
	from .export_jobs import ExportJobsRequest
	from .cached_report_configurations import CachedReportConfigurationsRequest
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.device_management_reports import DeviceManagementReports


class ReportsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceManagement/reports", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> DeviceManagementReports:
		"""
		Get reports from deviceManagement
		
		"""
		tags = ['deviceManagement.deviceManagementReports']

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
		return await self.request_adapter.send_async(request_info, DeviceManagementReports, error_mapping)

	async def patch(
		self,
		body: DeviceManagementReports,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> DeviceManagementReports:
		"""
		Update the navigation property reports in deviceManagement
		
		"""
		tags = ['deviceManagement.deviceManagementReports']

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
		return await self.request_adapter.send_async(request_info, DeviceManagementReports, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property reports for deviceManagement
		
		"""
		tags = ['deviceManagement.deviceManagementReports']
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
	def cached_report_configurations(self,
	) -> CachedReportConfigurationsRequest:
		from .cached_report_configurations import CachedReportConfigurationsRequest
		return CachedReportConfigurationsRequest(self.request_adapter, self.path_parameters)

	@property
	def export_jobs(self,
	) -> ExportJobsRequest:
		from .export_jobs import ExportJobsRequest
		return ExportJobsRequest(self.request_adapter, self.path_parameters)

	@property
	def get_active_malware_report(self,
	) -> GetActiveMalwareReportRequest:
		from .get_active_malware_report import GetActiveMalwareReportRequest
		return GetActiveMalwareReportRequest(self.request_adapter, self.path_parameters)

	@property
	def get_active_malware_summary_report(self,
	) -> GetActiveMalwareSummaryReportRequest:
		from .get_active_malware_summary_report import GetActiveMalwareSummaryReportRequest
		return GetActiveMalwareSummaryReportRequest(self.request_adapter, self.path_parameters)

	@property
	def get_all_certificates_report(self,
	) -> GetAllCertificatesReportRequest:
		from .get_all_certificates_report import GetAllCertificatesReportRequest
		return GetAllCertificatesReportRequest(self.request_adapter, self.path_parameters)

	@property
	def get_apps_install_summary_report(self,
	) -> GetAppsInstallSummaryReportRequest:
		from .get_apps_install_summary_report import GetAppsInstallSummaryReportRequest
		return GetAppsInstallSummaryReportRequest(self.request_adapter, self.path_parameters)

	@property
	def get_app_status_overview_report(self,
	) -> GetAppStatusOverviewReportRequest:
		from .get_app_status_overview_report import GetAppStatusOverviewReportRequest
		return GetAppStatusOverviewReportRequest(self.request_adapter, self.path_parameters)

	@property
	def get_cached_report(self,
	) -> GetCachedReportRequest:
		from .get_cached_report import GetCachedReportRequest
		return GetCachedReportRequest(self.request_adapter, self.path_parameters)

	@property
	def get_certificates_report(self,
	) -> GetCertificatesReportRequest:
		from .get_certificates_report import GetCertificatesReportRequest
		return GetCertificatesReportRequest(self.request_adapter, self.path_parameters)

	@property
	def get_compliance_policies_report_for_device(self,
	) -> GetCompliancePoliciesReportForDeviceRequest:
		from .get_compliance_policies_report_for_device import GetCompliancePoliciesReportForDeviceRequest
		return GetCompliancePoliciesReportForDeviceRequest(self.request_adapter, self.path_parameters)

	@property
	def get_compliance_policy_devices_report(self,
	) -> GetCompliancePolicyDevicesReportRequest:
		from .get_compliance_policy_devices_report import GetCompliancePolicyDevicesReportRequest
		return GetCompliancePolicyDevicesReportRequest(self.request_adapter, self.path_parameters)

	@property
	def get_compliance_policy_device_summary_report(self,
	) -> GetCompliancePolicyDeviceSummaryReportRequest:
		from .get_compliance_policy_device_summary_report import GetCompliancePolicyDeviceSummaryReportRequest
		return GetCompliancePolicyDeviceSummaryReportRequest(self.request_adapter, self.path_parameters)

	@property
	def get_compliance_policy_non_compliance_report(self,
	) -> GetCompliancePolicyNonComplianceReportRequest:
		from .get_compliance_policy_non_compliance_report import GetCompliancePolicyNonComplianceReportRequest
		return GetCompliancePolicyNonComplianceReportRequest(self.request_adapter, self.path_parameters)

	@property
	def get_compliance_policy_non_compliance_summary_report(self,
	) -> GetCompliancePolicyNonComplianceSummaryReportRequest:
		from .get_compliance_policy_non_compliance_summary_report import GetCompliancePolicyNonComplianceSummaryReportRequest
		return GetCompliancePolicyNonComplianceSummaryReportRequest(self.request_adapter, self.path_parameters)

	@property
	def get_compliance_setting_details_report(self,
	) -> GetComplianceSettingDetailsReportRequest:
		from .get_compliance_setting_details_report import GetComplianceSettingDetailsReportRequest
		return GetComplianceSettingDetailsReportRequest(self.request_adapter, self.path_parameters)

	@property
	def get_compliance_setting_non_compliance_report(self,
	) -> GetComplianceSettingNonComplianceReportRequest:
		from .get_compliance_setting_non_compliance_report import GetComplianceSettingNonComplianceReportRequest
		return GetComplianceSettingNonComplianceReportRequest(self.request_adapter, self.path_parameters)

	@property
	def get_compliance_settings_report(self,
	) -> GetComplianceSettingsReportRequest:
		from .get_compliance_settings_report import GetComplianceSettingsReportRequest
		return GetComplianceSettingsReportRequest(self.request_adapter, self.path_parameters)

	@property
	def get_config_manager_device_policy_status_report(self,
	) -> GetConfigManagerDevicePolicyStatusReportRequest:
		from .get_config_manager_device_policy_status_report import GetConfigManagerDevicePolicyStatusReportRequest
		return GetConfigManagerDevicePolicyStatusReportRequest(self.request_adapter, self.path_parameters)

	@property
	def get_configuration_policies_report_for_device(self,
	) -> GetConfigurationPoliciesReportForDeviceRequest:
		from .get_configuration_policies_report_for_device import GetConfigurationPoliciesReportForDeviceRequest
		return GetConfigurationPoliciesReportForDeviceRequest(self.request_adapter, self.path_parameters)

	@property
	def get_configuration_policy_devices_report(self,
	) -> GetConfigurationPolicyDevicesReportRequest:
		from .get_configuration_policy_devices_report import GetConfigurationPolicyDevicesReportRequest
		return GetConfigurationPolicyDevicesReportRequest(self.request_adapter, self.path_parameters)

	@property
	def get_configuration_policy_device_summary_report(self,
	) -> GetConfigurationPolicyDeviceSummaryReportRequest:
		from .get_configuration_policy_device_summary_report import GetConfigurationPolicyDeviceSummaryReportRequest
		return GetConfigurationPolicyDeviceSummaryReportRequest(self.request_adapter, self.path_parameters)

	@property
	def get_configuration_policy_non_compliance_report(self,
	) -> GetConfigurationPolicyNonComplianceReportRequest:
		from .get_configuration_policy_non_compliance_report import GetConfigurationPolicyNonComplianceReportRequest
		return GetConfigurationPolicyNonComplianceReportRequest(self.request_adapter, self.path_parameters)

	@property
	def get_configuration_policy_non_compliance_summary_report(self,
	) -> GetConfigurationPolicyNonComplianceSummaryReportRequest:
		from .get_configuration_policy_non_compliance_summary_report import GetConfigurationPolicyNonComplianceSummaryReportRequest
		return GetConfigurationPolicyNonComplianceSummaryReportRequest(self.request_adapter, self.path_parameters)

	@property
	def get_configuration_policy_settings_device_summary_report(self,
	) -> GetConfigurationPolicySettingsDeviceSummaryReportRequest:
		from .get_configuration_policy_settings_device_summary_report import GetConfigurationPolicySettingsDeviceSummaryReportRequest
		return GetConfigurationPolicySettingsDeviceSummaryReportRequest(self.request_adapter, self.path_parameters)

	@property
	def get_configuration_setting_details_report(self,
	) -> GetConfigurationSettingDetailsReportRequest:
		from .get_configuration_setting_details_report import GetConfigurationSettingDetailsReportRequest
		return GetConfigurationSettingDetailsReportRequest(self.request_adapter, self.path_parameters)

	@property
	def get_configuration_setting_non_compliance_report(self,
	) -> GetConfigurationSettingNonComplianceReportRequest:
		from .get_configuration_setting_non_compliance_report import GetConfigurationSettingNonComplianceReportRequest
		return GetConfigurationSettingNonComplianceReportRequest(self.request_adapter, self.path_parameters)

	@property
	def get_configuration_settings_report(self,
	) -> GetConfigurationSettingsReportRequest:
		from .get_configuration_settings_report import GetConfigurationSettingsReportRequest
		return GetConfigurationSettingsReportRequest(self.request_adapter, self.path_parameters)

	@property
	def get_device_configuration_policy_settings_summary_report(self,
	) -> GetDeviceConfigurationPolicySettingsSummaryReportRequest:
		from .get_device_configuration_policy_settings_summary_report import GetDeviceConfigurationPolicySettingsSummaryReportRequest
		return GetDeviceConfigurationPolicySettingsSummaryReportRequest(self.request_adapter, self.path_parameters)

	@property
	def get_device_configuration_policy_status_summary(self,
	) -> GetDeviceConfigurationPolicyStatusSummaryRequest:
		from .get_device_configuration_policy_status_summary import GetDeviceConfigurationPolicyStatusSummaryRequest
		return GetDeviceConfigurationPolicyStatusSummaryRequest(self.request_adapter, self.path_parameters)

	@property
	def get_device_install_status_report(self,
	) -> GetDeviceInstallStatusReportRequest:
		from .get_device_install_status_report import GetDeviceInstallStatusReportRequest
		return GetDeviceInstallStatusReportRequest(self.request_adapter, self.path_parameters)

	@property
	def get_device_management_intent_per_setting_contributing_profiles(self,
	) -> GetDeviceManagementIntentPerSettingContributingProfilesRequest:
		from .get_device_management_intent_per_setting_contributing_profiles import GetDeviceManagementIntentPerSettingContributingProfilesRequest
		return GetDeviceManagementIntentPerSettingContributingProfilesRequest(self.request_adapter, self.path_parameters)

	@property
	def get_device_management_intent_settings_report(self,
	) -> GetDeviceManagementIntentSettingsReportRequest:
		from .get_device_management_intent_settings_report import GetDeviceManagementIntentSettingsReportRequest
		return GetDeviceManagementIntentSettingsReportRequest(self.request_adapter, self.path_parameters)

	@property
	def get_device_non_compliance_report(self,
	) -> GetDeviceNonComplianceReportRequest:
		from .get_device_non_compliance_report import GetDeviceNonComplianceReportRequest
		return GetDeviceNonComplianceReportRequest(self.request_adapter, self.path_parameters)

	@property
	def get_device_policies_compliance_report(self,
	) -> GetDevicePoliciesComplianceReportRequest:
		from .get_device_policies_compliance_report import GetDevicePoliciesComplianceReportRequest
		return GetDevicePoliciesComplianceReportRequest(self.request_adapter, self.path_parameters)

	@property
	def get_device_policy_settings_compliance_report(self,
	) -> GetDevicePolicySettingsComplianceReportRequest:
		from .get_device_policy_settings_compliance_report import GetDevicePolicySettingsComplianceReportRequest
		return GetDevicePolicySettingsComplianceReportRequest(self.request_adapter, self.path_parameters)

	@property
	def get_devices_status_by_policy_platform_compliance_report(self,
	) -> GetDevicesStatusByPolicyPlatformComplianceReportRequest:
		from .get_devices_status_by_policy_platform_compliance_report import GetDevicesStatusByPolicyPlatformComplianceReportRequest
		return GetDevicesStatusByPolicyPlatformComplianceReportRequest(self.request_adapter, self.path_parameters)

	@property
	def get_devices_status_by_setting_report(self,
	) -> GetDevicesStatusBySettingReportRequest:
		from .get_devices_status_by_setting_report import GetDevicesStatusBySettingReportRequest
		return GetDevicesStatusBySettingReportRequest(self.request_adapter, self.path_parameters)

	@property
	def get_device_status_by_compliace_policy_report(self,
	) -> GetDeviceStatusByCompliacePolicyReportRequest:
		from .get_device_status_by_compliace_policy_report import GetDeviceStatusByCompliacePolicyReportRequest
		return GetDeviceStatusByCompliacePolicyReportRequest(self.request_adapter, self.path_parameters)

	@property
	def get_device_status_by_compliance_policy_setting_report(self,
	) -> GetDeviceStatusByCompliancePolicySettingReportRequest:
		from .get_device_status_by_compliance_policy_setting_report import GetDeviceStatusByCompliancePolicySettingReportRequest
		return GetDeviceStatusByCompliancePolicySettingReportRequest(self.request_adapter, self.path_parameters)

	@property
	def get_device_status_summary_by_compliace_policy_report(self,
	) -> GetDeviceStatusSummaryByCompliacePolicyReportRequest:
		from .get_device_status_summary_by_compliace_policy_report import GetDeviceStatusSummaryByCompliacePolicyReportRequest
		return GetDeviceStatusSummaryByCompliacePolicyReportRequest(self.request_adapter, self.path_parameters)

	@property
	def get_device_status_summary_by_compliance_policy_settings_report(self,
	) -> GetDeviceStatusSummaryByCompliancePolicySettingsReportRequest:
		from .get_device_status_summary_by_compliance_policy_settings_report import GetDeviceStatusSummaryByCompliancePolicySettingsReportRequest
		return GetDeviceStatusSummaryByCompliancePolicySettingsReportRequest(self.request_adapter, self.path_parameters)

	@property
	def get_devices_without_compliance_policy_report(self,
	) -> GetDevicesWithoutCompliancePolicyReportRequest:
		from .get_devices_without_compliance_policy_report import GetDevicesWithoutCompliancePolicyReportRequest
		return GetDevicesWithoutCompliancePolicyReportRequest(self.request_adapter, self.path_parameters)

	@property
	def get_encryption_report_for_devices(self,
	) -> GetEncryptionReportForDevicesRequest:
		from .get_encryption_report_for_devices import GetEncryptionReportForDevicesRequest
		return GetEncryptionReportForDevicesRequest(self.request_adapter, self.path_parameters)

	@property
	def get_enrollment_configuration_policies_by_device(self,
	) -> GetEnrollmentConfigurationPoliciesByDeviceRequest:
		from .get_enrollment_configuration_policies_by_device import GetEnrollmentConfigurationPoliciesByDeviceRequest
		return GetEnrollmentConfigurationPoliciesByDeviceRequest(self.request_adapter, self.path_parameters)

	@property
	def get_failed_mobile_apps_report(self,
	) -> GetFailedMobileAppsReportRequest:
		from .get_failed_mobile_apps_report import GetFailedMobileAppsReportRequest
		return GetFailedMobileAppsReportRequest(self.request_adapter, self.path_parameters)

	@property
	def get_failed_mobile_apps_summary_report(self,
	) -> GetFailedMobileAppsSummaryReportRequest:
		from .get_failed_mobile_apps_summary_report import GetFailedMobileAppsSummaryReportRequest
		return GetFailedMobileAppsSummaryReportRequest(self.request_adapter, self.path_parameters)

	@property
	def get_group_policy_settings_device_settings_report(self,
	) -> GetGroupPolicySettingsDeviceSettingsReportRequest:
		from .get_group_policy_settings_device_settings_report import GetGroupPolicySettingsDeviceSettingsReportRequest
		return GetGroupPolicySettingsDeviceSettingsReportRequest(self.request_adapter, self.path_parameters)

	@property
	def get_historical_report(self,
	) -> GetHistoricalReportRequest:
		from .get_historical_report import GetHistoricalReportRequest
		return GetHistoricalReportRequest(self.request_adapter, self.path_parameters)

	@property
	def get_malware_summary_report(self,
	) -> GetMalwareSummaryReportRequest:
		from .get_malware_summary_report import GetMalwareSummaryReportRequest
		return GetMalwareSummaryReportRequest(self.request_adapter, self.path_parameters)

	@property
	def get_mobile_application_management_app_configuration_report(self,
	) -> GetMobileApplicationManagementAppConfigurationReportRequest:
		from .get_mobile_application_management_app_configuration_report import GetMobileApplicationManagementAppConfigurationReportRequest
		return GetMobileApplicationManagementAppConfigurationReportRequest(self.request_adapter, self.path_parameters)

	@property
	def get_mobile_application_management_app_registration_summary_report(self,
	) -> GetMobileApplicationManagementAppRegistrationSummaryReportRequest:
		from .get_mobile_application_management_app_registration_summary_report import GetMobileApplicationManagementAppRegistrationSummaryReportRequest
		return GetMobileApplicationManagementAppRegistrationSummaryReportRequest(self.request_adapter, self.path_parameters)

	@property
	def get_noncompliant_devices_and_settings_report(self,
	) -> GetNoncompliantDevicesAndSettingsReportRequest:
		from .get_noncompliant_devices_and_settings_report import GetNoncompliantDevicesAndSettingsReportRequest
		return GetNoncompliantDevicesAndSettingsReportRequest(self.request_adapter, self.path_parameters)

	@property
	def get_policy_non_compliance_metadata(self,
	) -> GetPolicyNonComplianceMetadataRequest:
		from .get_policy_non_compliance_metadata import GetPolicyNonComplianceMetadataRequest
		return GetPolicyNonComplianceMetadataRequest(self.request_adapter, self.path_parameters)

	@property
	def get_policy_non_compliance_report(self,
	) -> GetPolicyNonComplianceReportRequest:
		from .get_policy_non_compliance_report import GetPolicyNonComplianceReportRequest
		return GetPolicyNonComplianceReportRequest(self.request_adapter, self.path_parameters)

	@property
	def get_policy_non_compliance_summary_report(self,
	) -> GetPolicyNonComplianceSummaryReportRequest:
		from .get_policy_non_compliance_summary_report import GetPolicyNonComplianceSummaryReportRequest
		return GetPolicyNonComplianceSummaryReportRequest(self.request_adapter, self.path_parameters)

	@property
	def get_quiet_time_policy_users_report(self,
	) -> GetQuietTimePolicyUsersReportRequest:
		from .get_quiet_time_policy_users_report import GetQuietTimePolicyUsersReportRequest
		return GetQuietTimePolicyUsersReportRequest(self.request_adapter, self.path_parameters)

	@property
	def get_quiet_time_policy_user_summary_report(self,
	) -> GetQuietTimePolicyUserSummaryReportRequest:
		from .get_quiet_time_policy_user_summary_report import GetQuietTimePolicyUserSummaryReportRequest
		return GetQuietTimePolicyUserSummaryReportRequest(self.request_adapter, self.path_parameters)

	@property
	def get_related_apps_status_report(self,
	) -> GetRelatedAppsStatusReportRequest:
		from .get_related_apps_status_report import GetRelatedAppsStatusReportRequest
		return GetRelatedAppsStatusReportRequest(self.request_adapter, self.path_parameters)

	@property
	def get_remote_assistance_sessions_report(self,
	) -> GetRemoteAssistanceSessionsReportRequest:
		from .get_remote_assistance_sessions_report import GetRemoteAssistanceSessionsReportRequest
		return GetRemoteAssistanceSessionsReportRequest(self.request_adapter, self.path_parameters)

	@property
	def get_report_filters(self,
	) -> GetReportFiltersRequest:
		from .get_report_filters import GetReportFiltersRequest
		return GetReportFiltersRequest(self.request_adapter, self.path_parameters)

	@property
	def get_setting_non_compliance_report(self,
	) -> GetSettingNonComplianceReportRequest:
		from .get_setting_non_compliance_report import GetSettingNonComplianceReportRequest
		return GetSettingNonComplianceReportRequest(self.request_adapter, self.path_parameters)

	@property
	def get_unhealthy_defender_agents_report(self,
	) -> GetUnhealthyDefenderAgentsReportRequest:
		from .get_unhealthy_defender_agents_report import GetUnhealthyDefenderAgentsReportRequest
		return GetUnhealthyDefenderAgentsReportRequest(self.request_adapter, self.path_parameters)

	@property
	def get_unhealthy_firewall_report(self,
	) -> GetUnhealthyFirewallReportRequest:
		from .get_unhealthy_firewall_report import GetUnhealthyFirewallReportRequest
		return GetUnhealthyFirewallReportRequest(self.request_adapter, self.path_parameters)

	@property
	def get_unhealthy_firewall_summary_report(self,
	) -> GetUnhealthyFirewallSummaryReportRequest:
		from .get_unhealthy_firewall_summary_report import GetUnhealthyFirewallSummaryReportRequest
		return GetUnhealthyFirewallSummaryReportRequest(self.request_adapter, self.path_parameters)

	@property
	def get_user_install_status_report(self,
	) -> GetUserInstallStatusReportRequest:
		from .get_user_install_status_report import GetUserInstallStatusReportRequest
		return GetUserInstallStatusReportRequest(self.request_adapter, self.path_parameters)

	@property
	def get_windows_driver_update_alerts_per_policy_per_device_report(self,
	) -> GetWindowsDriverUpdateAlertsPerPolicyPerDeviceReportRequest:
		from .get_windows_driver_update_alerts_per_policy_per_device_report import GetWindowsDriverUpdateAlertsPerPolicyPerDeviceReportRequest
		return GetWindowsDriverUpdateAlertsPerPolicyPerDeviceReportRequest(self.request_adapter, self.path_parameters)

	@property
	def get_windows_driver_update_alert_summary_report(self,
	) -> GetWindowsDriverUpdateAlertSummaryReportRequest:
		from .get_windows_driver_update_alert_summary_report import GetWindowsDriverUpdateAlertSummaryReportRequest
		return GetWindowsDriverUpdateAlertSummaryReportRequest(self.request_adapter, self.path_parameters)

	@property
	def get_windows_quality_update_alerts_per_policy_per_device_report(self,
	) -> GetWindowsQualityUpdateAlertsPerPolicyPerDeviceReportRequest:
		from .get_windows_quality_update_alerts_per_policy_per_device_report import GetWindowsQualityUpdateAlertsPerPolicyPerDeviceReportRequest
		return GetWindowsQualityUpdateAlertsPerPolicyPerDeviceReportRequest(self.request_adapter, self.path_parameters)

	@property
	def get_windows_quality_update_alert_summary_report(self,
	) -> GetWindowsQualityUpdateAlertSummaryReportRequest:
		from .get_windows_quality_update_alert_summary_report import GetWindowsQualityUpdateAlertSummaryReportRequest
		return GetWindowsQualityUpdateAlertSummaryReportRequest(self.request_adapter, self.path_parameters)

	@property
	def get_windows_update_alerts_per_policy_per_device_report(self,
	) -> GetWindowsUpdateAlertsPerPolicyPerDeviceReportRequest:
		from .get_windows_update_alerts_per_policy_per_device_report import GetWindowsUpdateAlertsPerPolicyPerDeviceReportRequest
		return GetWindowsUpdateAlertsPerPolicyPerDeviceReportRequest(self.request_adapter, self.path_parameters)

	@property
	def get_windows_update_alert_summary_report(self,
	) -> GetWindowsUpdateAlertSummaryReportRequest:
		from .get_windows_update_alert_summary_report import GetWindowsUpdateAlertSummaryReportRequest
		return GetWindowsUpdateAlertSummaryReportRequest(self.request_adapter, self.path_parameters)

	@property
	def get_zebra_fota_deployment_report(self,
	) -> GetZebraFotaDeploymentReportRequest:
		from .get_zebra_fota_deployment_report import GetZebraFotaDeploymentReportRequest
		return GetZebraFotaDeploymentReportRequest(self.request_adapter, self.path_parameters)

	@property
	def retrieve_cloud_pki_leaf_certificate_report(self,
	) -> RetrieveCloudPkiLeafCertificateReportRequest:
		from .retrieve_cloud_pki_leaf_certificate_report import RetrieveCloudPkiLeafCertificateReportRequest
		return RetrieveCloudPkiLeafCertificateReportRequest(self.request_adapter, self.path_parameters)

	@property
	def retrieve_cloud_pki_leaf_certificate_summary_report(self,
	) -> RetrieveCloudPkiLeafCertificateSummaryReportRequest:
		from .retrieve_cloud_pki_leaf_certificate_summary_report import RetrieveCloudPkiLeafCertificateSummaryReportRequest
		return RetrieveCloudPkiLeafCertificateSummaryReportRequest(self.request_adapter, self.path_parameters)

	@property
	def retrieve_device_app_installation_status_report(self,
	) -> RetrieveDeviceAppInstallationStatusReportRequest:
		from .retrieve_device_app_installation_status_report import RetrieveDeviceAppInstallationStatusReportRequest
		return RetrieveDeviceAppInstallationStatusReportRequest(self.request_adapter, self.path_parameters)

	@property
	def retrieve_security_task_apps_report(self,
	) -> RetrieveSecurityTaskAppsReportRequest:
		from .retrieve_security_task_apps_report import RetrieveSecurityTaskAppsReportRequest
		return RetrieveSecurityTaskAppsReportRequest(self.request_adapter, self.path_parameters)

	@property
	def retrieve_win32_catalog_apps_update_report(self,
	) -> RetrieveWin32CatalogAppsUpdateReportRequest:
		from .retrieve_win32_catalog_apps_update_report import RetrieveWin32CatalogAppsUpdateReportRequest
		return RetrieveWin32CatalogAppsUpdateReportRequest(self.request_adapter, self.path_parameters)

