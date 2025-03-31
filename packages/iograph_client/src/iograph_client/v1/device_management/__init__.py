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
	from .windows_malware_information import WindowsMalwareInformationRequest
	from .windows_information_protection_network_learning_summaries import WindowsInformationProtectionNetworkLearningSummariesRequest
	from .windows_information_protection_app_learning_summaries import WindowsInformationProtectionAppLearningSummariesRequest
	from .windows_autopilot_device_identities import WindowsAutopilotDeviceIdentitiesRequest
	from .virtual_endpoint import VirtualEndpointRequest
	from .user_experience_analytics_work_from_anywhere_model_performance import UserExperienceAnalyticsWorkFromAnywhereModelPerformanceRequest
	from .user_experience_analytics_work_from_anywhere_metrics import UserExperienceAnalyticsWorkFromAnywhereMetricsRequest
	from .user_experience_analytics_work_from_anywhere_hardware_readiness_metric import UserExperienceAnalyticsWorkFromAnywhereHardwareReadinessMetricRequest
	from .user_experience_analytics_score_history import UserExperienceAnalyticsScoreHistoryRequest
	from .user_experience_analytics_overview import UserExperienceAnalyticsOverviewRequest
	from .user_experience_analytics_model_scores import UserExperienceAnalyticsModelScoresRequest
	from .user_experience_analytics_metric_history import UserExperienceAnalyticsMetricHistoryRequest
	from .user_experience_analytics_device_startup_process_performance import UserExperienceAnalyticsDeviceStartupProcessPerformanceRequest
	from .user_experience_analytics_device_startup_processes import UserExperienceAnalyticsDeviceStartupProcessesRequest
	from .user_experience_analytics_device_startup_history import UserExperienceAnalyticsDeviceStartupHistoryRequest
	from .user_experience_analytics_device_scores import UserExperienceAnalyticsDeviceScoresRequest
	from .user_experience_analytics_device_performance import UserExperienceAnalyticsDevicePerformanceRequest
	from .user_experience_analytics_categories import UserExperienceAnalyticsCategoriesRequest
	from .user_experience_analytics_baselines import UserExperienceAnalyticsBaselinesRequest
	from .user_experience_analytics_app_health_overview import UserExperienceAnalyticsAppHealthOverviewRequest
	from .user_experience_analytics_app_health_o_s_version_performance import UserExperienceAnalyticsAppHealthOSVersionPerformanceRequest
	from .user_experience_analytics_app_health_device_performance_details import UserExperienceAnalyticsAppHealthDevicePerformanceDetailsRequest
	from .user_experience_analytics_app_health_device_performance import UserExperienceAnalyticsAppHealthDevicePerformanceRequest
	from .user_experience_analytics_app_health_device_model_performance import UserExperienceAnalyticsAppHealthDeviceModelPerformanceRequest
	from .user_experience_analytics_app_health_application_performance_by_o_s_version import UserExperienceAnalyticsAppHealthApplicationPerformanceByOSVersionRequest
	from .user_experience_analytics_app_health_application_performance_by_app_version_device_id import UserExperienceAnalyticsAppHealthApplicationPerformanceByAppVersionDeviceIdRequest
	from .user_experience_analytics_app_health_application_performance_by_app_version_details import UserExperienceAnalyticsAppHealthApplicationPerformanceByAppVersionDetailsRequest
	from .user_experience_analytics_app_health_application_performance import UserExperienceAnalyticsAppHealthApplicationPerformanceRequest
	from .troubleshooting_events import TroubleshootingEventsRequest
	from .terms_and_conditions import TermsAndConditionsRequest
	from .telecom_expense_management_partners import TelecomExpenseManagementPartnersRequest
	from .software_update_status_summary import SoftwareUpdateStatusSummaryRequest
	from .role_definitions import RoleDefinitionsRequest
	from .role_assignments import RoleAssignmentsRequest
	from .resource_operations import ResourceOperationsRequest
	from .reports import ReportsRequest
	from .remote_assistance_partners import RemoteAssistancePartnersRequest
	from .notification_message_templates import NotificationMessageTemplatesRequest
	from .mobile_threat_defense_connectors import MobileThreatDefenseConnectorsRequest
	from .mobile_app_troubleshooting_events import MobileAppTroubleshootingEventsRequest
	from .verify_windows_enrollment_auto_discovery_with_domainname import VerifyWindowsEnrollmentAutoDiscoveryWithDomainNameRequest
	from .user_experience_analytics_summarize_work_from_anywhere_devices import UserExperienceAnalyticsSummarizeWorkFromAnywhereDevicesRequest
	from .get_effective_permissions_with_scope import GetEffectivePermissionsWithScopeRequest
	from .managed_devices import ManagedDevicesRequest
	from .managed_device_overview import ManagedDeviceOverviewRequest
	from .ios_update_statuses import IosUpdateStatusesRequest
	from .imported_windows_autopilot_device_identities import ImportedWindowsAutopilotDeviceIdentitiesRequest
	from .exchange_connectors import ExchangeConnectorsRequest
	from .device_management_partners import DeviceManagementPartnersRequest
	from .device_enrollment_configurations import DeviceEnrollmentConfigurationsRequest
	from .device_configurations import DeviceConfigurationsRequest
	from .device_configuration_device_state_summaries import DeviceConfigurationDeviceStateSummariesRequest
	from .device_compliance_policy_setting_state_summaries import DeviceCompliancePolicySettingStateSummariesRequest
	from .device_compliance_policy_device_state_summary import DeviceCompliancePolicyDeviceStateSummaryRequest
	from .device_compliance_policies import DeviceCompliancePoliciesRequest
	from .device_categories import DeviceCategoriesRequest
	from .detected_apps import DetectedAppsRequest
	from .conditional_access_settings import ConditionalAccessSettingsRequest
	from .compliance_management_partners import ComplianceManagementPartnersRequest
	from .audit_events import AuditEventsRequest
	from .apple_push_notification_certificate import ApplePushNotificationCertificateRequest
	from ...request_adapter import HttpxRequestAdapter
