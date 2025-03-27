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
	from .zebra_fota_deployments import ZebraFotaDeploymentsRequest
	from .zebra_fota_connector import ZebraFotaConnectorRequest
	from .zebra_fota_artifacts import ZebraFotaArtifactsRequest
	from .windows_update_catalog_items import WindowsUpdateCatalogItemsRequest
	from .windows_quality_update_profiles import WindowsQualityUpdateProfilesRequest
	from .windows_quality_update_policies import WindowsQualityUpdatePoliciesRequest
	from .windows_malware_information import WindowsMalwareInformationRequest
	from .windows_information_protection_network_learning_summaries import WindowsInformationProtectionNetworkLearningSummariesRequest
	from .windows_information_protection_app_learning_summaries import WindowsInformationProtectionAppLearningSummariesRequest
	from .windows_feature_update_profiles import WindowsFeatureUpdateProfilesRequest
	from .windows_driver_update_profiles import WindowsDriverUpdateProfilesRequest
	from .windows_autopilot_settings import WindowsAutopilotSettingsRequest
	from .windows_autopilot_device_identities import WindowsAutopilotDeviceIdentitiesRequest
	from .windows_autopilot_deployment_profiles import WindowsAutopilotDeploymentProfilesRequest
	from .virtual_endpoint import VirtualEndpointRequest
	from .user_pfx_certificates import UserPfxCertificatesRequest
	from .user_experience_analytics_work_from_anywhere_model_performance import UserExperienceAnalyticsWorkFromAnywhereModelPerformanceRequest
	from .user_experience_analytics_work_from_anywhere_metrics import UserExperienceAnalyticsWorkFromAnywhereMetricsRequest
	from .user_experience_analytics_work_from_anywhere_hardware_readiness_metric import UserExperienceAnalyticsWorkFromAnywhereHardwareReadinessMetricRequest
	from .user_experience_analytics_score_history import UserExperienceAnalyticsScoreHistoryRequest
	from .user_experience_analytics_resource_performance import UserExperienceAnalyticsResourcePerformanceRequest
	from .user_experience_analytics_remote_connection import UserExperienceAnalyticsRemoteConnectionRequest
	from .user_experience_analytics_overview import UserExperienceAnalyticsOverviewRequest
	from .user_experience_analytics_not_autopilot_ready_device import UserExperienceAnalyticsNotAutopilotReadyDeviceRequest
	from .user_experience_analytics_model_scores import UserExperienceAnalyticsModelScoresRequest
	from .user_experience_analytics_metric_history import UserExperienceAnalyticsMetricHistoryRequest
	from .user_experience_analytics_impacting_process import UserExperienceAnalyticsImpactingProcessRequest
	from .user_experience_analytics_device_timeline_event import UserExperienceAnalyticsDeviceTimelineEventRequest
	from .user_experience_analytics_devices_without_cloud_identity import UserExperienceAnalyticsDevicesWithoutCloudIdentityRequest
	from .user_experience_analytics_device_startup_process_performance import UserExperienceAnalyticsDeviceStartupProcessPerformanceRequest
	from .user_experience_analytics_device_startup_processes import UserExperienceAnalyticsDeviceStartupProcessesRequest
	from .user_experience_analytics_device_startup_history import UserExperienceAnalyticsDeviceStartupHistoryRequest
	from .user_experience_analytics_device_scores import UserExperienceAnalyticsDeviceScoresRequest
	from .user_experience_analytics_device_scopes import UserExperienceAnalyticsDeviceScopesRequest
	from .user_experience_analytics_device_scope import UserExperienceAnalyticsDeviceScopeRequest
	from .user_experience_analytics_device_performance import UserExperienceAnalyticsDevicePerformanceRequest
	from .user_experience_analytics_device_metric_history import UserExperienceAnalyticsDeviceMetricHistoryRequest
	from .user_experience_analytics_categories import UserExperienceAnalyticsCategoriesRequest
	from .user_experience_analytics_battery_health_runtime_details import UserExperienceAnalyticsBatteryHealthRuntimeDetailsRequest
	from .user_experience_analytics_battery_health_os_performance import UserExperienceAnalyticsBatteryHealthOsPerformanceRequest
	from .user_experience_analytics_battery_health_model_performance import UserExperienceAnalyticsBatteryHealthModelPerformanceRequest
	from .user_experience_analytics_battery_health_device_runtime_history import UserExperienceAnalyticsBatteryHealthDeviceRuntimeHistoryRequest
	from .user_experience_analytics_battery_health_device_performance import UserExperienceAnalyticsBatteryHealthDevicePerformanceRequest
	from .user_experience_analytics_battery_health_device_app_impact import UserExperienceAnalyticsBatteryHealthDeviceAppImpactRequest
	from .user_experience_analytics_battery_health_capacity_details import UserExperienceAnalyticsBatteryHealthCapacityDetailsRequest
	from .user_experience_analytics_battery_health_app_impact import UserExperienceAnalyticsBatteryHealthAppImpactRequest
	from .user_experience_analytics_baselines import UserExperienceAnalyticsBaselinesRequest
	from .user_experience_analytics_app_health_overview import UserExperienceAnalyticsAppHealthOverviewRequest
	from .user_experience_analytics_app_health_o_s_version_performance import UserExperienceAnalyticsAppHealthOSVersionPerformanceRequest
	from .user_experience_analytics_app_health_device_performance_details import UserExperienceAnalyticsAppHealthDevicePerformanceDetailsRequest
	from .user_experience_analytics_app_health_device_performance import UserExperienceAnalyticsAppHealthDevicePerformanceRequest
	from .user_experience_analytics_app_health_device_model_performance import UserExperienceAnalyticsAppHealthDeviceModelPerformanceRequest
	from .user_experience_analytics_app_health_application_performance_by_o_s_version import UserExperienceAnalyticsAppHealthApplicationPerformanceByOSVersionRequest
	from .user_experience_analytics_app_health_application_performance_by_app_version_device_id import UserExperienceAnalyticsAppHealthApplicationPerformanceByAppVersionDeviceIdRequest
	from .user_experience_analytics_app_health_application_performance_by_app_version_details import UserExperienceAnalyticsAppHealthApplicationPerformanceByAppVersionDetailsRequest
	from .user_experience_analytics_app_health_application_performance_by_app_version import UserExperienceAnalyticsAppHealthApplicationPerformanceByAppVersionRequest
	from .user_experience_analytics_app_health_application_performance import UserExperienceAnalyticsAppHealthApplicationPerformanceRequest
	from .user_experience_analytics_anomaly_device import UserExperienceAnalyticsAnomalyDeviceRequest
	from .user_experience_analytics_anomaly_correlation_group_overview import UserExperienceAnalyticsAnomalyCorrelationGroupOverviewRequest
	from .user_experience_analytics_anomaly import UserExperienceAnalyticsAnomalyRequest
	from .troubleshooting_events import TroubleshootingEventsRequest
	from .terms_and_conditions import TermsAndConditionsRequest
	from .tenant_attach_r_b_a_c import TenantAttachRBACRequest
	from .template_settings import TemplateSettingsRequest
	from .templates import TemplatesRequest
	from .template_insights import TemplateInsightsRequest
	from .telecom_expense_management_partners import TelecomExpenseManagementPartnersRequest
	from .software_update_status_summary import SoftwareUpdateStatusSummaryRequest
	from .setting_definitions import SettingDefinitionsRequest
	from .service_now_connections import ServiceNowConnectionsRequest
	from .role_scope_tags import RoleScopeTagsRequest
	from .role_definitions import RoleDefinitionsRequest
	from .role_assignments import RoleAssignmentsRequest
	from .reusable_settings import ReusableSettingsRequest
	from .reusable_policy_settings import ReusablePolicySettingsRequest
	from .resource_operations import ResourceOperationsRequest
	from .resource_access_profiles import ResourceAccessProfilesRequest
	from .reports import ReportsRequest
	from .remote_assistance_settings import RemoteAssistanceSettingsRequest
	from .remote_assistance_partners import RemoteAssistancePartnersRequest
	from .remote_action_audits import RemoteActionAuditsRequest
	from .privilege_management_elevations import PrivilegeManagementElevationsRequest
	from .operation_approval_requests import OperationApprovalRequestsRequest
	from .operation_approval_policies import OperationApprovalPoliciesRequest
	from .notification_message_templates import NotificationMessageTemplatesRequest
	from .ndes_connectors import NdesConnectorsRequest
	from .monitoring import MonitoringRequest
	from .mobile_threat_defense_connectors import MobileThreatDefenseConnectorsRequest
	from .mobile_app_troubleshooting_events import MobileAppTroubleshootingEventsRequest
	from .microsoft_tunnel_sites import MicrosoftTunnelSitesRequest
	from .microsoft_tunnel_server_log_collection_responses import MicrosoftTunnelServerLogCollectionResponsesRequest
	from .microsoft_tunnel_health_thresholds import MicrosoftTunnelHealthThresholdsRequest
	from .microsoft_tunnel_configurations import MicrosoftTunnelConfigurationsRequest
	from .verify_windows_enrollment_auto_discovery_with_domainname import VerifyWindowsEnrollmentAutoDiscoveryWithDomainNameRequest
	from .user_experience_analytics_summarize_work_from_anywhere_devices import UserExperienceAnalyticsSummarizeWorkFromAnywhereDevicesRequest
	from .user_experience_analytics_summarized_device_scopes import UserExperienceAnalyticsSummarizedDeviceScopesRequest
	from .send_custom_notification_to_company_portal import SendCustomNotificationToCompanyPortalRequest
	from .scoped_for_resource_with_resource import ScopedForResourceWithResourceRequest
	from .retrieve_user_role_detail_with_userid import RetrieveUserRoleDetailWithUseridRequest
	from .get_suggested_enrollment_limit_with_enrollmenttype import GetSuggestedEnrollmentLimitWithEnrollmentTypeRequest
	from .get_role_scope_tags_by_resource_with_resource import GetRoleScopeTagsByResourceWithResourceRequest
	from .get_effective_permissions_with_scope import GetEffectivePermissionsWithScopeRequest
	from .get_effective_permissions import GetEffectivePermissionsRequest
	from .get_comanagement_eligible_devices_summary import GetComanagementEligibleDevicesSummaryRequest
	from .get_comanaged_devices_summary import GetComanagedDevicesSummaryRequest
	from .get_assignment_filters_status_details import GetAssignmentFiltersStatusDetailsRequest
	from .get_assigned_role_details import GetAssignedRoleDetailsRequest
	from .evaluate_assignment_filter import EvaluateAssignmentFilterRequest
	from .enable_unlicensed_adminstrators import EnableUnlicensedAdminstratorsRequest
	from .enable_legacy_pc_management import EnableLegacyPcManagementRequest
	from .enable_endpoint_privilege_management import EnableEndpointPrivilegeManagementRequest
	from .enable_android_device_administrator_enrollment import EnableAndroidDeviceAdministratorEnrollmentRequest
	from .managed_device_windows_o_s_images import ManagedDeviceWindowsOSImagesRequest
	from .managed_devices import ManagedDevicesRequest
	from .managed_device_overview import ManagedDeviceOverviewRequest
	from .managed_device_encryption_states import ManagedDeviceEncryptionStatesRequest
	from .managed_device_cleanup_rules import ManagedDeviceCleanupRulesRequest
	from .mac_o_s_software_update_account_summaries import MacOSSoftwareUpdateAccountSummariesRequest
	from .ios_update_statuses import IosUpdateStatusesRequest
	from .intune_branding_profiles import IntuneBrandingProfilesRequest
	from .intents import IntentsRequest
	from .imported_windows_autopilot_device_identities import ImportedWindowsAutopilotDeviceIdentitiesRequest
	from .imported_device_identities import ImportedDeviceIdentitiesRequest
	from .hardware_password_info import HardwarePasswordInfoRequest
	from .hardware_password_details import HardwarePasswordDetailsRequest
	from .hardware_configurations import HardwareConfigurationsRequest
	from .group_policy_uploaded_definition_files import GroupPolicyUploadedDefinitionFilesRequest
	from .group_policy_object_files import GroupPolicyObjectFilesRequest
	from .group_policy_migration_reports import GroupPolicyMigrationReportsRequest
	from .group_policy_definitions import GroupPolicyDefinitionsRequest
	from .group_policy_definition_files import GroupPolicyDefinitionFilesRequest
	from .group_policy_configurations import GroupPolicyConfigurationsRequest
	from .group_policy_categories import GroupPolicyCategoriesRequest
	from .exchange_on_premises_policy import ExchangeOnPremisesPolicyRequest
	from .exchange_on_premises_policies import ExchangeOnPremisesPoliciesRequest
	from .exchange_connectors import ExchangeConnectorsRequest
	from .endpoint_privilege_management_provisioning_status import EndpointPrivilegeManagementProvisioningStatusRequest
	from .embedded_s_i_m_activation_code_pools import EmbeddedSIMActivationCodePoolsRequest
	from .elevation_requests import ElevationRequestsRequest
	from .domain_join_connectors import DomainJoinConnectorsRequest
	from .device_shell_scripts import DeviceShellScriptsRequest
	from .device_management_scripts import DeviceManagementScriptsRequest
	from .device_management_partners import DeviceManagementPartnersRequest
	from .device_health_scripts import DeviceHealthScriptsRequest
	from .device_enrollment_configurations import DeviceEnrollmentConfigurationsRequest
	from .device_custom_attribute_shell_scripts import DeviceCustomAttributeShellScriptsRequest
	from .device_configuration_user_state_summaries import DeviceConfigurationUserStateSummariesRequest
	from .device_configurations_all_managed_device_certificate_states import DeviceConfigurationsAllManagedDeviceCertificateStatesRequest
	from .device_configurations import DeviceConfigurationsRequest
	from .device_configuration_restricted_apps_violations import DeviceConfigurationRestrictedAppsViolationsRequest
	from .device_configuration_device_state_summaries import DeviceConfigurationDeviceStateSummariesRequest
	from .device_configuration_conflict_summary import DeviceConfigurationConflictSummaryRequest
	from .device_compliance_scripts import DeviceComplianceScriptsRequest
	from .device_compliance_policy_setting_state_summaries import DeviceCompliancePolicySettingStateSummariesRequest
	from .device_compliance_policy_device_state_summary import DeviceCompliancePolicyDeviceStateSummaryRequest
	from .device_compliance_policies import DeviceCompliancePoliciesRequest
	from .device_categories import DeviceCategoriesRequest
	from .detected_apps import DetectedAppsRequest
	from .derived_credentials import DerivedCredentialsRequest
	from .dep_onboarding_settings import DepOnboardingSettingsRequest
	from .data_sharing_consents import DataSharingConsentsRequest
	from .configuration_settings import ConfigurationSettingsRequest
	from .configuration_policy_templates import ConfigurationPolicyTemplatesRequest
	from .configuration_policies import ConfigurationPoliciesRequest
	from .configuration_categories import ConfigurationCategoriesRequest
	from .config_manager_collections import ConfigManagerCollectionsRequest
	from .conditional_access_settings import ConditionalAccessSettingsRequest
	from .compliance_settings import ComplianceSettingsRequest
	from .compliance_policies import CompliancePoliciesRequest
	from .compliance_management_partners import ComplianceManagementPartnersRequest
	from .compliance_categories import ComplianceCategoriesRequest
	from .comanagement_eligible_devices import ComanagementEligibleDevicesRequest
	from .comanaged_devices import ComanagedDevicesRequest
	from .cloud_p_c_connectivity_issues import CloudPCConnectivityIssuesRequest
	from .cloud_certification_authority_leaf_certificate import CloudCertificationAuthorityLeafCertificateRequest
	from .cloud_certification_authority import CloudCertificationAuthorityRequest
	from .chrome_o_s_onboarding_settings import ChromeOSOnboardingSettingsRequest
	from .certificate_connector_details import CertificateConnectorDetailsRequest
	from .categories import CategoriesRequest
	from .cart_to_class_associations import CartToClassAssociationsRequest
	from .autopilot_events import AutopilotEventsRequest
	from .audit_events import AuditEventsRequest
	from .assignment_filters import AssignmentFiltersRequest
	from .apple_user_initiated_enrollment_profiles import AppleUserInitiatedEnrollmentProfilesRequest
	from .apple_push_notification_certificate import ApplePushNotificationCertificateRequest
	from .android_managed_store_app_configuration_schemas import AndroidManagedStoreAppConfigurationSchemasRequest
	from .android_managed_store_account_enterprise_settings import AndroidManagedStoreAccountEnterpriseSettingsRequest
	from .android_for_work_settings import AndroidForWorkSettingsRequest
	from .android_for_work_enrollment_profiles import AndroidForWorkEnrollmentProfilesRequest
	from .android_for_work_app_configuration_schemas import AndroidForWorkAppConfigurationSchemasRequest
	from .android_device_owner_enrollment_profiles import AndroidDeviceOwnerEnrollmentProfilesRequest
	from .advanced_threat_protection_onboarding_state_summary import AdvancedThreatProtectionOnboardingStateSummaryRequest
	from ...request_adapter import HttpxRequestAdapter
