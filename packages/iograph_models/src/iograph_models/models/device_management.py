from __future__ import annotations
from uuid import UUID
from typing import Optional
from pydantic import BaseModel, Field


class DeviceManagement(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	deviceProtectionOverview: Optional[DeviceProtectionOverview] = Field(default=None,alias="deviceProtectionOverview",)
	intuneAccountId: Optional[UUID] = Field(default=None,alias="intuneAccountId",)
	intuneBrand: Optional[IntuneBrand] = Field(default=None,alias="intuneBrand",)
	settings: Optional[DeviceManagementSettings] = Field(default=None,alias="settings",)
	subscriptionState: Optional[DeviceManagementSubscriptionState] = Field(default=None,alias="subscriptionState",)
	userExperienceAnalyticsSettings: Optional[UserExperienceAnalyticsSettings] = Field(default=None,alias="userExperienceAnalyticsSettings",)
	windowsMalwareOverview: Optional[WindowsMalwareOverview] = Field(default=None,alias="windowsMalwareOverview",)
	applePushNotificationCertificate: Optional[ApplePushNotificationCertificate] = Field(default=None,alias="applePushNotificationCertificate",)
	auditEvents: Optional[list[AuditEvent]] = Field(default=None,alias="auditEvents",)
	complianceManagementPartners: Optional[list[ComplianceManagementPartner]] = Field(default=None,alias="complianceManagementPartners",)
	conditionalAccessSettings: Optional[OnPremisesConditionalAccessSettings] = Field(default=None,alias="conditionalAccessSettings",)
	detectedApps: Optional[list[DetectedApp]] = Field(default=None,alias="detectedApps",)
	deviceCategories: Optional[list[DeviceCategory]] = Field(default=None,alias="deviceCategories",)
	deviceCompliancePolicies: Optional[list[DeviceCompliancePolicy]] = Field(default=None,alias="deviceCompliancePolicies",)
	deviceCompliancePolicyDeviceStateSummary: Optional[DeviceCompliancePolicyDeviceStateSummary] = Field(default=None,alias="deviceCompliancePolicyDeviceStateSummary",)
	deviceCompliancePolicySettingStateSummaries: Optional[list[DeviceCompliancePolicySettingStateSummary]] = Field(default=None,alias="deviceCompliancePolicySettingStateSummaries",)
	deviceConfigurationDeviceStateSummaries: Optional[DeviceConfigurationDeviceStateSummary] = Field(default=None,alias="deviceConfigurationDeviceStateSummaries",)
	deviceConfigurations: Optional[list[DeviceConfiguration]] = Field(default=None,alias="deviceConfigurations",)
	deviceEnrollmentConfigurations: Optional[list[DeviceEnrollmentConfiguration]] = Field(default=None,alias="deviceEnrollmentConfigurations",)
	deviceManagementPartners: Optional[list[DeviceManagementPartner]] = Field(default=None,alias="deviceManagementPartners",)
	exchangeConnectors: Optional[list[DeviceManagementExchangeConnector]] = Field(default=None,alias="exchangeConnectors",)
	importedWindowsAutopilotDeviceIdentities: Optional[list[ImportedWindowsAutopilotDeviceIdentity]] = Field(default=None,alias="importedWindowsAutopilotDeviceIdentities",)
	iosUpdateStatuses: Optional[list[IosUpdateDeviceStatus]] = Field(default=None,alias="iosUpdateStatuses",)
	managedDeviceOverview: Optional[ManagedDeviceOverview] = Field(default=None,alias="managedDeviceOverview",)
	managedDevices: Optional[list[ManagedDevice]] = Field(default=None,alias="managedDevices",)
	mobileAppTroubleshootingEvents: Optional[list[MobileAppTroubleshootingEvent]] = Field(default=None,alias="mobileAppTroubleshootingEvents",)
	mobileThreatDefenseConnectors: Optional[list[MobileThreatDefenseConnector]] = Field(default=None,alias="mobileThreatDefenseConnectors",)
	notificationMessageTemplates: Optional[list[NotificationMessageTemplate]] = Field(default=None,alias="notificationMessageTemplates",)
	remoteAssistancePartners: Optional[list[RemoteAssistancePartner]] = Field(default=None,alias="remoteAssistancePartners",)
	reports: Optional[DeviceManagementReports] = Field(default=None,alias="reports",)
	resourceOperations: Optional[list[ResourceOperation]] = Field(default=None,alias="resourceOperations",)
	roleAssignments: Optional[list[DeviceAndAppManagementRoleAssignment]] = Field(default=None,alias="roleAssignments",)
	roleDefinitions: Optional[list[RoleDefinition]] = Field(default=None,alias="roleDefinitions",)
	softwareUpdateStatusSummary: Optional[SoftwareUpdateStatusSummary] = Field(default=None,alias="softwareUpdateStatusSummary",)
	telecomExpenseManagementPartners: Optional[list[TelecomExpenseManagementPartner]] = Field(default=None,alias="telecomExpenseManagementPartners",)
	termsAndConditions: Optional[list[TermsAndConditions]] = Field(default=None,alias="termsAndConditions",)
	troubleshootingEvents: Optional[list[DeviceManagementTroubleshootingEvent]] = Field(default=None,alias="troubleshootingEvents",)
	userExperienceAnalyticsAppHealthApplicationPerformance: Optional[list[UserExperienceAnalyticsAppHealthApplicationPerformance]] = Field(default=None,alias="userExperienceAnalyticsAppHealthApplicationPerformance",)
	userExperienceAnalyticsAppHealthApplicationPerformanceByAppVersionDetails: Optional[list[UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionDetails]] = Field(default=None,alias="userExperienceAnalyticsAppHealthApplicationPerformanceByAppVersionDetails",)
	userExperienceAnalyticsAppHealthApplicationPerformanceByAppVersionDeviceId: Optional[list[UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionDeviceId]] = Field(default=None,alias="userExperienceAnalyticsAppHealthApplicationPerformanceByAppVersionDeviceId",)
	userExperienceAnalyticsAppHealthApplicationPerformanceByOSVersion: Optional[list[UserExperienceAnalyticsAppHealthAppPerformanceByOSVersion]] = Field(default=None,alias="userExperienceAnalyticsAppHealthApplicationPerformanceByOSVersion",)
	userExperienceAnalyticsAppHealthDeviceModelPerformance: Optional[list[UserExperienceAnalyticsAppHealthDeviceModelPerformance]] = Field(default=None,alias="userExperienceAnalyticsAppHealthDeviceModelPerformance",)
	userExperienceAnalyticsAppHealthDevicePerformance: Optional[list[UserExperienceAnalyticsAppHealthDevicePerformance]] = Field(default=None,alias="userExperienceAnalyticsAppHealthDevicePerformance",)
	userExperienceAnalyticsAppHealthDevicePerformanceDetails: Optional[list[UserExperienceAnalyticsAppHealthDevicePerformanceDetails]] = Field(default=None,alias="userExperienceAnalyticsAppHealthDevicePerformanceDetails",)
	userExperienceAnalyticsAppHealthOSVersionPerformance: Optional[list[UserExperienceAnalyticsAppHealthOSVersionPerformance]] = Field(default=None,alias="userExperienceAnalyticsAppHealthOSVersionPerformance",)
	userExperienceAnalyticsAppHealthOverview: Optional[UserExperienceAnalyticsCategory] = Field(default=None,alias="userExperienceAnalyticsAppHealthOverview",)
	userExperienceAnalyticsBaselines: Optional[list[UserExperienceAnalyticsBaseline]] = Field(default=None,alias="userExperienceAnalyticsBaselines",)
	userExperienceAnalyticsCategories: Optional[list[UserExperienceAnalyticsCategory]] = Field(default=None,alias="userExperienceAnalyticsCategories",)
	userExperienceAnalyticsDevicePerformance: Optional[list[UserExperienceAnalyticsDevicePerformance]] = Field(default=None,alias="userExperienceAnalyticsDevicePerformance",)
	userExperienceAnalyticsDeviceScores: Optional[list[UserExperienceAnalyticsDeviceScores]] = Field(default=None,alias="userExperienceAnalyticsDeviceScores",)
	userExperienceAnalyticsDeviceStartupHistory: Optional[list[UserExperienceAnalyticsDeviceStartupHistory]] = Field(default=None,alias="userExperienceAnalyticsDeviceStartupHistory",)
	userExperienceAnalyticsDeviceStartupProcesses: Optional[list[UserExperienceAnalyticsDeviceStartupProcess]] = Field(default=None,alias="userExperienceAnalyticsDeviceStartupProcesses",)
	userExperienceAnalyticsDeviceStartupProcessPerformance: Optional[list[UserExperienceAnalyticsDeviceStartupProcessPerformance]] = Field(default=None,alias="userExperienceAnalyticsDeviceStartupProcessPerformance",)
	userExperienceAnalyticsMetricHistory: Optional[list[UserExperienceAnalyticsMetricHistory]] = Field(default=None,alias="userExperienceAnalyticsMetricHistory",)
	userExperienceAnalyticsModelScores: Optional[list[UserExperienceAnalyticsModelScores]] = Field(default=None,alias="userExperienceAnalyticsModelScores",)
	userExperienceAnalyticsOverview: Optional[UserExperienceAnalyticsOverview] = Field(default=None,alias="userExperienceAnalyticsOverview",)
	userExperienceAnalyticsScoreHistory: Optional[list[UserExperienceAnalyticsScoreHistory]] = Field(default=None,alias="userExperienceAnalyticsScoreHistory",)
	userExperienceAnalyticsWorkFromAnywhereHardwareReadinessMetric: Optional[UserExperienceAnalyticsWorkFromAnywhereHardwareReadinessMetric] = Field(default=None,alias="userExperienceAnalyticsWorkFromAnywhereHardwareReadinessMetric",)
	userExperienceAnalyticsWorkFromAnywhereMetrics: Optional[list[UserExperienceAnalyticsWorkFromAnywhereMetric]] = Field(default=None,alias="userExperienceAnalyticsWorkFromAnywhereMetrics",)
	userExperienceAnalyticsWorkFromAnywhereModelPerformance: Optional[list[UserExperienceAnalyticsWorkFromAnywhereModelPerformance]] = Field(default=None,alias="userExperienceAnalyticsWorkFromAnywhereModelPerformance",)
	virtualEndpoint: Optional[VirtualEndpoint] = Field(default=None,alias="virtualEndpoint",)
	windowsAutopilotDeviceIdentities: Optional[list[WindowsAutopilotDeviceIdentity]] = Field(default=None,alias="windowsAutopilotDeviceIdentities",)
	windowsInformationProtectionAppLearningSummaries: Optional[list[WindowsInformationProtectionAppLearningSummary]] = Field(default=None,alias="windowsInformationProtectionAppLearningSummaries",)
	windowsInformationProtectionNetworkLearningSummaries: Optional[list[WindowsInformationProtectionNetworkLearningSummary]] = Field(default=None,alias="windowsInformationProtectionNetworkLearningSummaries",)
	windowsMalwareInformation: Optional[list[WindowsMalwareInformation]] = Field(default=None,alias="windowsMalwareInformation",)

from .device_protection_overview import DeviceProtectionOverview
from .intune_brand import IntuneBrand
from .device_management_settings import DeviceManagementSettings
from .device_management_subscription_state import DeviceManagementSubscriptionState
from .user_experience_analytics_settings import UserExperienceAnalyticsSettings
from .windows_malware_overview import WindowsMalwareOverview
from .apple_push_notification_certificate import ApplePushNotificationCertificate
from .audit_event import AuditEvent
from .compliance_management_partner import ComplianceManagementPartner
from .on_premises_conditional_access_settings import OnPremisesConditionalAccessSettings
from .detected_app import DetectedApp
from .device_category import DeviceCategory
from .device_compliance_policy import DeviceCompliancePolicy
from .device_compliance_policy_device_state_summary import DeviceCompliancePolicyDeviceStateSummary
from .device_compliance_policy_setting_state_summary import DeviceCompliancePolicySettingStateSummary
from .device_configuration_device_state_summary import DeviceConfigurationDeviceStateSummary
from .device_configuration import DeviceConfiguration
from .device_enrollment_configuration import DeviceEnrollmentConfiguration
from .device_management_partner import DeviceManagementPartner
from .device_management_exchange_connector import DeviceManagementExchangeConnector
from .imported_windows_autopilot_device_identity import ImportedWindowsAutopilotDeviceIdentity
from .ios_update_device_status import IosUpdateDeviceStatus
from .managed_device_overview import ManagedDeviceOverview
from .managed_device import ManagedDevice
from .mobile_app_troubleshooting_event import MobileAppTroubleshootingEvent
from .mobile_threat_defense_connector import MobileThreatDefenseConnector
from .notification_message_template import NotificationMessageTemplate
from .remote_assistance_partner import RemoteAssistancePartner
from .device_management_reports import DeviceManagementReports
from .resource_operation import ResourceOperation
from .device_and_app_management_role_assignment import DeviceAndAppManagementRoleAssignment
from .role_definition import RoleDefinition
from .software_update_status_summary import SoftwareUpdateStatusSummary
from .telecom_expense_management_partner import TelecomExpenseManagementPartner
from .terms_and_conditions import TermsAndConditions
from .device_management_troubleshooting_event import DeviceManagementTroubleshootingEvent
from .user_experience_analytics_app_health_application_performance import UserExperienceAnalyticsAppHealthApplicationPerformance
from .user_experience_analytics_app_health_app_performance_by_app_version_details import UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionDetails
from .user_experience_analytics_app_health_app_performance_by_app_version_device_id import UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionDeviceId
from .user_experience_analytics_app_health_app_performance_by_o_s_version import UserExperienceAnalyticsAppHealthAppPerformanceByOSVersion
from .user_experience_analytics_app_health_device_model_performance import UserExperienceAnalyticsAppHealthDeviceModelPerformance
from .user_experience_analytics_app_health_device_performance import UserExperienceAnalyticsAppHealthDevicePerformance
from .user_experience_analytics_app_health_device_performance_details import UserExperienceAnalyticsAppHealthDevicePerformanceDetails
from .user_experience_analytics_app_health_o_s_version_performance import UserExperienceAnalyticsAppHealthOSVersionPerformance
from .user_experience_analytics_category import UserExperienceAnalyticsCategory
from .user_experience_analytics_baseline import UserExperienceAnalyticsBaseline
from .user_experience_analytics_category import UserExperienceAnalyticsCategory
from .user_experience_analytics_device_performance import UserExperienceAnalyticsDevicePerformance
from .user_experience_analytics_device_scores import UserExperienceAnalyticsDeviceScores
from .user_experience_analytics_device_startup_history import UserExperienceAnalyticsDeviceStartupHistory
from .user_experience_analytics_device_startup_process import UserExperienceAnalyticsDeviceStartupProcess
from .user_experience_analytics_device_startup_process_performance import UserExperienceAnalyticsDeviceStartupProcessPerformance
from .user_experience_analytics_metric_history import UserExperienceAnalyticsMetricHistory
from .user_experience_analytics_model_scores import UserExperienceAnalyticsModelScores
from .user_experience_analytics_overview import UserExperienceAnalyticsOverview
from .user_experience_analytics_score_history import UserExperienceAnalyticsScoreHistory
from .user_experience_analytics_work_from_anywhere_hardware_readiness_metric import UserExperienceAnalyticsWorkFromAnywhereHardwareReadinessMetric
from .user_experience_analytics_work_from_anywhere_metric import UserExperienceAnalyticsWorkFromAnywhereMetric
from .user_experience_analytics_work_from_anywhere_model_performance import UserExperienceAnalyticsWorkFromAnywhereModelPerformance
from .virtual_endpoint import VirtualEndpoint
from .windows_autopilot_device_identity import WindowsAutopilotDeviceIdentity
from .windows_information_protection_app_learning_summary import WindowsInformationProtectionAppLearningSummary
from .windows_information_protection_network_learning_summary import WindowsInformationProtectionNetworkLearningSummary
from .windows_malware_information import WindowsMalwareInformation