from iograph_models.v1.device_management import DeviceManagement
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError


class DeviceManagementRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceManagement", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> DeviceManagement:
		"""
		Get deviceManagement
		Read properties and relationships of the deviceManagement object.
		Find more info here: https://learn.microsoft.com/graph/api/intune-wip-devicemanagement-get?view=graph-rest-1.0
		"""
		tags = ['deviceManagement.deviceManagement']

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
		return await self.request_adapter.send_async(request_info, DeviceManagement, error_mapping)

	async def patch(
		self,
		body: DeviceManagement,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> DeviceManagement:
		"""
		Update deviceManagement
		Update the properties of a deviceManagement object.
		Find more info here: https://learn.microsoft.com/graph/api/intune-deviceconfig-devicemanagement-update?view=graph-rest-1.0
		"""
		tags = ['deviceManagement.deviceManagement']

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
		return await self.request_adapter.send_async(request_info, DeviceManagement, error_mapping)

	class GetQueryParams(BaseModel):
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> DeviceManagementRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: DeviceManagementRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return DeviceManagementRequest(self.request_adapter, self.path_parameters)

	@property
	def apple_push_notification_certificate(self,
	) -> ApplePushNotificationCertificateRequest:
		from .apple_push_notification_certificate import ApplePushNotificationCertificateRequest
		return ApplePushNotificationCertificateRequest(self.request_adapter, self.path_parameters)

	@property
	def audit_events(self,
	) -> AuditEventsRequest:
		from .audit_events import AuditEventsRequest
		return AuditEventsRequest(self.request_adapter, self.path_parameters)

	@property
	def compliance_management_partners(self,
	) -> ComplianceManagementPartnersRequest:
		from .compliance_management_partners import ComplianceManagementPartnersRequest
		return ComplianceManagementPartnersRequest(self.request_adapter, self.path_parameters)

	@property
	def conditional_access_settings(self,
	) -> ConditionalAccessSettingsRequest:
		from .conditional_access_settings import ConditionalAccessSettingsRequest
		return ConditionalAccessSettingsRequest(self.request_adapter, self.path_parameters)

	@property
	def detected_apps(self,
	) -> DetectedAppsRequest:
		from .detected_apps import DetectedAppsRequest
		return DetectedAppsRequest(self.request_adapter, self.path_parameters)

	@property
	def device_categories(self,
	) -> DeviceCategoriesRequest:
		from .device_categories import DeviceCategoriesRequest
		return DeviceCategoriesRequest(self.request_adapter, self.path_parameters)

	@property
	def device_compliance_policies(self,
	) -> DeviceCompliancePoliciesRequest:
		from .device_compliance_policies import DeviceCompliancePoliciesRequest
		return DeviceCompliancePoliciesRequest(self.request_adapter, self.path_parameters)

	@property
	def device_compliance_policy_device_state_summary(self,
	) -> DeviceCompliancePolicyDeviceStateSummaryRequest:
		from .device_compliance_policy_device_state_summary import DeviceCompliancePolicyDeviceStateSummaryRequest
		return DeviceCompliancePolicyDeviceStateSummaryRequest(self.request_adapter, self.path_parameters)

	@property
	def device_compliance_policy_setting_state_summaries(self,
	) -> DeviceCompliancePolicySettingStateSummariesRequest:
		from .device_compliance_policy_setting_state_summaries import DeviceCompliancePolicySettingStateSummariesRequest
		return DeviceCompliancePolicySettingStateSummariesRequest(self.request_adapter, self.path_parameters)

	@property
	def device_configuration_device_state_summaries(self,
	) -> DeviceConfigurationDeviceStateSummariesRequest:
		from .device_configuration_device_state_summaries import DeviceConfigurationDeviceStateSummariesRequest
		return DeviceConfigurationDeviceStateSummariesRequest(self.request_adapter, self.path_parameters)

	@property
	def device_configurations(self,
	) -> DeviceConfigurationsRequest:
		from .device_configurations import DeviceConfigurationsRequest
		return DeviceConfigurationsRequest(self.request_adapter, self.path_parameters)

	@property
	def device_enrollment_configurations(self,
	) -> DeviceEnrollmentConfigurationsRequest:
		from .device_enrollment_configurations import DeviceEnrollmentConfigurationsRequest
		return DeviceEnrollmentConfigurationsRequest(self.request_adapter, self.path_parameters)

	@property
	def device_management_partners(self,
	) -> DeviceManagementPartnersRequest:
		from .device_management_partners import DeviceManagementPartnersRequest
		return DeviceManagementPartnersRequest(self.request_adapter, self.path_parameters)

	@property
	def exchange_connectors(self,
	) -> ExchangeConnectorsRequest:
		from .exchange_connectors import ExchangeConnectorsRequest
		return ExchangeConnectorsRequest(self.request_adapter, self.path_parameters)

	@property
	def imported_windows_autopilot_device_identities(self,
	) -> ImportedWindowsAutopilotDeviceIdentitiesRequest:
		from .imported_windows_autopilot_device_identities import ImportedWindowsAutopilotDeviceIdentitiesRequest
		return ImportedWindowsAutopilotDeviceIdentitiesRequest(self.request_adapter, self.path_parameters)

	@property
	def ios_update_statuses(self,
	) -> IosUpdateStatusesRequest:
		from .ios_update_statuses import IosUpdateStatusesRequest
		return IosUpdateStatusesRequest(self.request_adapter, self.path_parameters)

	@property
	def managed_device_overview(self,
	) -> ManagedDeviceOverviewRequest:
		from .managed_device_overview import ManagedDeviceOverviewRequest
		return ManagedDeviceOverviewRequest(self.request_adapter, self.path_parameters)

	@property
	def managed_devices(self,
	) -> ManagedDevicesRequest:
		from .managed_devices import ManagedDevicesRequest
		return ManagedDevicesRequest(self.request_adapter, self.path_parameters)

	def get_effective_permissions_with_scope(self,
		scope: str,
	) -> GetEffectivePermissionsWithScopeRequest:
		if scope is None:
			raise TypeError("scope cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["scope"] =  scope

		from .get_effective_permissions_with_scope import GetEffectivePermissionsWithScopeRequest
		return GetEffectivePermissionsWithScopeRequest(self.request_adapter, path_parameters)

	@property
	def user_experience_analytics_summarize_work_from_anywhere_devices(self,
	) -> UserExperienceAnalyticsSummarizeWorkFromAnywhereDevicesRequest:
		from .user_experience_analytics_summarize_work_from_anywhere_devices import UserExperienceAnalyticsSummarizeWorkFromAnywhereDevicesRequest
		return UserExperienceAnalyticsSummarizeWorkFromAnywhereDevicesRequest(self.request_adapter, self.path_parameters)

	def verify_windows_enrollment_auto_discovery_with_domainname(self,
		domainName: str,
	) -> VerifyWindowsEnrollmentAutoDiscoveryWithDomainNameRequest:
		if domainName is None:
			raise TypeError("domainName cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["domainName"] =  domainName

		from .verify_windows_enrollment_auto_discovery_with_domainname import VerifyWindowsEnrollmentAutoDiscoveryWithDomainNameRequest
		return VerifyWindowsEnrollmentAutoDiscoveryWithDomainNameRequest(self.request_adapter, path_parameters)

	@property
	def mobile_app_troubleshooting_events(self,
	) -> MobileAppTroubleshootingEventsRequest:
		from .mobile_app_troubleshooting_events import MobileAppTroubleshootingEventsRequest
		return MobileAppTroubleshootingEventsRequest(self.request_adapter, self.path_parameters)

	@property
	def mobile_threat_defense_connectors(self,
	) -> MobileThreatDefenseConnectorsRequest:
		from .mobile_threat_defense_connectors import MobileThreatDefenseConnectorsRequest
		return MobileThreatDefenseConnectorsRequest(self.request_adapter, self.path_parameters)

	@property
	def notification_message_templates(self,
	) -> NotificationMessageTemplatesRequest:
		from .notification_message_templates import NotificationMessageTemplatesRequest
		return NotificationMessageTemplatesRequest(self.request_adapter, self.path_parameters)

	@property
	def remote_assistance_partners(self,
	) -> RemoteAssistancePartnersRequest:
		from .remote_assistance_partners import RemoteAssistancePartnersRequest
		return RemoteAssistancePartnersRequest(self.request_adapter, self.path_parameters)

	@property
	def reports(self,
	) -> ReportsRequest:
		from .reports import ReportsRequest
		return ReportsRequest(self.request_adapter, self.path_parameters)

	@property
	def resource_operations(self,
	) -> ResourceOperationsRequest:
		from .resource_operations import ResourceOperationsRequest
		return ResourceOperationsRequest(self.request_adapter, self.path_parameters)

	@property
	def role_assignments(self,
	) -> RoleAssignmentsRequest:
		from .role_assignments import RoleAssignmentsRequest
		return RoleAssignmentsRequest(self.request_adapter, self.path_parameters)

	@property
	def role_definitions(self,
	) -> RoleDefinitionsRequest:
		from .role_definitions import RoleDefinitionsRequest
		return RoleDefinitionsRequest(self.request_adapter, self.path_parameters)

	@property
	def software_update_status_summary(self,
	) -> SoftwareUpdateStatusSummaryRequest:
		from .software_update_status_summary import SoftwareUpdateStatusSummaryRequest
		return SoftwareUpdateStatusSummaryRequest(self.request_adapter, self.path_parameters)

	@property
	def telecom_expense_management_partners(self,
	) -> TelecomExpenseManagementPartnersRequest:
		from .telecom_expense_management_partners import TelecomExpenseManagementPartnersRequest
		return TelecomExpenseManagementPartnersRequest(self.request_adapter, self.path_parameters)

	@property
	def terms_and_conditions(self,
	) -> TermsAndConditionsRequest:
		from .terms_and_conditions import TermsAndConditionsRequest
		return TermsAndConditionsRequest(self.request_adapter, self.path_parameters)

	@property
	def troubleshooting_events(self,
	) -> TroubleshootingEventsRequest:
		from .troubleshooting_events import TroubleshootingEventsRequest
		return TroubleshootingEventsRequest(self.request_adapter, self.path_parameters)

	@property
	def user_experience_analytics_app_health_application_performance(self,
	) -> UserExperienceAnalyticsAppHealthApplicationPerformanceRequest:
		from .user_experience_analytics_app_health_application_performance import UserExperienceAnalyticsAppHealthApplicationPerformanceRequest
		return UserExperienceAnalyticsAppHealthApplicationPerformanceRequest(self.request_adapter, self.path_parameters)

	@property
	def user_experience_analytics_app_health_application_performance_by_app_version_details(self,
	) -> UserExperienceAnalyticsAppHealthApplicationPerformanceByAppVersionDetailsRequest:
		from .user_experience_analytics_app_health_application_performance_by_app_version_details import UserExperienceAnalyticsAppHealthApplicationPerformanceByAppVersionDetailsRequest
		return UserExperienceAnalyticsAppHealthApplicationPerformanceByAppVersionDetailsRequest(self.request_adapter, self.path_parameters)

	@property
	def user_experience_analytics_app_health_application_performance_by_app_version_device_id(self,
	) -> UserExperienceAnalyticsAppHealthApplicationPerformanceByAppVersionDeviceIdRequest:
		from .user_experience_analytics_app_health_application_performance_by_app_version_device_id import UserExperienceAnalyticsAppHealthApplicationPerformanceByAppVersionDeviceIdRequest
		return UserExperienceAnalyticsAppHealthApplicationPerformanceByAppVersionDeviceIdRequest(self.request_adapter, self.path_parameters)

	@property
	def user_experience_analytics_app_health_application_performance_by_o_s_version(self,
	) -> UserExperienceAnalyticsAppHealthApplicationPerformanceByOSVersionRequest:
		from .user_experience_analytics_app_health_application_performance_by_o_s_version import UserExperienceAnalyticsAppHealthApplicationPerformanceByOSVersionRequest
		return UserExperienceAnalyticsAppHealthApplicationPerformanceByOSVersionRequest(self.request_adapter, self.path_parameters)

	@property
	def user_experience_analytics_app_health_device_model_performance(self,
	) -> UserExperienceAnalyticsAppHealthDeviceModelPerformanceRequest:
		from .user_experience_analytics_app_health_device_model_performance import UserExperienceAnalyticsAppHealthDeviceModelPerformanceRequest
		return UserExperienceAnalyticsAppHealthDeviceModelPerformanceRequest(self.request_adapter, self.path_parameters)

	@property
	def user_experience_analytics_app_health_device_performance(self,
	) -> UserExperienceAnalyticsAppHealthDevicePerformanceRequest:
		from .user_experience_analytics_app_health_device_performance import UserExperienceAnalyticsAppHealthDevicePerformanceRequest
		return UserExperienceAnalyticsAppHealthDevicePerformanceRequest(self.request_adapter, self.path_parameters)

	@property
	def user_experience_analytics_app_health_device_performance_details(self,
	) -> UserExperienceAnalyticsAppHealthDevicePerformanceDetailsRequest:
		from .user_experience_analytics_app_health_device_performance_details import UserExperienceAnalyticsAppHealthDevicePerformanceDetailsRequest
		return UserExperienceAnalyticsAppHealthDevicePerformanceDetailsRequest(self.request_adapter, self.path_parameters)

	@property
	def user_experience_analytics_app_health_o_s_version_performance(self,
	) -> UserExperienceAnalyticsAppHealthOSVersionPerformanceRequest:
		from .user_experience_analytics_app_health_o_s_version_performance import UserExperienceAnalyticsAppHealthOSVersionPerformanceRequest
		return UserExperienceAnalyticsAppHealthOSVersionPerformanceRequest(self.request_adapter, self.path_parameters)

	@property
	def user_experience_analytics_app_health_overview(self,
	) -> UserExperienceAnalyticsAppHealthOverviewRequest:
		from .user_experience_analytics_app_health_overview import UserExperienceAnalyticsAppHealthOverviewRequest
		return UserExperienceAnalyticsAppHealthOverviewRequest(self.request_adapter, self.path_parameters)

	@property
	def user_experience_analytics_baselines(self,
	) -> UserExperienceAnalyticsBaselinesRequest:
		from .user_experience_analytics_baselines import UserExperienceAnalyticsBaselinesRequest
		return UserExperienceAnalyticsBaselinesRequest(self.request_adapter, self.path_parameters)

	@property
	def user_experience_analytics_categories(self,
	) -> UserExperienceAnalyticsCategoriesRequest:
		from .user_experience_analytics_categories import UserExperienceAnalyticsCategoriesRequest
		return UserExperienceAnalyticsCategoriesRequest(self.request_adapter, self.path_parameters)

	@property
	def user_experience_analytics_device_performance(self,
	) -> UserExperienceAnalyticsDevicePerformanceRequest:
		from .user_experience_analytics_device_performance import UserExperienceAnalyticsDevicePerformanceRequest
		return UserExperienceAnalyticsDevicePerformanceRequest(self.request_adapter, self.path_parameters)

	@property
	def user_experience_analytics_device_scores(self,
	) -> UserExperienceAnalyticsDeviceScoresRequest:
		from .user_experience_analytics_device_scores import UserExperienceAnalyticsDeviceScoresRequest
		return UserExperienceAnalyticsDeviceScoresRequest(self.request_adapter, self.path_parameters)

	@property
	def user_experience_analytics_device_startup_history(self,
	) -> UserExperienceAnalyticsDeviceStartupHistoryRequest:
		from .user_experience_analytics_device_startup_history import UserExperienceAnalyticsDeviceStartupHistoryRequest
		return UserExperienceAnalyticsDeviceStartupHistoryRequest(self.request_adapter, self.path_parameters)

	@property
	def user_experience_analytics_device_startup_processes(self,
	) -> UserExperienceAnalyticsDeviceStartupProcessesRequest:
		from .user_experience_analytics_device_startup_processes import UserExperienceAnalyticsDeviceStartupProcessesRequest
		return UserExperienceAnalyticsDeviceStartupProcessesRequest(self.request_adapter, self.path_parameters)

	@property
	def user_experience_analytics_device_startup_process_performance(self,
	) -> UserExperienceAnalyticsDeviceStartupProcessPerformanceRequest:
		from .user_experience_analytics_device_startup_process_performance import UserExperienceAnalyticsDeviceStartupProcessPerformanceRequest
		return UserExperienceAnalyticsDeviceStartupProcessPerformanceRequest(self.request_adapter, self.path_parameters)

	@property
	def user_experience_analytics_metric_history(self,
	) -> UserExperienceAnalyticsMetricHistoryRequest:
		from .user_experience_analytics_metric_history import UserExperienceAnalyticsMetricHistoryRequest
		return UserExperienceAnalyticsMetricHistoryRequest(self.request_adapter, self.path_parameters)

	@property
	def user_experience_analytics_model_scores(self,
	) -> UserExperienceAnalyticsModelScoresRequest:
		from .user_experience_analytics_model_scores import UserExperienceAnalyticsModelScoresRequest
		return UserExperienceAnalyticsModelScoresRequest(self.request_adapter, self.path_parameters)

	@property
	def user_experience_analytics_overview(self,
	) -> UserExperienceAnalyticsOverviewRequest:
		from .user_experience_analytics_overview import UserExperienceAnalyticsOverviewRequest
		return UserExperienceAnalyticsOverviewRequest(self.request_adapter, self.path_parameters)

	@property
	def user_experience_analytics_score_history(self,
	) -> UserExperienceAnalyticsScoreHistoryRequest:
		from .user_experience_analytics_score_history import UserExperienceAnalyticsScoreHistoryRequest
		return UserExperienceAnalyticsScoreHistoryRequest(self.request_adapter, self.path_parameters)

	@property
	def user_experience_analytics_work_from_anywhere_hardware_readiness_metric(self,
	) -> UserExperienceAnalyticsWorkFromAnywhereHardwareReadinessMetricRequest:
		from .user_experience_analytics_work_from_anywhere_hardware_readiness_metric import UserExperienceAnalyticsWorkFromAnywhereHardwareReadinessMetricRequest
		return UserExperienceAnalyticsWorkFromAnywhereHardwareReadinessMetricRequest(self.request_adapter, self.path_parameters)

	@property
	def user_experience_analytics_work_from_anywhere_metrics(self,
	) -> UserExperienceAnalyticsWorkFromAnywhereMetricsRequest:
		from .user_experience_analytics_work_from_anywhere_metrics import UserExperienceAnalyticsWorkFromAnywhereMetricsRequest
		return UserExperienceAnalyticsWorkFromAnywhereMetricsRequest(self.request_adapter, self.path_parameters)

	@property
	def user_experience_analytics_work_from_anywhere_model_performance(self,
	) -> UserExperienceAnalyticsWorkFromAnywhereModelPerformanceRequest:
		from .user_experience_analytics_work_from_anywhere_model_performance import UserExperienceAnalyticsWorkFromAnywhereModelPerformanceRequest
		return UserExperienceAnalyticsWorkFromAnywhereModelPerformanceRequest(self.request_adapter, self.path_parameters)

	@property
	def virtual_endpoint(self,
	) -> VirtualEndpointRequest:
		from .virtual_endpoint import VirtualEndpointRequest
		return VirtualEndpointRequest(self.request_adapter, self.path_parameters)

	@property
	def windows_autopilot_device_identities(self,
	) -> WindowsAutopilotDeviceIdentitiesRequest:
		from .windows_autopilot_device_identities import WindowsAutopilotDeviceIdentitiesRequest
		return WindowsAutopilotDeviceIdentitiesRequest(self.request_adapter, self.path_parameters)

	@property
	def windows_information_protection_app_learning_summaries(self,
	) -> WindowsInformationProtectionAppLearningSummariesRequest:
		from .windows_information_protection_app_learning_summaries import WindowsInformationProtectionAppLearningSummariesRequest
		return WindowsInformationProtectionAppLearningSummariesRequest(self.request_adapter, self.path_parameters)

	@property
	def windows_information_protection_network_learning_summaries(self,
	) -> WindowsInformationProtectionNetworkLearningSummariesRequest:
		from .windows_information_protection_network_learning_summaries import WindowsInformationProtectionNetworkLearningSummariesRequest
		return WindowsInformationProtectionNetworkLearningSummariesRequest(self.request_adapter, self.path_parameters)

	@property
	def windows_malware_information(self,
	) -> WindowsMalwareInformationRequest:
		from .windows_malware_information import WindowsMalwareInformationRequest
		return WindowsMalwareInformationRequest(self.request_adapter, self.path_parameters)

