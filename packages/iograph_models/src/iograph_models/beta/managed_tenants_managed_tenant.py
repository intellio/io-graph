from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class ManagedTenantsManagedTenant(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.managedTenants.managedTenant"] = Field(alias="@odata.type", default="#microsoft.graph.managedTenants.managedTenant")
	aggregatedPolicyCompliances: Optional[list[ManagedTenantsAggregatedPolicyCompliance]] = Field(alias="aggregatedPolicyCompliances", default=None,)
	appPerformances: Optional[list[ManagedTenantsAppPerformance]] = Field(alias="appPerformances", default=None,)
	auditEvents: Optional[list[ManagedTenantsAuditEvent]] = Field(alias="auditEvents", default=None,)
	cloudPcConnections: Optional[list[ManagedTenantsCloudPcConnection]] = Field(alias="cloudPcConnections", default=None,)
	cloudPcDevices: Optional[list[ManagedTenantsCloudPcDevice]] = Field(alias="cloudPcDevices", default=None,)
	cloudPcsOverview: Optional[list[ManagedTenantsCloudPcOverview]] = Field(alias="cloudPcsOverview", default=None,)
	conditionalAccessPolicyCoverages: Optional[list[ManagedTenantsConditionalAccessPolicyCoverage]] = Field(alias="conditionalAccessPolicyCoverages", default=None,)
	credentialUserRegistrationsSummaries: Optional[list[ManagedTenantsCredentialUserRegistrationsSummary]] = Field(alias="credentialUserRegistrationsSummaries", default=None,)
	deviceAppPerformances: Optional[list[ManagedTenantsDeviceAppPerformance]] = Field(alias="deviceAppPerformances", default=None,)
	deviceCompliancePolicySettingStateSummaries: Optional[list[ManagedTenantsDeviceCompliancePolicySettingStateSummary]] = Field(alias="deviceCompliancePolicySettingStateSummaries", default=None,)
	deviceHealthStatuses: Optional[list[ManagedTenantsDeviceHealthStatus]] = Field(alias="deviceHealthStatuses", default=None,)
	managedDeviceCompliances: Optional[list[ManagedTenantsManagedDeviceCompliance]] = Field(alias="managedDeviceCompliances", default=None,)
	managedDeviceComplianceTrends: Optional[list[ManagedTenantsManagedDeviceComplianceTrend]] = Field(alias="managedDeviceComplianceTrends", default=None,)
	managedTenantAlertLogs: Optional[list[ManagedTenantsManagedTenantAlertLog]] = Field(alias="managedTenantAlertLogs", default=None,)
	managedTenantAlertRuleDefinitions: Optional[list[ManagedTenantsManagedTenantAlertRuleDefinition]] = Field(alias="managedTenantAlertRuleDefinitions", default=None,)
	managedTenantAlertRules: Optional[list[ManagedTenantsManagedTenantAlertRule]] = Field(alias="managedTenantAlertRules", default=None,)
	managedTenantAlerts: Optional[list[ManagedTenantsManagedTenantAlert]] = Field(alias="managedTenantAlerts", default=None,)
	managedTenantApiNotifications: Optional[list[ManagedTenantsManagedTenantApiNotification]] = Field(alias="managedTenantApiNotifications", default=None,)
	managedTenantEmailNotifications: Optional[list[ManagedTenantsManagedTenantEmailNotification]] = Field(alias="managedTenantEmailNotifications", default=None,)
	managedTenantTicketingEndpoints: Optional[list[ManagedTenantsManagedTenantTicketingEndpoint]] = Field(alias="managedTenantTicketingEndpoints", default=None,)
	managementActions: Optional[list[ManagedTenantsManagementAction]] = Field(alias="managementActions", default=None,)
	managementActionTenantDeploymentStatuses: Optional[list[ManagedTenantsManagementActionTenantDeploymentStatus]] = Field(alias="managementActionTenantDeploymentStatuses", default=None,)
	managementIntents: Optional[list[ManagedTenantsManagementIntent]] = Field(alias="managementIntents", default=None,)
	managementTemplateCollections: Optional[list[ManagedTenantsManagementTemplateCollection]] = Field(alias="managementTemplateCollections", default=None,)
	managementTemplateCollectionTenantSummaries: Optional[list[ManagedTenantsManagementTemplateCollectionTenantSummary]] = Field(alias="managementTemplateCollectionTenantSummaries", default=None,)
	managementTemplates: Optional[list[ManagedTenantsManagementTemplate]] = Field(alias="managementTemplates", default=None,)
	managementTemplateSteps: Optional[list[ManagedTenantsManagementTemplateStep]] = Field(alias="managementTemplateSteps", default=None,)
	managementTemplateStepTenantSummaries: Optional[list[ManagedTenantsManagementTemplateStepTenantSummary]] = Field(alias="managementTemplateStepTenantSummaries", default=None,)
	managementTemplateStepVersions: Optional[list[ManagedTenantsManagementTemplateStepVersion]] = Field(alias="managementTemplateStepVersions", default=None,)
	myRoles: Optional[list[ManagedTenantsMyRole]] = Field(alias="myRoles", default=None,)
	tenantGroups: Optional[list[ManagedTenantsTenantGroup]] = Field(alias="tenantGroups", default=None,)
	tenants: Optional[list[ManagedTenantsTenant]] = Field(alias="tenants", default=None,)
	tenantsCustomizedInformation: Optional[list[ManagedTenantsTenantCustomizedInformation]] = Field(alias="tenantsCustomizedInformation", default=None,)
	tenantsDetailedInformation: Optional[list[ManagedTenantsTenantDetailedInformation]] = Field(alias="tenantsDetailedInformation", default=None,)
	tenantTags: Optional[list[ManagedTenantsTenantTag]] = Field(alias="tenantTags", default=None,)
	windowsDeviceMalwareStates: Optional[list[ManagedTenantsWindowsDeviceMalwareState]] = Field(alias="windowsDeviceMalwareStates", default=None,)
	windowsProtectionStates: Optional[list[ManagedTenantsWindowsProtectionState]] = Field(alias="windowsProtectionStates", default=None,)

from .managed_tenants_aggregated_policy_compliance import ManagedTenantsAggregatedPolicyCompliance
from .managed_tenants_app_performance import ManagedTenantsAppPerformance
from .managed_tenants_audit_event import ManagedTenantsAuditEvent
from .managed_tenants_cloud_pc_connection import ManagedTenantsCloudPcConnection
from .managed_tenants_cloud_pc_device import ManagedTenantsCloudPcDevice
from .managed_tenants_cloud_pc_overview import ManagedTenantsCloudPcOverview
from .managed_tenants_conditional_access_policy_coverage import ManagedTenantsConditionalAccessPolicyCoverage
from .managed_tenants_credential_user_registrations_summary import ManagedTenantsCredentialUserRegistrationsSummary
from .managed_tenants_device_app_performance import ManagedTenantsDeviceAppPerformance
from .managed_tenants_device_compliance_policy_setting_state_summary import ManagedTenantsDeviceCompliancePolicySettingStateSummary
from .managed_tenants_device_health_status import ManagedTenantsDeviceHealthStatus
from .managed_tenants_managed_device_compliance import ManagedTenantsManagedDeviceCompliance
from .managed_tenants_managed_device_compliance_trend import ManagedTenantsManagedDeviceComplianceTrend
from .managed_tenants_managed_tenant_alert_log import ManagedTenantsManagedTenantAlertLog
from .managed_tenants_managed_tenant_alert_rule_definition import ManagedTenantsManagedTenantAlertRuleDefinition
from .managed_tenants_managed_tenant_alert_rule import ManagedTenantsManagedTenantAlertRule
from .managed_tenants_managed_tenant_alert import ManagedTenantsManagedTenantAlert
from .managed_tenants_managed_tenant_api_notification import ManagedTenantsManagedTenantApiNotification
from .managed_tenants_managed_tenant_email_notification import ManagedTenantsManagedTenantEmailNotification
from .managed_tenants_managed_tenant_ticketing_endpoint import ManagedTenantsManagedTenantTicketingEndpoint
from .managed_tenants_management_action import ManagedTenantsManagementAction
from .managed_tenants_management_action_tenant_deployment_status import ManagedTenantsManagementActionTenantDeploymentStatus
from .managed_tenants_management_intent import ManagedTenantsManagementIntent
from .managed_tenants_management_template_collection import ManagedTenantsManagementTemplateCollection
from .managed_tenants_management_template_collection_tenant_summary import ManagedTenantsManagementTemplateCollectionTenantSummary
from .managed_tenants_management_template import ManagedTenantsManagementTemplate
from .managed_tenants_management_template_step import ManagedTenantsManagementTemplateStep
from .managed_tenants_management_template_step_tenant_summary import ManagedTenantsManagementTemplateStepTenantSummary
from .managed_tenants_management_template_step_version import ManagedTenantsManagementTemplateStepVersion
from .managed_tenants_my_role import ManagedTenantsMyRole
from .managed_tenants_tenant_group import ManagedTenantsTenantGroup
from .managed_tenants_tenant import ManagedTenantsTenant
from .managed_tenants_tenant_customized_information import ManagedTenantsTenantCustomizedInformation
from .managed_tenants_tenant_detailed_information import ManagedTenantsTenantDetailedInformation
from .managed_tenants_tenant_tag import ManagedTenantsTenantTag
from .managed_tenants_windows_device_malware_state import ManagedTenantsWindowsDeviceMalwareState
from .managed_tenants_windows_protection_state import ManagedTenantsWindowsProtectionState