from iograph_models.beta.device_management import DeviceManagement
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class DeviceManagementRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceManagement", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> DeviceManagement:
		"""
		Get deviceManagement
		
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
	def advanced_threat_protection_onboarding_state_summary(self,
	) -> AdvancedThreatProtectionOnboardingStateSummaryRequest:
		from .advanced_threat_protection_onboarding_state_summary import AdvancedThreatProtectionOnboardingStateSummaryRequest
		return AdvancedThreatProtectionOnboardingStateSummaryRequest(self.request_adapter, self.path_parameters)

	@property
	def android_device_owner_enrollment_profiles(self,
	) -> AndroidDeviceOwnerEnrollmentProfilesRequest:
		from .android_device_owner_enrollment_profiles import AndroidDeviceOwnerEnrollmentProfilesRequest
		return AndroidDeviceOwnerEnrollmentProfilesRequest(self.request_adapter, self.path_parameters)

	@property
	def android_for_work_app_configuration_schemas(self,
	) -> AndroidForWorkAppConfigurationSchemasRequest:
		from .android_for_work_app_configuration_schemas import AndroidForWorkAppConfigurationSchemasRequest
		return AndroidForWorkAppConfigurationSchemasRequest(self.request_adapter, self.path_parameters)

	@property
	def android_for_work_enrollment_profiles(self,
	) -> AndroidForWorkEnrollmentProfilesRequest:
		from .android_for_work_enrollment_profiles import AndroidForWorkEnrollmentProfilesRequest
		return AndroidForWorkEnrollmentProfilesRequest(self.request_adapter, self.path_parameters)

	@property
	def android_for_work_settings(self,
	) -> AndroidForWorkSettingsRequest:
		from .android_for_work_settings import AndroidForWorkSettingsRequest
		return AndroidForWorkSettingsRequest(self.request_adapter, self.path_parameters)

	@property
	def android_managed_store_account_enterprise_settings(self,
	) -> AndroidManagedStoreAccountEnterpriseSettingsRequest:
		from .android_managed_store_account_enterprise_settings import AndroidManagedStoreAccountEnterpriseSettingsRequest
		return AndroidManagedStoreAccountEnterpriseSettingsRequest(self.request_adapter, self.path_parameters)

	@property
	def android_managed_store_app_configuration_schemas(self,
	) -> AndroidManagedStoreAppConfigurationSchemasRequest:
		from .android_managed_store_app_configuration_schemas import AndroidManagedStoreAppConfigurationSchemasRequest
		return AndroidManagedStoreAppConfigurationSchemasRequest(self.request_adapter, self.path_parameters)

	@property
	def apple_push_notification_certificate(self,
	) -> ApplePushNotificationCertificateRequest:
		from .apple_push_notification_certificate import ApplePushNotificationCertificateRequest
		return ApplePushNotificationCertificateRequest(self.request_adapter, self.path_parameters)

	@property
	def apple_user_initiated_enrollment_profiles(self,
	) -> AppleUserInitiatedEnrollmentProfilesRequest:
		from .apple_user_initiated_enrollment_profiles import AppleUserInitiatedEnrollmentProfilesRequest
		return AppleUserInitiatedEnrollmentProfilesRequest(self.request_adapter, self.path_parameters)

	@property
	def assignment_filters(self,
	) -> AssignmentFiltersRequest:
		from .assignment_filters import AssignmentFiltersRequest
		return AssignmentFiltersRequest(self.request_adapter, self.path_parameters)

	@property
	def audit_events(self,
	) -> AuditEventsRequest:
		from .audit_events import AuditEventsRequest
		return AuditEventsRequest(self.request_adapter, self.path_parameters)

	@property
	def autopilot_events(self,
	) -> AutopilotEventsRequest:
		from .autopilot_events import AutopilotEventsRequest
		return AutopilotEventsRequest(self.request_adapter, self.path_parameters)

	@property
	def cart_to_class_associations(self,
	) -> CartToClassAssociationsRequest:
		from .cart_to_class_associations import CartToClassAssociationsRequest
		return CartToClassAssociationsRequest(self.request_adapter, self.path_parameters)

	@property
	def categories(self,
	) -> CategoriesRequest:
		from .categories import CategoriesRequest
		return CategoriesRequest(self.request_adapter, self.path_parameters)

	@property
	def certificate_connector_details(self,
	) -> CertificateConnectorDetailsRequest:
		from .certificate_connector_details import CertificateConnectorDetailsRequest
		return CertificateConnectorDetailsRequest(self.request_adapter, self.path_parameters)

	@property
	def chrome_o_s_onboarding_settings(self,
	) -> ChromeOSOnboardingSettingsRequest:
		from .chrome_o_s_onboarding_settings import ChromeOSOnboardingSettingsRequest
		return ChromeOSOnboardingSettingsRequest(self.request_adapter, self.path_parameters)

	@property
	def cloud_certification_authority(self,
	) -> CloudCertificationAuthorityRequest:
		from .cloud_certification_authority import CloudCertificationAuthorityRequest
		return CloudCertificationAuthorityRequest(self.request_adapter, self.path_parameters)

	@property
	def cloud_certification_authority_leaf_certificate(self,
	) -> CloudCertificationAuthorityLeafCertificateRequest:
		from .cloud_certification_authority_leaf_certificate import CloudCertificationAuthorityLeafCertificateRequest
		return CloudCertificationAuthorityLeafCertificateRequest(self.request_adapter, self.path_parameters)

	@property
	def cloud_p_c_connectivity_issues(self,
	) -> CloudPCConnectivityIssuesRequest:
		from .cloud_p_c_connectivity_issues import CloudPCConnectivityIssuesRequest
		return CloudPCConnectivityIssuesRequest(self.request_adapter, self.path_parameters)

	@property
	def comanaged_devices(self,
	) -> ComanagedDevicesRequest:
		from .comanaged_devices import ComanagedDevicesRequest
		return ComanagedDevicesRequest(self.request_adapter, self.path_parameters)

	@property
	def comanagement_eligible_devices(self,
	) -> ComanagementEligibleDevicesRequest:
		from .comanagement_eligible_devices import ComanagementEligibleDevicesRequest
		return ComanagementEligibleDevicesRequest(self.request_adapter, self.path_parameters)

	@property
	def compliance_categories(self,
	) -> ComplianceCategoriesRequest:
		from .compliance_categories import ComplianceCategoriesRequest
		return ComplianceCategoriesRequest(self.request_adapter, self.path_parameters)

	@property
	def compliance_management_partners(self,
	) -> ComplianceManagementPartnersRequest:
		from .compliance_management_partners import ComplianceManagementPartnersRequest
		return ComplianceManagementPartnersRequest(self.request_adapter, self.path_parameters)

	@property
	def compliance_policies(self,
	) -> CompliancePoliciesRequest:
		from .compliance_policies import CompliancePoliciesRequest
		return CompliancePoliciesRequest(self.request_adapter, self.path_parameters)

	@property
	def compliance_settings(self,
	) -> ComplianceSettingsRequest:
		from .compliance_settings import ComplianceSettingsRequest
		return ComplianceSettingsRequest(self.request_adapter, self.path_parameters)

	@property
	def conditional_access_settings(self,
	) -> ConditionalAccessSettingsRequest:
		from .conditional_access_settings import ConditionalAccessSettingsRequest
		return ConditionalAccessSettingsRequest(self.request_adapter, self.path_parameters)

	@property
	def config_manager_collections(self,
	) -> ConfigManagerCollectionsRequest:
		from .config_manager_collections import ConfigManagerCollectionsRequest
		return ConfigManagerCollectionsRequest(self.request_adapter, self.path_parameters)

	@property
	def configuration_categories(self,
	) -> ConfigurationCategoriesRequest:
		from .configuration_categories import ConfigurationCategoriesRequest
		return ConfigurationCategoriesRequest(self.request_adapter, self.path_parameters)

	@property
	def configuration_policies(self,
	) -> ConfigurationPoliciesRequest:
		from .configuration_policies import ConfigurationPoliciesRequest
		return ConfigurationPoliciesRequest(self.request_adapter, self.path_parameters)

	@property
	def configuration_policy_templates(self,
	) -> ConfigurationPolicyTemplatesRequest:
		from .configuration_policy_templates import ConfigurationPolicyTemplatesRequest
		return ConfigurationPolicyTemplatesRequest(self.request_adapter, self.path_parameters)

	@property
	def configuration_settings(self,
	) -> ConfigurationSettingsRequest:
		from .configuration_settings import ConfigurationSettingsRequest
		return ConfigurationSettingsRequest(self.request_adapter, self.path_parameters)

	@property
	def data_sharing_consents(self,
	) -> DataSharingConsentsRequest:
		from .data_sharing_consents import DataSharingConsentsRequest
		return DataSharingConsentsRequest(self.request_adapter, self.path_parameters)

	@property
	def dep_onboarding_settings(self,
	) -> DepOnboardingSettingsRequest:
		from .dep_onboarding_settings import DepOnboardingSettingsRequest
		return DepOnboardingSettingsRequest(self.request_adapter, self.path_parameters)

	@property
	def derived_credentials(self,
	) -> DerivedCredentialsRequest:
		from .derived_credentials import DerivedCredentialsRequest
		return DerivedCredentialsRequest(self.request_adapter, self.path_parameters)

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
	def device_compliance_scripts(self,
	) -> DeviceComplianceScriptsRequest:
		from .device_compliance_scripts import DeviceComplianceScriptsRequest
		return DeviceComplianceScriptsRequest(self.request_adapter, self.path_parameters)

	@property
	def device_configuration_conflict_summary(self,
	) -> DeviceConfigurationConflictSummaryRequest:
		from .device_configuration_conflict_summary import DeviceConfigurationConflictSummaryRequest
		return DeviceConfigurationConflictSummaryRequest(self.request_adapter, self.path_parameters)

	@property
	def device_configuration_device_state_summaries(self,
	) -> DeviceConfigurationDeviceStateSummariesRequest:
		from .device_configuration_device_state_summaries import DeviceConfigurationDeviceStateSummariesRequest
		return DeviceConfigurationDeviceStateSummariesRequest(self.request_adapter, self.path_parameters)

	@property
	def device_configuration_restricted_apps_violations(self,
	) -> DeviceConfigurationRestrictedAppsViolationsRequest:
		from .device_configuration_restricted_apps_violations import DeviceConfigurationRestrictedAppsViolationsRequest
		return DeviceConfigurationRestrictedAppsViolationsRequest(self.request_adapter, self.path_parameters)

	@property
	def device_configurations(self,
	) -> DeviceConfigurationsRequest:
		from .device_configurations import DeviceConfigurationsRequest
		return DeviceConfigurationsRequest(self.request_adapter, self.path_parameters)

	@property
	def device_configurations_all_managed_device_certificate_states(self,
	) -> DeviceConfigurationsAllManagedDeviceCertificateStatesRequest:
		from .device_configurations_all_managed_device_certificate_states import DeviceConfigurationsAllManagedDeviceCertificateStatesRequest
		return DeviceConfigurationsAllManagedDeviceCertificateStatesRequest(self.request_adapter, self.path_parameters)

	@property
	def device_configuration_user_state_summaries(self,
	) -> DeviceConfigurationUserStateSummariesRequest:
		from .device_configuration_user_state_summaries import DeviceConfigurationUserStateSummariesRequest
		return DeviceConfigurationUserStateSummariesRequest(self.request_adapter, self.path_parameters)

	@property
	def device_custom_attribute_shell_scripts(self,
	) -> DeviceCustomAttributeShellScriptsRequest:
		from .device_custom_attribute_shell_scripts import DeviceCustomAttributeShellScriptsRequest
		return DeviceCustomAttributeShellScriptsRequest(self.request_adapter, self.path_parameters)

	@property
	def device_enrollment_configurations(self,
	) -> DeviceEnrollmentConfigurationsRequest:
		from .device_enrollment_configurations import DeviceEnrollmentConfigurationsRequest
		return DeviceEnrollmentConfigurationsRequest(self.request_adapter, self.path_parameters)

	@property
	def device_health_scripts(self,
	) -> DeviceHealthScriptsRequest:
		from .device_health_scripts import DeviceHealthScriptsRequest
		return DeviceHealthScriptsRequest(self.request_adapter, self.path_parameters)

	@property
	def device_management_partners(self,
	) -> DeviceManagementPartnersRequest:
		from .device_management_partners import DeviceManagementPartnersRequest
		return DeviceManagementPartnersRequest(self.request_adapter, self.path_parameters)

	@property
	def device_management_scripts(self,
	) -> DeviceManagementScriptsRequest:
		from .device_management_scripts import DeviceManagementScriptsRequest
		return DeviceManagementScriptsRequest(self.request_adapter, self.path_parameters)

	@property
	def device_shell_scripts(self,
	) -> DeviceShellScriptsRequest:
		from .device_shell_scripts import DeviceShellScriptsRequest
		return DeviceShellScriptsRequest(self.request_adapter, self.path_parameters)

	@property
	def domain_join_connectors(self,
	) -> DomainJoinConnectorsRequest:
		from .domain_join_connectors import DomainJoinConnectorsRequest
		return DomainJoinConnectorsRequest(self.request_adapter, self.path_parameters)

	@property
	def elevation_requests(self,
	) -> ElevationRequestsRequest:
		from .elevation_requests import ElevationRequestsRequest
		return ElevationRequestsRequest(self.request_adapter, self.path_parameters)

	@property
	def embedded_s_i_m_activation_code_pools(self,
	) -> EmbeddedSIMActivationCodePoolsRequest:
		from .embedded_s_i_m_activation_code_pools import EmbeddedSIMActivationCodePoolsRequest
		return EmbeddedSIMActivationCodePoolsRequest(self.request_adapter, self.path_parameters)

	@property
	def endpoint_privilege_management_provisioning_status(self,
	) -> EndpointPrivilegeManagementProvisioningStatusRequest:
		from .endpoint_privilege_management_provisioning_status import EndpointPrivilegeManagementProvisioningStatusRequest
		return EndpointPrivilegeManagementProvisioningStatusRequest(self.request_adapter, self.path_parameters)

	@property
	def exchange_connectors(self,
	) -> ExchangeConnectorsRequest:
		from .exchange_connectors import ExchangeConnectorsRequest
		return ExchangeConnectorsRequest(self.request_adapter, self.path_parameters)

	@property
	def exchange_on_premises_policies(self,
	) -> ExchangeOnPremisesPoliciesRequest:
		from .exchange_on_premises_policies import ExchangeOnPremisesPoliciesRequest
		return ExchangeOnPremisesPoliciesRequest(self.request_adapter, self.path_parameters)

	@property
	def exchange_on_premises_policy(self,
	) -> ExchangeOnPremisesPolicyRequest:
		from .exchange_on_premises_policy import ExchangeOnPremisesPolicyRequest
		return ExchangeOnPremisesPolicyRequest(self.request_adapter, self.path_parameters)

	@property
	def group_policy_categories(self,
	) -> GroupPolicyCategoriesRequest:
		from .group_policy_categories import GroupPolicyCategoriesRequest
		return GroupPolicyCategoriesRequest(self.request_adapter, self.path_parameters)

	@property
	def group_policy_configurations(self,
	) -> GroupPolicyConfigurationsRequest:
		from .group_policy_configurations import GroupPolicyConfigurationsRequest
		return GroupPolicyConfigurationsRequest(self.request_adapter, self.path_parameters)

	@property
	def group_policy_definition_files(self,
	) -> GroupPolicyDefinitionFilesRequest:
		from .group_policy_definition_files import GroupPolicyDefinitionFilesRequest
		return GroupPolicyDefinitionFilesRequest(self.request_adapter, self.path_parameters)

	@property
	def group_policy_definitions(self,
	) -> GroupPolicyDefinitionsRequest:
		from .group_policy_definitions import GroupPolicyDefinitionsRequest
		return GroupPolicyDefinitionsRequest(self.request_adapter, self.path_parameters)

	@property
	def group_policy_migration_reports(self,
	) -> GroupPolicyMigrationReportsRequest:
		from .group_policy_migration_reports import GroupPolicyMigrationReportsRequest
		return GroupPolicyMigrationReportsRequest(self.request_adapter, self.path_parameters)

	@property
	def group_policy_object_files(self,
	) -> GroupPolicyObjectFilesRequest:
		from .group_policy_object_files import GroupPolicyObjectFilesRequest
		return GroupPolicyObjectFilesRequest(self.request_adapter, self.path_parameters)

	@property
	def group_policy_uploaded_definition_files(self,
	) -> GroupPolicyUploadedDefinitionFilesRequest:
		from .group_policy_uploaded_definition_files import GroupPolicyUploadedDefinitionFilesRequest
		return GroupPolicyUploadedDefinitionFilesRequest(self.request_adapter, self.path_parameters)

	@property
	def hardware_configurations(self,
	) -> HardwareConfigurationsRequest:
		from .hardware_configurations import HardwareConfigurationsRequest
		return HardwareConfigurationsRequest(self.request_adapter, self.path_parameters)

	@property
	def hardware_password_details(self,
	) -> HardwarePasswordDetailsRequest:
		from .hardware_password_details import HardwarePasswordDetailsRequest
		return HardwarePasswordDetailsRequest(self.request_adapter, self.path_parameters)

	@property
	def hardware_password_info(self,
	) -> HardwarePasswordInfoRequest:
		from .hardware_password_info import HardwarePasswordInfoRequest
		return HardwarePasswordInfoRequest(self.request_adapter, self.path_parameters)

	@property
	def imported_device_identities(self,
	) -> ImportedDeviceIdentitiesRequest:
		from .imported_device_identities import ImportedDeviceIdentitiesRequest
		return ImportedDeviceIdentitiesRequest(self.request_adapter, self.path_parameters)

	@property
	def imported_windows_autopilot_device_identities(self,
	) -> ImportedWindowsAutopilotDeviceIdentitiesRequest:
		from .imported_windows_autopilot_device_identities import ImportedWindowsAutopilotDeviceIdentitiesRequest
		return ImportedWindowsAutopilotDeviceIdentitiesRequest(self.request_adapter, self.path_parameters)

	@property
	def intents(self,
	) -> IntentsRequest:
		from .intents import IntentsRequest
		return IntentsRequest(self.request_adapter, self.path_parameters)

	@property
	def intune_branding_profiles(self,
	) -> IntuneBrandingProfilesRequest:
		from .intune_branding_profiles import IntuneBrandingProfilesRequest
		return IntuneBrandingProfilesRequest(self.request_adapter, self.path_parameters)

	@property
	def ios_update_statuses(self,
	) -> IosUpdateStatusesRequest:
		from .ios_update_statuses import IosUpdateStatusesRequest
		return IosUpdateStatusesRequest(self.request_adapter, self.path_parameters)

	@property
	def mac_o_s_software_update_account_summaries(self,
	) -> MacOSSoftwareUpdateAccountSummariesRequest:
		from .mac_o_s_software_update_account_summaries import MacOSSoftwareUpdateAccountSummariesRequest
		return MacOSSoftwareUpdateAccountSummariesRequest(self.request_adapter, self.path_parameters)

	@property
	def managed_device_cleanup_rules(self,
	) -> ManagedDeviceCleanupRulesRequest:
		from .managed_device_cleanup_rules import ManagedDeviceCleanupRulesRequest
		return ManagedDeviceCleanupRulesRequest(self.request_adapter, self.path_parameters)

	@property
	def managed_device_encryption_states(self,
	) -> ManagedDeviceEncryptionStatesRequest:
		from .managed_device_encryption_states import ManagedDeviceEncryptionStatesRequest
		return ManagedDeviceEncryptionStatesRequest(self.request_adapter, self.path_parameters)

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

	@property
	def managed_device_windows_o_s_images(self,
	) -> ManagedDeviceWindowsOSImagesRequest:
		from .managed_device_windows_o_s_images import ManagedDeviceWindowsOSImagesRequest
		return ManagedDeviceWindowsOSImagesRequest(self.request_adapter, self.path_parameters)

	@property
	def enable_android_device_administrator_enrollment(self,
	) -> EnableAndroidDeviceAdministratorEnrollmentRequest:
		from .enable_android_device_administrator_enrollment import EnableAndroidDeviceAdministratorEnrollmentRequest
		return EnableAndroidDeviceAdministratorEnrollmentRequest(self.request_adapter, self.path_parameters)

	@property
	def enable_endpoint_privilege_management(self,
	) -> EnableEndpointPrivilegeManagementRequest:
		from .enable_endpoint_privilege_management import EnableEndpointPrivilegeManagementRequest
		return EnableEndpointPrivilegeManagementRequest(self.request_adapter, self.path_parameters)

	@property
	def enable_legacy_pc_management(self,
	) -> EnableLegacyPcManagementRequest:
		from .enable_legacy_pc_management import EnableLegacyPcManagementRequest
		return EnableLegacyPcManagementRequest(self.request_adapter, self.path_parameters)

	@property
	def enable_unlicensed_adminstrators(self,
	) -> EnableUnlicensedAdminstratorsRequest:
		from .enable_unlicensed_adminstrators import EnableUnlicensedAdminstratorsRequest
		return EnableUnlicensedAdminstratorsRequest(self.request_adapter, self.path_parameters)

	@property
	def evaluate_assignment_filter(self,
	) -> EvaluateAssignmentFilterRequest:
		from .evaluate_assignment_filter import EvaluateAssignmentFilterRequest
		return EvaluateAssignmentFilterRequest(self.request_adapter, self.path_parameters)

	@property
	def get_assigned_role_details(self,
	) -> GetAssignedRoleDetailsRequest:
		from .get_assigned_role_details import GetAssignedRoleDetailsRequest
		return GetAssignedRoleDetailsRequest(self.request_adapter, self.path_parameters)

	@property
	def get_assignment_filters_status_details(self,
	) -> GetAssignmentFiltersStatusDetailsRequest:
		from .get_assignment_filters_status_details import GetAssignmentFiltersStatusDetailsRequest
		return GetAssignmentFiltersStatusDetailsRequest(self.request_adapter, self.path_parameters)

	@property
	def get_comanaged_devices_summary(self,
	) -> GetComanagedDevicesSummaryRequest:
		from .get_comanaged_devices_summary import GetComanagedDevicesSummaryRequest
		return GetComanagedDevicesSummaryRequest(self.request_adapter, self.path_parameters)

	@property
	def get_comanagement_eligible_devices_summary(self,
	) -> GetComanagementEligibleDevicesSummaryRequest:
		from .get_comanagement_eligible_devices_summary import GetComanagementEligibleDevicesSummaryRequest
		return GetComanagementEligibleDevicesSummaryRequest(self.request_adapter, self.path_parameters)

	@property
	def get_effective_permissions(self,
	) -> GetEffectivePermissionsRequest:
		from .get_effective_permissions import GetEffectivePermissionsRequest
		return GetEffectivePermissionsRequest(self.request_adapter, self.path_parameters)

	def get_effective_permissions_with_scope(self,
		scope: str,
	) -> GetEffectivePermissionsWithScopeRequest:
		if scope is None:
			raise TypeError("scope cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["scope"] =  scope

		from .get_effective_permissions_with_scope import GetEffectivePermissionsWithScopeRequest
		return GetEffectivePermissionsWithScopeRequest(self.request_adapter, path_parameters)

	def get_role_scope_tags_by_resource_with_resource(self,
		resource: str,
	) -> GetRoleScopeTagsByResourceWithResourceRequest:
		if resource is None:
			raise TypeError("resource cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["resource"] =  resource

		from .get_role_scope_tags_by_resource_with_resource import GetRoleScopeTagsByResourceWithResourceRequest
		return GetRoleScopeTagsByResourceWithResourceRequest(self.request_adapter, path_parameters)

	def get_suggested_enrollment_limit_with_enrollmenttype(self,
		enrollmentType: str,
	) -> GetSuggestedEnrollmentLimitWithEnrollmentTypeRequest:
		if enrollmentType is None:
			raise TypeError("enrollmentType cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["enrollmentType"] =  enrollmentType

		from .get_suggested_enrollment_limit_with_enrollmenttype import GetSuggestedEnrollmentLimitWithEnrollmentTypeRequest
		return GetSuggestedEnrollmentLimitWithEnrollmentTypeRequest(self.request_adapter, path_parameters)

	def retrieve_user_role_detail_with_userid(self,
		userid: str,
	) -> RetrieveUserRoleDetailWithUseridRequest:
		if userid is None:
			raise TypeError("userid cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["userid"] =  userid

		from .retrieve_user_role_detail_with_userid import RetrieveUserRoleDetailWithUseridRequest
		return RetrieveUserRoleDetailWithUseridRequest(self.request_adapter, path_parameters)

	def scoped_for_resource_with_resource(self,
		resource: str,
	) -> ScopedForResourceWithResourceRequest:
		if resource is None:
			raise TypeError("resource cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["resource"] =  resource

		from .scoped_for_resource_with_resource import ScopedForResourceWithResourceRequest
		return ScopedForResourceWithResourceRequest(self.request_adapter, path_parameters)

	@property
	def send_custom_notification_to_company_portal(self,
	) -> SendCustomNotificationToCompanyPortalRequest:
		from .send_custom_notification_to_company_portal import SendCustomNotificationToCompanyPortalRequest
		return SendCustomNotificationToCompanyPortalRequest(self.request_adapter, self.path_parameters)

	@property
	def user_experience_analytics_summarized_device_scopes(self,
	) -> UserExperienceAnalyticsSummarizedDeviceScopesRequest:
		from .user_experience_analytics_summarized_device_scopes import UserExperienceAnalyticsSummarizedDeviceScopesRequest
		return UserExperienceAnalyticsSummarizedDeviceScopesRequest(self.request_adapter, self.path_parameters)

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
	def microsoft_tunnel_configurations(self,
	) -> MicrosoftTunnelConfigurationsRequest:
		from .microsoft_tunnel_configurations import MicrosoftTunnelConfigurationsRequest
		return MicrosoftTunnelConfigurationsRequest(self.request_adapter, self.path_parameters)

	@property
	def microsoft_tunnel_health_thresholds(self,
	) -> MicrosoftTunnelHealthThresholdsRequest:
		from .microsoft_tunnel_health_thresholds import MicrosoftTunnelHealthThresholdsRequest
		return MicrosoftTunnelHealthThresholdsRequest(self.request_adapter, self.path_parameters)

	@property
	def microsoft_tunnel_server_log_collection_responses(self,
	) -> MicrosoftTunnelServerLogCollectionResponsesRequest:
		from .microsoft_tunnel_server_log_collection_responses import MicrosoftTunnelServerLogCollectionResponsesRequest
		return MicrosoftTunnelServerLogCollectionResponsesRequest(self.request_adapter, self.path_parameters)

	@property
	def microsoft_tunnel_sites(self,
	) -> MicrosoftTunnelSitesRequest:
		from .microsoft_tunnel_sites import MicrosoftTunnelSitesRequest
		return MicrosoftTunnelSitesRequest(self.request_adapter, self.path_parameters)

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
	def monitoring(self,
	) -> MonitoringRequest:
		from .monitoring import MonitoringRequest
		return MonitoringRequest(self.request_adapter, self.path_parameters)

	@property
	def ndes_connectors(self,
	) -> NdesConnectorsRequest:
		from .ndes_connectors import NdesConnectorsRequest
		return NdesConnectorsRequest(self.request_adapter, self.path_parameters)

	@property
	def notification_message_templates(self,
	) -> NotificationMessageTemplatesRequest:
		from .notification_message_templates import NotificationMessageTemplatesRequest
		return NotificationMessageTemplatesRequest(self.request_adapter, self.path_parameters)

	@property
	def operation_approval_policies(self,
	) -> OperationApprovalPoliciesRequest:
		from .operation_approval_policies import OperationApprovalPoliciesRequest
		return OperationApprovalPoliciesRequest(self.request_adapter, self.path_parameters)

	@property
	def operation_approval_requests(self,
	) -> OperationApprovalRequestsRequest:
		from .operation_approval_requests import OperationApprovalRequestsRequest
		return OperationApprovalRequestsRequest(self.request_adapter, self.path_parameters)

	@property
	def privilege_management_elevations(self,
	) -> PrivilegeManagementElevationsRequest:
		from .privilege_management_elevations import PrivilegeManagementElevationsRequest
		return PrivilegeManagementElevationsRequest(self.request_adapter, self.path_parameters)

	@property
	def remote_action_audits(self,
	) -> RemoteActionAuditsRequest:
		from .remote_action_audits import RemoteActionAuditsRequest
		return RemoteActionAuditsRequest(self.request_adapter, self.path_parameters)

	@property
	def remote_assistance_partners(self,
	) -> RemoteAssistancePartnersRequest:
		from .remote_assistance_partners import RemoteAssistancePartnersRequest
		return RemoteAssistancePartnersRequest(self.request_adapter, self.path_parameters)

	@property
	def remote_assistance_settings(self,
	) -> RemoteAssistanceSettingsRequest:
		from .remote_assistance_settings import RemoteAssistanceSettingsRequest
		return RemoteAssistanceSettingsRequest(self.request_adapter, self.path_parameters)

	@property
	def reports(self,
	) -> ReportsRequest:
		from .reports import ReportsRequest
		return ReportsRequest(self.request_adapter, self.path_parameters)

	@property
	def resource_access_profiles(self,
	) -> ResourceAccessProfilesRequest:
		from .resource_access_profiles import ResourceAccessProfilesRequest
		return ResourceAccessProfilesRequest(self.request_adapter, self.path_parameters)

	@property
	def resource_operations(self,
	) -> ResourceOperationsRequest:
		from .resource_operations import ResourceOperationsRequest
		return ResourceOperationsRequest(self.request_adapter, self.path_parameters)

	@property
	def reusable_policy_settings(self,
	) -> ReusablePolicySettingsRequest:
		from .reusable_policy_settings import ReusablePolicySettingsRequest
		return ReusablePolicySettingsRequest(self.request_adapter, self.path_parameters)

	@property
	def reusable_settings(self,
	) -> ReusableSettingsRequest:
		from .reusable_settings import ReusableSettingsRequest
		return ReusableSettingsRequest(self.request_adapter, self.path_parameters)

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
	def role_scope_tags(self,
	) -> RoleScopeTagsRequest:
		from .role_scope_tags import RoleScopeTagsRequest
		return RoleScopeTagsRequest(self.request_adapter, self.path_parameters)

	@property
	def service_now_connections(self,
	) -> ServiceNowConnectionsRequest:
		from .service_now_connections import ServiceNowConnectionsRequest
		return ServiceNowConnectionsRequest(self.request_adapter, self.path_parameters)

	@property
	def setting_definitions(self,
	) -> SettingDefinitionsRequest:
		from .setting_definitions import SettingDefinitionsRequest
		return SettingDefinitionsRequest(self.request_adapter, self.path_parameters)

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
	def template_insights(self,
	) -> TemplateInsightsRequest:
		from .template_insights import TemplateInsightsRequest
		return TemplateInsightsRequest(self.request_adapter, self.path_parameters)

	@property
	def templates(self,
	) -> TemplatesRequest:
		from .templates import TemplatesRequest
		return TemplatesRequest(self.request_adapter, self.path_parameters)

	@property
	def template_settings(self,
	) -> TemplateSettingsRequest:
		from .template_settings import TemplateSettingsRequest
		return TemplateSettingsRequest(self.request_adapter, self.path_parameters)

	@property
	def tenant_attach_r_b_a_c(self,
	) -> TenantAttachRBACRequest:
		from .tenant_attach_r_b_a_c import TenantAttachRBACRequest
		return TenantAttachRBACRequest(self.request_adapter, self.path_parameters)

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
	def user_experience_analytics_anomaly(self,
	) -> UserExperienceAnalyticsAnomalyRequest:
		from .user_experience_analytics_anomaly import UserExperienceAnalyticsAnomalyRequest
		return UserExperienceAnalyticsAnomalyRequest(self.request_adapter, self.path_parameters)

	@property
	def user_experience_analytics_anomaly_correlation_group_overview(self,
	) -> UserExperienceAnalyticsAnomalyCorrelationGroupOverviewRequest:
		from .user_experience_analytics_anomaly_correlation_group_overview import UserExperienceAnalyticsAnomalyCorrelationGroupOverviewRequest
		return UserExperienceAnalyticsAnomalyCorrelationGroupOverviewRequest(self.request_adapter, self.path_parameters)

	@property
	def user_experience_analytics_anomaly_device(self,
	) -> UserExperienceAnalyticsAnomalyDeviceRequest:
		from .user_experience_analytics_anomaly_device import UserExperienceAnalyticsAnomalyDeviceRequest
		return UserExperienceAnalyticsAnomalyDeviceRequest(self.request_adapter, self.path_parameters)

	@property
	def user_experience_analytics_app_health_application_performance(self,
	) -> UserExperienceAnalyticsAppHealthApplicationPerformanceRequest:
		from .user_experience_analytics_app_health_application_performance import UserExperienceAnalyticsAppHealthApplicationPerformanceRequest
		return UserExperienceAnalyticsAppHealthApplicationPerformanceRequest(self.request_adapter, self.path_parameters)

	@property
	def user_experience_analytics_app_health_application_performance_by_app_version(self,
	) -> UserExperienceAnalyticsAppHealthApplicationPerformanceByAppVersionRequest:
		from .user_experience_analytics_app_health_application_performance_by_app_version import UserExperienceAnalyticsAppHealthApplicationPerformanceByAppVersionRequest
		return UserExperienceAnalyticsAppHealthApplicationPerformanceByAppVersionRequest(self.request_adapter, self.path_parameters)

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
	def user_experience_analytics_battery_health_app_impact(self,
	) -> UserExperienceAnalyticsBatteryHealthAppImpactRequest:
		from .user_experience_analytics_battery_health_app_impact import UserExperienceAnalyticsBatteryHealthAppImpactRequest
		return UserExperienceAnalyticsBatteryHealthAppImpactRequest(self.request_adapter, self.path_parameters)

	@property
	def user_experience_analytics_battery_health_capacity_details(self,
	) -> UserExperienceAnalyticsBatteryHealthCapacityDetailsRequest:
		from .user_experience_analytics_battery_health_capacity_details import UserExperienceAnalyticsBatteryHealthCapacityDetailsRequest
		return UserExperienceAnalyticsBatteryHealthCapacityDetailsRequest(self.request_adapter, self.path_parameters)

	@property
	def user_experience_analytics_battery_health_device_app_impact(self,
	) -> UserExperienceAnalyticsBatteryHealthDeviceAppImpactRequest:
		from .user_experience_analytics_battery_health_device_app_impact import UserExperienceAnalyticsBatteryHealthDeviceAppImpactRequest
		return UserExperienceAnalyticsBatteryHealthDeviceAppImpactRequest(self.request_adapter, self.path_parameters)

	@property
	def user_experience_analytics_battery_health_device_performance(self,
	) -> UserExperienceAnalyticsBatteryHealthDevicePerformanceRequest:
		from .user_experience_analytics_battery_health_device_performance import UserExperienceAnalyticsBatteryHealthDevicePerformanceRequest
		return UserExperienceAnalyticsBatteryHealthDevicePerformanceRequest(self.request_adapter, self.path_parameters)

	@property
	def user_experience_analytics_battery_health_device_runtime_history(self,
	) -> UserExperienceAnalyticsBatteryHealthDeviceRuntimeHistoryRequest:
		from .user_experience_analytics_battery_health_device_runtime_history import UserExperienceAnalyticsBatteryHealthDeviceRuntimeHistoryRequest
		return UserExperienceAnalyticsBatteryHealthDeviceRuntimeHistoryRequest(self.request_adapter, self.path_parameters)

	@property
	def user_experience_analytics_battery_health_model_performance(self,
	) -> UserExperienceAnalyticsBatteryHealthModelPerformanceRequest:
		from .user_experience_analytics_battery_health_model_performance import UserExperienceAnalyticsBatteryHealthModelPerformanceRequest
		return UserExperienceAnalyticsBatteryHealthModelPerformanceRequest(self.request_adapter, self.path_parameters)

	@property
	def user_experience_analytics_battery_health_os_performance(self,
	) -> UserExperienceAnalyticsBatteryHealthOsPerformanceRequest:
		from .user_experience_analytics_battery_health_os_performance import UserExperienceAnalyticsBatteryHealthOsPerformanceRequest
		return UserExperienceAnalyticsBatteryHealthOsPerformanceRequest(self.request_adapter, self.path_parameters)

	@property
	def user_experience_analytics_battery_health_runtime_details(self,
	) -> UserExperienceAnalyticsBatteryHealthRuntimeDetailsRequest:
		from .user_experience_analytics_battery_health_runtime_details import UserExperienceAnalyticsBatteryHealthRuntimeDetailsRequest
		return UserExperienceAnalyticsBatteryHealthRuntimeDetailsRequest(self.request_adapter, self.path_parameters)

	@property
	def user_experience_analytics_categories(self,
	) -> UserExperienceAnalyticsCategoriesRequest:
		from .user_experience_analytics_categories import UserExperienceAnalyticsCategoriesRequest
		return UserExperienceAnalyticsCategoriesRequest(self.request_adapter, self.path_parameters)

	@property
	def user_experience_analytics_device_metric_history(self,
	) -> UserExperienceAnalyticsDeviceMetricHistoryRequest:
		from .user_experience_analytics_device_metric_history import UserExperienceAnalyticsDeviceMetricHistoryRequest
		return UserExperienceAnalyticsDeviceMetricHistoryRequest(self.request_adapter, self.path_parameters)

	@property
	def user_experience_analytics_device_performance(self,
	) -> UserExperienceAnalyticsDevicePerformanceRequest:
		from .user_experience_analytics_device_performance import UserExperienceAnalyticsDevicePerformanceRequest
		return UserExperienceAnalyticsDevicePerformanceRequest(self.request_adapter, self.path_parameters)

	@property
	def user_experience_analytics_device_scope(self,
	) -> UserExperienceAnalyticsDeviceScopeRequest:
		from .user_experience_analytics_device_scope import UserExperienceAnalyticsDeviceScopeRequest
		return UserExperienceAnalyticsDeviceScopeRequest(self.request_adapter, self.path_parameters)

	@property
	def user_experience_analytics_device_scopes(self,
	) -> UserExperienceAnalyticsDeviceScopesRequest:
		from .user_experience_analytics_device_scopes import UserExperienceAnalyticsDeviceScopesRequest
		return UserExperienceAnalyticsDeviceScopesRequest(self.request_adapter, self.path_parameters)

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
	def user_experience_analytics_devices_without_cloud_identity(self,
	) -> UserExperienceAnalyticsDevicesWithoutCloudIdentityRequest:
		from .user_experience_analytics_devices_without_cloud_identity import UserExperienceAnalyticsDevicesWithoutCloudIdentityRequest
		return UserExperienceAnalyticsDevicesWithoutCloudIdentityRequest(self.request_adapter, self.path_parameters)

	@property
	def user_experience_analytics_device_timeline_event(self,
	) -> UserExperienceAnalyticsDeviceTimelineEventRequest:
		from .user_experience_analytics_device_timeline_event import UserExperienceAnalyticsDeviceTimelineEventRequest
		return UserExperienceAnalyticsDeviceTimelineEventRequest(self.request_adapter, self.path_parameters)

	@property
	def user_experience_analytics_impacting_process(self,
	) -> UserExperienceAnalyticsImpactingProcessRequest:
		from .user_experience_analytics_impacting_process import UserExperienceAnalyticsImpactingProcessRequest
		return UserExperienceAnalyticsImpactingProcessRequest(self.request_adapter, self.path_parameters)

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
	def user_experience_analytics_not_autopilot_ready_device(self,
	) -> UserExperienceAnalyticsNotAutopilotReadyDeviceRequest:
		from .user_experience_analytics_not_autopilot_ready_device import UserExperienceAnalyticsNotAutopilotReadyDeviceRequest
		return UserExperienceAnalyticsNotAutopilotReadyDeviceRequest(self.request_adapter, self.path_parameters)

	@property
	def user_experience_analytics_overview(self,
	) -> UserExperienceAnalyticsOverviewRequest:
		from .user_experience_analytics_overview import UserExperienceAnalyticsOverviewRequest
		return UserExperienceAnalyticsOverviewRequest(self.request_adapter, self.path_parameters)

	@property
	def user_experience_analytics_remote_connection(self,
	) -> UserExperienceAnalyticsRemoteConnectionRequest:
		from .user_experience_analytics_remote_connection import UserExperienceAnalyticsRemoteConnectionRequest
		return UserExperienceAnalyticsRemoteConnectionRequest(self.request_adapter, self.path_parameters)

	@property
	def user_experience_analytics_resource_performance(self,
	) -> UserExperienceAnalyticsResourcePerformanceRequest:
		from .user_experience_analytics_resource_performance import UserExperienceAnalyticsResourcePerformanceRequest
		return UserExperienceAnalyticsResourcePerformanceRequest(self.request_adapter, self.path_parameters)

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
	def user_pfx_certificates(self,
	) -> UserPfxCertificatesRequest:
		from .user_pfx_certificates import UserPfxCertificatesRequest
		return UserPfxCertificatesRequest(self.request_adapter, self.path_parameters)

	@property
	def virtual_endpoint(self,
	) -> VirtualEndpointRequest:
		from .virtual_endpoint import VirtualEndpointRequest
		return VirtualEndpointRequest(self.request_adapter, self.path_parameters)

	@property
	def windows_autopilot_deployment_profiles(self,
	) -> WindowsAutopilotDeploymentProfilesRequest:
		from .windows_autopilot_deployment_profiles import WindowsAutopilotDeploymentProfilesRequest
		return WindowsAutopilotDeploymentProfilesRequest(self.request_adapter, self.path_parameters)

	@property
	def windows_autopilot_device_identities(self,
	) -> WindowsAutopilotDeviceIdentitiesRequest:
		from .windows_autopilot_device_identities import WindowsAutopilotDeviceIdentitiesRequest
		return WindowsAutopilotDeviceIdentitiesRequest(self.request_adapter, self.path_parameters)

	@property
	def windows_autopilot_settings(self,
	) -> WindowsAutopilotSettingsRequest:
		from .windows_autopilot_settings import WindowsAutopilotSettingsRequest
		return WindowsAutopilotSettingsRequest(self.request_adapter, self.path_parameters)

	@property
	def windows_driver_update_profiles(self,
	) -> WindowsDriverUpdateProfilesRequest:
		from .windows_driver_update_profiles import WindowsDriverUpdateProfilesRequest
		return WindowsDriverUpdateProfilesRequest(self.request_adapter, self.path_parameters)

	@property
	def windows_feature_update_profiles(self,
	) -> WindowsFeatureUpdateProfilesRequest:
		from .windows_feature_update_profiles import WindowsFeatureUpdateProfilesRequest
		return WindowsFeatureUpdateProfilesRequest(self.request_adapter, self.path_parameters)

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

	@property
	def windows_quality_update_policies(self,
	) -> WindowsQualityUpdatePoliciesRequest:
		from .windows_quality_update_policies import WindowsQualityUpdatePoliciesRequest
		return WindowsQualityUpdatePoliciesRequest(self.request_adapter, self.path_parameters)

	@property
	def windows_quality_update_profiles(self,
	) -> WindowsQualityUpdateProfilesRequest:
		from .windows_quality_update_profiles import WindowsQualityUpdateProfilesRequest
		return WindowsQualityUpdateProfilesRequest(self.request_adapter, self.path_parameters)

	@property
	def windows_update_catalog_items(self,
	) -> WindowsUpdateCatalogItemsRequest:
		from .windows_update_catalog_items import WindowsUpdateCatalogItemsRequest
		return WindowsUpdateCatalogItemsRequest(self.request_adapter, self.path_parameters)

	@property
	def zebra_fota_artifacts(self,
	) -> ZebraFotaArtifactsRequest:
		from .zebra_fota_artifacts import ZebraFotaArtifactsRequest
		return ZebraFotaArtifactsRequest(self.request_adapter, self.path_parameters)

	@property
	def zebra_fota_connector(self,
	) -> ZebraFotaConnectorRequest:
		from .zebra_fota_connector import ZebraFotaConnectorRequest
		return ZebraFotaConnectorRequest(self.request_adapter, self.path_parameters)

	@property
	def zebra_fota_deployments(self,
	) -> ZebraFotaDeploymentsRequest:
		from .zebra_fota_deployments import ZebraFotaDeploymentsRequest
		return ZebraFotaDeploymentsRequest(self.request_adapter, self.path_parameters)

