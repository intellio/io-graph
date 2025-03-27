from __future__ import annotations
from uuid import UUID
from typing import Optional
from typing import Union
from typing import Annotated
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagement(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	accountMoveCompletionDateTime: Optional[datetime] = Field(alias="accountMoveCompletionDateTime", default=None,)
	adminConsent: Optional[AdminConsent] = Field(alias="adminConsent", default=None,)
	connectorStatus: Optional[list[ConnectorStatusDetails]] = Field(alias="connectorStatus", default=None,)
	dataProcessorServiceForWindowsFeaturesOnboarding: Optional[DataProcessorServiceForWindowsFeaturesOnboarding] = Field(alias="dataProcessorServiceForWindowsFeaturesOnboarding", default=None,)
	deviceComplianceReportSummarizationDateTime: Optional[datetime] = Field(alias="deviceComplianceReportSummarizationDateTime", default=None,)
	deviceProtectionOverview: Optional[DeviceProtectionOverview] = Field(alias="deviceProtectionOverview", default=None,)
	intuneAccountId: Optional[UUID] = Field(alias="intuneAccountId", default=None,)
	intuneBrand: Optional[IntuneBrand] = Field(alias="intuneBrand", default=None,)
	lastReportAggregationDateTime: Optional[datetime] = Field(alias="lastReportAggregationDateTime", default=None,)
	legacyPcManangementEnabled: Optional[bool] = Field(alias="legacyPcManangementEnabled", default=None,)
	managedDeviceCleanupSettings: Optional[ManagedDeviceCleanupSettings] = Field(alias="managedDeviceCleanupSettings", default=None,)
	maximumDepTokens: Optional[int] = Field(alias="maximumDepTokens", default=None,)
	settings: Optional[DeviceManagementSettings] = Field(alias="settings", default=None,)
	subscriptions: Optional[DeviceManagementSubscriptions | str] = Field(alias="subscriptions", default=None,)
	subscriptionState: Optional[DeviceManagementSubscriptionState | str] = Field(alias="subscriptionState", default=None,)
	unlicensedAdminstratorsEnabled: Optional[bool] = Field(alias="unlicensedAdminstratorsEnabled", default=None,)
	userExperienceAnalyticsAnomalySeverityOverview: Optional[UserExperienceAnalyticsAnomalySeverityOverview] = Field(alias="userExperienceAnalyticsAnomalySeverityOverview", default=None,)
	userExperienceAnalyticsSettings: Optional[UserExperienceAnalyticsSettings] = Field(alias="userExperienceAnalyticsSettings", default=None,)
	windowsMalwareOverview: Optional[WindowsMalwareOverview] = Field(alias="windowsMalwareOverview", default=None,)
	advancedThreatProtectionOnboardingStateSummary: Optional[AdvancedThreatProtectionOnboardingStateSummary] = Field(alias="advancedThreatProtectionOnboardingStateSummary", default=None,)
	androidDeviceOwnerEnrollmentProfiles: Optional[list[AndroidDeviceOwnerEnrollmentProfile]] = Field(alias="androidDeviceOwnerEnrollmentProfiles", default=None,)
	androidForWorkAppConfigurationSchemas: Optional[list[AndroidForWorkAppConfigurationSchema]] = Field(alias="androidForWorkAppConfigurationSchemas", default=None,)
	androidForWorkEnrollmentProfiles: Optional[list[AndroidForWorkEnrollmentProfile]] = Field(alias="androidForWorkEnrollmentProfiles", default=None,)
	androidForWorkSettings: Optional[AndroidForWorkSettings] = Field(alias="androidForWorkSettings", default=None,)
	androidManagedStoreAccountEnterpriseSettings: Optional[AndroidManagedStoreAccountEnterpriseSettings] = Field(alias="androidManagedStoreAccountEnterpriseSettings", default=None,)
	androidManagedStoreAppConfigurationSchemas: Optional[list[AndroidManagedStoreAppConfigurationSchema]] = Field(alias="androidManagedStoreAppConfigurationSchemas", default=None,)
	applePushNotificationCertificate: Optional[ApplePushNotificationCertificate] = Field(alias="applePushNotificationCertificate", default=None,)
	appleUserInitiatedEnrollmentProfiles: Optional[list[AppleUserInitiatedEnrollmentProfile]] = Field(alias="appleUserInitiatedEnrollmentProfiles", default=None,)
	assignmentFilters: Optional[list[Annotated[Union[PayloadCompatibleAssignmentFilter]],Field(discriminator="odata_type")]]] = Field(alias="assignmentFilters", default=None,)
	auditEvents: Optional[list[AuditEvent]] = Field(alias="auditEvents", default=None,)
	autopilotEvents: Optional[list[DeviceManagementAutopilotEvent]] = Field(alias="autopilotEvents", default=None,)
	cartToClassAssociations: Optional[list[CartToClassAssociation]] = Field(alias="cartToClassAssociations", default=None,)
	categories: Optional[list[Annotated[Union[DeviceManagementIntentSettingCategory, DeviceManagementTemplateSettingCategory]],Field(discriminator="odata_type")]]] = Field(alias="categories", default=None,)
	certificateConnectorDetails: Optional[list[CertificateConnectorDetails]] = Field(alias="certificateConnectorDetails", default=None,)
	chromeOSOnboardingSettings: Optional[list[ChromeOSOnboardingSettings]] = Field(alias="chromeOSOnboardingSettings", default=None,)
	cloudCertificationAuthority: Optional[list[CloudCertificationAuthority]] = Field(alias="cloudCertificationAuthority", default=None,)
	cloudCertificationAuthorityLeafCertificate: Optional[list[CloudCertificationAuthorityLeafCertificate]] = Field(alias="cloudCertificationAuthorityLeafCertificate", default=None,)
	cloudPCConnectivityIssues: Optional[list[CloudPCConnectivityIssue]] = Field(alias="cloudPCConnectivityIssues", default=None,)
	comanagedDevices: Optional[list[Annotated[Union[WindowsManagedDevice]],Field(discriminator="odata_type")]]] = Field(alias="comanagedDevices", default=None,)
	comanagementEligibleDevices: Optional[list[ComanagementEligibleDevice]] = Field(alias="comanagementEligibleDevices", default=None,)
	complianceCategories: Optional[list[DeviceManagementConfigurationCategory]] = Field(alias="complianceCategories", default=None,)
	complianceManagementPartners: Optional[list[ComplianceManagementPartner]] = Field(alias="complianceManagementPartners", default=None,)
	compliancePolicies: Optional[list[DeviceManagementCompliancePolicy]] = Field(alias="compliancePolicies", default=None,)
	complianceSettings: Optional[list[Annotated[Union[DeviceManagementConfigurationChoiceSettingDefinition, DeviceManagementConfigurationChoiceSettingCollectionDefinition, DeviceManagementConfigurationRedirectSettingDefinition, DeviceManagementConfigurationSettingGroupDefinition, DeviceManagementConfigurationSettingGroupCollectionDefinition, DeviceManagementConfigurationSimpleSettingDefinition, DeviceManagementConfigurationSimpleSettingCollectionDefinition]],Field(discriminator="odata_type")]]] = Field(alias="complianceSettings", default=None,)
	conditionalAccessSettings: Optional[OnPremisesConditionalAccessSettings] = Field(alias="conditionalAccessSettings", default=None,)
	configManagerCollections: Optional[list[ConfigManagerCollection]] = Field(alias="configManagerCollections", default=None,)
	configurationCategories: Optional[list[DeviceManagementConfigurationCategory]] = Field(alias="configurationCategories", default=None,)
	configurationPolicies: Optional[list[DeviceManagementConfigurationPolicy]] = Field(alias="configurationPolicies", default=None,)
	configurationPolicyTemplates: Optional[list[DeviceManagementConfigurationPolicyTemplate]] = Field(alias="configurationPolicyTemplates", default=None,)
	configurationSettings: Optional[list[Annotated[Union[DeviceManagementConfigurationChoiceSettingDefinition, DeviceManagementConfigurationChoiceSettingCollectionDefinition, DeviceManagementConfigurationRedirectSettingDefinition, DeviceManagementConfigurationSettingGroupDefinition, DeviceManagementConfigurationSettingGroupCollectionDefinition, DeviceManagementConfigurationSimpleSettingDefinition, DeviceManagementConfigurationSimpleSettingCollectionDefinition]],Field(discriminator="odata_type")]]] = Field(alias="configurationSettings", default=None,)
	dataSharingConsents: Optional[list[DataSharingConsent]] = Field(alias="dataSharingConsents", default=None,)
	depOnboardingSettings: Optional[list[DepOnboardingSetting]] = Field(alias="depOnboardingSettings", default=None,)
	derivedCredentials: Optional[list[DeviceManagementDerivedCredentialSettings]] = Field(alias="derivedCredentials", default=None,)
	detectedApps: Optional[list[DetectedApp]] = Field(alias="detectedApps", default=None,)
	deviceCategories: Optional[list[DeviceCategory]] = Field(alias="deviceCategories", default=None,)
	deviceCompliancePolicies: Optional[list[Annotated[Union[AndroidCompliancePolicy, AndroidDeviceOwnerCompliancePolicy, AndroidForWorkCompliancePolicy, AndroidWorkProfileCompliancePolicy, AospDeviceOwnerCompliancePolicy, DefaultDeviceCompliancePolicy, IosCompliancePolicy, MacOSCompliancePolicy, Windows10CompliancePolicy, Windows10MobileCompliancePolicy, Windows81CompliancePolicy, WindowsPhone81CompliancePolicy]],Field(discriminator="odata_type")]]] = Field(alias="deviceCompliancePolicies", default=None,)
	deviceCompliancePolicyDeviceStateSummary: Optional[DeviceCompliancePolicyDeviceStateSummary] = Field(alias="deviceCompliancePolicyDeviceStateSummary", default=None,)
	deviceCompliancePolicySettingStateSummaries: Optional[list[DeviceCompliancePolicySettingStateSummary]] = Field(alias="deviceCompliancePolicySettingStateSummaries", default=None,)
	deviceComplianceScripts: Optional[list[DeviceComplianceScript]] = Field(alias="deviceComplianceScripts", default=None,)
	deviceConfigurationConflictSummary: Optional[list[DeviceConfigurationConflictSummary]] = Field(alias="deviceConfigurationConflictSummary", default=None,)
	deviceConfigurationDeviceStateSummaries: Optional[DeviceConfigurationDeviceStateSummary] = Field(alias="deviceConfigurationDeviceStateSummaries", default=None,)
	deviceConfigurationRestrictedAppsViolations: Optional[list[RestrictedAppsViolation]] = Field(alias="deviceConfigurationRestrictedAppsViolations", default=None,)
	deviceConfigurations: Optional[list[Annotated[Union[AndroidCertificateProfileBase, AndroidForWorkImportedPFXCertificateProfile, AndroidImportedPFXCertificateProfile, AndroidPkcsCertificateProfile, AndroidScepCertificateProfile, AndroidCustomConfiguration, AndroidDeviceOwnerCertificateProfileBase, AndroidDeviceOwnerImportedPFXCertificateProfile, AndroidDeviceOwnerPkcsCertificateProfile, AndroidDeviceOwnerScepCertificateProfile, AndroidDeviceOwnerDerivedCredentialAuthenticationConfiguration, AndroidDeviceOwnerGeneralDeviceConfiguration, AndroidDeviceOwnerTrustedRootCertificate, AndroidDeviceOwnerWiFiConfiguration, AndroidDeviceOwnerEnterpriseWiFiConfiguration, AndroidEasEmailProfileConfiguration, AndroidForWorkCertificateProfileBase, AndroidForWorkPkcsCertificateProfile, AndroidForWorkScepCertificateProfile, AndroidForWorkCustomConfiguration, AndroidForWorkEasEmailProfileBase, AndroidForWorkGmailEasConfiguration, AndroidForWorkNineWorkEasConfiguration, AndroidForWorkGeneralDeviceConfiguration, AndroidForWorkTrustedRootCertificate, AndroidForWorkVpnConfiguration, AndroidForWorkWiFiConfiguration, AndroidForWorkEnterpriseWiFiConfiguration, AndroidGeneralDeviceConfiguration, AndroidOmaCpConfiguration, AndroidTrustedRootCertificate, AndroidVpnConfiguration, AndroidWiFiConfiguration, AndroidEnterpriseWiFiConfiguration, AndroidWorkProfileCertificateProfileBase, AndroidWorkProfilePkcsCertificateProfile, AndroidWorkProfileScepCertificateProfile, AndroidWorkProfileCustomConfiguration, AndroidWorkProfileEasEmailProfileBase, AndroidWorkProfileGmailEasConfiguration, AndroidWorkProfileNineWorkEasConfiguration, AndroidWorkProfileGeneralDeviceConfiguration, AndroidWorkProfileTrustedRootCertificate, AndroidWorkProfileVpnConfiguration, AndroidWorkProfileWiFiConfiguration, AndroidWorkProfileEnterpriseWiFiConfiguration, AospDeviceOwnerCertificateProfileBase, AospDeviceOwnerPkcsCertificateProfile, AospDeviceOwnerScepCertificateProfile, AospDeviceOwnerDeviceConfiguration, AospDeviceOwnerTrustedRootCertificate, AospDeviceOwnerWiFiConfiguration, AospDeviceOwnerEnterpriseWiFiConfiguration, AppleDeviceFeaturesConfigurationBase, IosDeviceFeaturesConfiguration, MacOSDeviceFeaturesConfiguration, AppleExpeditedCheckinConfigurationBase, IosExpeditedCheckinConfiguration, AppleVpnConfiguration, IosVpnConfiguration, IosikEv2VpnConfiguration, MacOSVpnConfiguration, EasEmailProfileConfigurationBase, IosEasEmailProfileConfiguration, Windows10EasEmailProfileConfiguration, WindowsPhoneEASEmailProfileConfiguration, EditionUpgradeConfiguration, IosCertificateProfile, IosCertificateProfileBase, IosPkcsCertificateProfile, IosScepCertificateProfile, IosImportedPFXCertificateProfile, IosCustomConfiguration, IosDerivedCredentialAuthenticationConfiguration, IosEducationDeviceConfiguration, IosEduDeviceConfiguration, IosGeneralDeviceConfiguration, IosTrustedRootCertificate, IosUpdateConfiguration, IosWiFiConfiguration, IosEnterpriseWiFiConfiguration, MacOSCertificateProfileBase, MacOSImportedPFXCertificateProfile, MacOSPkcsCertificateProfile, MacOSScepCertificateProfile, MacOSCustomAppConfiguration, MacOSCustomConfiguration, MacOSEndpointProtectionConfiguration, MacOSExtensionsConfiguration, MacOSGeneralDeviceConfiguration, MacOSSoftwareUpdateConfiguration, MacOSTrustedRootCertificate, MacOSWiFiConfiguration, MacOSEnterpriseWiFiConfiguration, MacOSWiredNetworkConfiguration, SharedPCConfiguration, UnsupportedDeviceConfiguration, VpnConfiguration, AndroidDeviceOwnerVpnConfiguration, Windows10CustomConfiguration, Windows10DeviceFirmwareConfigurationInterface, Windows10EndpointProtectionConfiguration, Windows10EnterpriseModernAppManagementConfiguration, Windows10GeneralConfiguration, Windows10NetworkBoundaryConfiguration, Windows10PFXImportCertificateProfile, Windows10SecureAssessmentConfiguration, Windows10TeamGeneralConfiguration, Windows81GeneralConfiguration, Windows81TrustedRootCertificate, Windows81WifiImportConfiguration, WindowsCertificateProfileBase, Windows10CertificateProfileBase, Windows10PkcsCertificateProfile, Windows10ImportedPFXCertificateProfile, Windows81CertificateProfileBase, Windows81SCEPCertificateProfile, WindowsPhone81ImportedPFXCertificateProfile, WindowsDefenderAdvancedThreatProtectionConfiguration, WindowsDeliveryOptimizationConfiguration, WindowsDomainJoinConfiguration, WindowsHealthMonitoringConfiguration, WindowsIdentityProtectionConfiguration, WindowsKioskConfiguration, WindowsPhone81CertificateProfileBase, WindowsPhone81SCEPCertificateProfile, WindowsPhone81CustomConfiguration, WindowsPhone81GeneralConfiguration, WindowsPhone81TrustedRootCertificate, WindowsUpdateForBusinessConfiguration, WindowsVpnConfiguration, Windows10VpnConfiguration, Windows81VpnConfiguration, WindowsPhone81VpnConfiguration, WindowsWifiConfiguration, WindowsWifiEnterpriseEAPConfiguration, WindowsWiredNetworkConfiguration]],Field(discriminator="odata_type")]]] = Field(alias="deviceConfigurations", default=None,)
	deviceConfigurationsAllManagedDeviceCertificateStates: Optional[list[ManagedAllDeviceCertificateState]] = Field(alias="deviceConfigurationsAllManagedDeviceCertificateStates", default=None,)
	deviceConfigurationUserStateSummaries: Optional[DeviceConfigurationUserStateSummary] = Field(alias="deviceConfigurationUserStateSummaries", default=None,)
	deviceCustomAttributeShellScripts: Optional[list[DeviceCustomAttributeShellScript]] = Field(alias="deviceCustomAttributeShellScripts", default=None,)
	deviceEnrollmentConfigurations: Optional[list[Annotated[Union[DeviceComanagementAuthorityConfiguration, DeviceEnrollmentLimitConfiguration, DeviceEnrollmentNotificationConfiguration, DeviceEnrollmentPlatformRestrictionConfiguration, DeviceEnrollmentPlatformRestrictionsConfiguration, DeviceEnrollmentWindowsHelloForBusinessConfiguration, Windows10EnrollmentCompletionPageConfiguration]],Field(discriminator="odata_type")]]] = Field(alias="deviceEnrollmentConfigurations", default=None,)
	deviceHealthScripts: Optional[list[DeviceHealthScript]] = Field(alias="deviceHealthScripts", default=None,)
	deviceManagementPartners: Optional[list[DeviceManagementPartner]] = Field(alias="deviceManagementPartners", default=None,)
	deviceManagementScripts: Optional[list[DeviceManagementScript]] = Field(alias="deviceManagementScripts", default=None,)
	deviceShellScripts: Optional[list[DeviceShellScript]] = Field(alias="deviceShellScripts", default=None,)
	domainJoinConnectors: Optional[list[DeviceManagementDomainJoinConnector]] = Field(alias="domainJoinConnectors", default=None,)
	elevationRequests: Optional[list[PrivilegeManagementElevationRequest]] = Field(alias="elevationRequests", default=None,)
	embeddedSIMActivationCodePools: Optional[list[EmbeddedSIMActivationCodePool]] = Field(alias="embeddedSIMActivationCodePools", default=None,)
	endpointPrivilegeManagementProvisioningStatus: Optional[EndpointPrivilegeManagementProvisioningStatus] = Field(alias="endpointPrivilegeManagementProvisioningStatus", default=None,)
	exchangeConnectors: Optional[list[DeviceManagementExchangeConnector]] = Field(alias="exchangeConnectors", default=None,)
	exchangeOnPremisesPolicies: Optional[list[DeviceManagementExchangeOnPremisesPolicy]] = Field(alias="exchangeOnPremisesPolicies", default=None,)
	exchangeOnPremisesPolicy: Optional[DeviceManagementExchangeOnPremisesPolicy] = Field(alias="exchangeOnPremisesPolicy", default=None,)
	groupPolicyCategories: Optional[list[GroupPolicyCategory]] = Field(alias="groupPolicyCategories", default=None,)
	groupPolicyConfigurations: Optional[list[GroupPolicyConfiguration]] = Field(alias="groupPolicyConfigurations", default=None,)
	groupPolicyDefinitionFiles: Optional[list[Annotated[Union[GroupPolicyUploadedDefinitionFile]],Field(discriminator="odata_type")]]] = Field(alias="groupPolicyDefinitionFiles", default=None,)
	groupPolicyDefinitions: Optional[list[GroupPolicyDefinition]] = Field(alias="groupPolicyDefinitions", default=None,)
	groupPolicyMigrationReports: Optional[list[GroupPolicyMigrationReport]] = Field(alias="groupPolicyMigrationReports", default=None,)
	groupPolicyObjectFiles: Optional[list[GroupPolicyObjectFile]] = Field(alias="groupPolicyObjectFiles", default=None,)
	groupPolicyUploadedDefinitionFiles: Optional[list[GroupPolicyUploadedDefinitionFile]] = Field(alias="groupPolicyUploadedDefinitionFiles", default=None,)
	hardwareConfigurations: Optional[list[HardwareConfiguration]] = Field(alias="hardwareConfigurations", default=None,)
	hardwarePasswordDetails: Optional[list[HardwarePasswordDetail]] = Field(alias="hardwarePasswordDetails", default=None,)
	hardwarePasswordInfo: Optional[list[HardwarePasswordInfo]] = Field(alias="hardwarePasswordInfo", default=None,)
	importedDeviceIdentities: Optional[list[Annotated[Union[ImportedDeviceIdentityResult]],Field(discriminator="odata_type")]]] = Field(alias="importedDeviceIdentities", default=None,)
	importedWindowsAutopilotDeviceIdentities: Optional[list[ImportedWindowsAutopilotDeviceIdentity]] = Field(alias="importedWindowsAutopilotDeviceIdentities", default=None,)
	intents: Optional[list[DeviceManagementIntent]] = Field(alias="intents", default=None,)
	intuneBrandingProfiles: Optional[list[IntuneBrandingProfile]] = Field(alias="intuneBrandingProfiles", default=None,)
	iosUpdateStatuses: Optional[list[IosUpdateDeviceStatus]] = Field(alias="iosUpdateStatuses", default=None,)
	macOSSoftwareUpdateAccountSummaries: Optional[list[MacOSSoftwareUpdateAccountSummary]] = Field(alias="macOSSoftwareUpdateAccountSummaries", default=None,)
	managedDeviceCleanupRules: Optional[list[ManagedDeviceCleanupRule]] = Field(alias="managedDeviceCleanupRules", default=None,)
	managedDeviceEncryptionStates: Optional[list[ManagedDeviceEncryptionState]] = Field(alias="managedDeviceEncryptionStates", default=None,)
	managedDeviceOverview: Optional[ManagedDeviceOverview] = Field(alias="managedDeviceOverview", default=None,)
	managedDevices: Optional[list[Annotated[Union[WindowsManagedDevice]],Field(discriminator="odata_type")]]] = Field(alias="managedDevices", default=None,)
	managedDeviceWindowsOSImages: Optional[list[ManagedDeviceWindowsOperatingSystemImage]] = Field(alias="managedDeviceWindowsOSImages", default=None,)
	microsoftTunnelConfigurations: Optional[list[MicrosoftTunnelConfiguration]] = Field(alias="microsoftTunnelConfigurations", default=None,)
	microsoftTunnelHealthThresholds: Optional[list[MicrosoftTunnelHealthThreshold]] = Field(alias="microsoftTunnelHealthThresholds", default=None,)
	microsoftTunnelServerLogCollectionResponses: Optional[list[MicrosoftTunnelServerLogCollectionResponse]] = Field(alias="microsoftTunnelServerLogCollectionResponses", default=None,)
	microsoftTunnelSites: Optional[list[MicrosoftTunnelSite]] = Field(alias="microsoftTunnelSites", default=None,)
	mobileAppTroubleshootingEvents: Optional[list[MobileAppTroubleshootingEvent]] = Field(alias="mobileAppTroubleshootingEvents", default=None,)
	mobileThreatDefenseConnectors: Optional[list[MobileThreatDefenseConnector]] = Field(alias="mobileThreatDefenseConnectors", default=None,)
	monitoring: Optional[DeviceManagementMonitoring] = Field(alias="monitoring", default=None,)
	ndesConnectors: Optional[list[NdesConnector]] = Field(alias="ndesConnectors", default=None,)
	notificationMessageTemplates: Optional[list[NotificationMessageTemplate]] = Field(alias="notificationMessageTemplates", default=None,)
	operationApprovalPolicies: Optional[list[OperationApprovalPolicy]] = Field(alias="operationApprovalPolicies", default=None,)
	operationApprovalRequests: Optional[list[OperationApprovalRequest]] = Field(alias="operationApprovalRequests", default=None,)
	privilegeManagementElevations: Optional[list[PrivilegeManagementElevation]] = Field(alias="privilegeManagementElevations", default=None,)
	remoteActionAudits: Optional[list[RemoteActionAudit]] = Field(alias="remoteActionAudits", default=None,)
	remoteAssistancePartners: Optional[list[RemoteAssistancePartner]] = Field(alias="remoteAssistancePartners", default=None,)
	remoteAssistanceSettings: Optional[RemoteAssistanceSettings] = Field(alias="remoteAssistanceSettings", default=None,)
	reports: Optional[DeviceManagementReports] = Field(alias="reports", default=None,)
	resourceAccessProfiles: Optional[list[Annotated[Union[Windows10XCertificateProfile, Windows10XSCEPCertificateProfile, Windows10XTrustedRootCertificate, Windows10XVpnConfiguration, Windows10XWifiConfiguration]],Field(discriminator="odata_type")]]] = Field(alias="resourceAccessProfiles", default=None,)
	resourceOperations: Optional[list[ResourceOperation]] = Field(alias="resourceOperations", default=None,)
	reusablePolicySettings: Optional[list[DeviceManagementReusablePolicySetting]] = Field(alias="reusablePolicySettings", default=None,)
	reusableSettings: Optional[list[Annotated[Union[DeviceManagementConfigurationChoiceSettingDefinition, DeviceManagementConfigurationChoiceSettingCollectionDefinition, DeviceManagementConfigurationRedirectSettingDefinition, DeviceManagementConfigurationSettingGroupDefinition, DeviceManagementConfigurationSettingGroupCollectionDefinition, DeviceManagementConfigurationSimpleSettingDefinition, DeviceManagementConfigurationSimpleSettingCollectionDefinition]],Field(discriminator="odata_type")]]] = Field(alias="reusableSettings", default=None,)
	roleAssignments: Optional[list[DeviceAndAppManagementRoleAssignment]] = Field(alias="roleAssignments", default=None,)
	roleDefinitions: Optional[list[Annotated[Union[DeviceAndAppManagementRoleDefinition]],Field(discriminator="odata_type")]]] = Field(alias="roleDefinitions", default=None,)
	roleScopeTags: Optional[list[RoleScopeTag]] = Field(alias="roleScopeTags", default=None,)
	serviceNowConnections: Optional[list[ServiceNowConnection]] = Field(alias="serviceNowConnections", default=None,)
	settingDefinitions: Optional[list[Annotated[Union[DeviceManagementAbstractComplexSettingDefinition, DeviceManagementCollectionSettingDefinition, DeviceManagementComplexSettingDefinition]],Field(discriminator="odata_type")]]] = Field(alias="settingDefinitions", default=None,)
	softwareUpdateStatusSummary: Optional[SoftwareUpdateStatusSummary] = Field(alias="softwareUpdateStatusSummary", default=None,)
	telecomExpenseManagementPartners: Optional[list[TelecomExpenseManagementPartner]] = Field(alias="telecomExpenseManagementPartners", default=None,)
	templateInsights: Optional[list[DeviceManagementTemplateInsightsDefinition]] = Field(alias="templateInsights", default=None,)
	templates: Optional[list[Annotated[Union[SecurityBaselineTemplate]],Field(discriminator="odata_type")]]] = Field(alias="templates", default=None,)
	templateSettings: Optional[list[DeviceManagementConfigurationSettingTemplate]] = Field(alias="templateSettings", default=None,)
	tenantAttachRBAC: Optional[TenantAttachRBAC] = Field(alias="tenantAttachRBAC", default=None,)
	termsAndConditions: Optional[list[TermsAndConditions]] = Field(alias="termsAndConditions", default=None,)
	troubleshootingEvents: Optional[list[Annotated[Union[AppleVppTokenTroubleshootingEvent, EnrollmentTroubleshootingEvent, MobileAppTroubleshootingEvent]],Field(discriminator="odata_type")]]] = Field(alias="troubleshootingEvents", default=None,)
	userExperienceAnalyticsAnomaly: Optional[list[UserExperienceAnalyticsAnomaly]] = Field(alias="userExperienceAnalyticsAnomaly", default=None,)
	userExperienceAnalyticsAnomalyCorrelationGroupOverview: Optional[list[UserExperienceAnalyticsAnomalyCorrelationGroupOverview]] = Field(alias="userExperienceAnalyticsAnomalyCorrelationGroupOverview", default=None,)
	userExperienceAnalyticsAnomalyDevice: Optional[list[UserExperienceAnalyticsAnomalyDevice]] = Field(alias="userExperienceAnalyticsAnomalyDevice", default=None,)
	userExperienceAnalyticsAppHealthApplicationPerformance: Optional[list[UserExperienceAnalyticsAppHealthApplicationPerformance]] = Field(alias="userExperienceAnalyticsAppHealthApplicationPerformance", default=None,)
	userExperienceAnalyticsAppHealthApplicationPerformanceByAppVersion: Optional[list[UserExperienceAnalyticsAppHealthAppPerformanceByAppVersion]] = Field(alias="userExperienceAnalyticsAppHealthApplicationPerformanceByAppVersion", default=None,)
	userExperienceAnalyticsAppHealthApplicationPerformanceByAppVersionDetails: Optional[list[UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionDetails]] = Field(alias="userExperienceAnalyticsAppHealthApplicationPerformanceByAppVersionDetails", default=None,)
	userExperienceAnalyticsAppHealthApplicationPerformanceByAppVersionDeviceId: Optional[list[UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionDeviceId]] = Field(alias="userExperienceAnalyticsAppHealthApplicationPerformanceByAppVersionDeviceId", default=None,)
	userExperienceAnalyticsAppHealthApplicationPerformanceByOSVersion: Optional[list[UserExperienceAnalyticsAppHealthAppPerformanceByOSVersion]] = Field(alias="userExperienceAnalyticsAppHealthApplicationPerformanceByOSVersion", default=None,)
	userExperienceAnalyticsAppHealthDeviceModelPerformance: Optional[list[UserExperienceAnalyticsAppHealthDeviceModelPerformance]] = Field(alias="userExperienceAnalyticsAppHealthDeviceModelPerformance", default=None,)
	userExperienceAnalyticsAppHealthDevicePerformance: Optional[list[UserExperienceAnalyticsAppHealthDevicePerformance]] = Field(alias="userExperienceAnalyticsAppHealthDevicePerformance", default=None,)
	userExperienceAnalyticsAppHealthDevicePerformanceDetails: Optional[list[UserExperienceAnalyticsAppHealthDevicePerformanceDetails]] = Field(alias="userExperienceAnalyticsAppHealthDevicePerformanceDetails", default=None,)
	userExperienceAnalyticsAppHealthOSVersionPerformance: Optional[list[UserExperienceAnalyticsAppHealthOSVersionPerformance]] = Field(alias="userExperienceAnalyticsAppHealthOSVersionPerformance", default=None,)
	userExperienceAnalyticsAppHealthOverview: Optional[UserExperienceAnalyticsCategory] = Field(alias="userExperienceAnalyticsAppHealthOverview", default=None,)
	userExperienceAnalyticsBaselines: Optional[list[UserExperienceAnalyticsBaseline]] = Field(alias="userExperienceAnalyticsBaselines", default=None,)
	userExperienceAnalyticsBatteryHealthAppImpact: Optional[list[UserExperienceAnalyticsBatteryHealthAppImpact]] = Field(alias="userExperienceAnalyticsBatteryHealthAppImpact", default=None,)
	userExperienceAnalyticsBatteryHealthCapacityDetails: Optional[UserExperienceAnalyticsBatteryHealthCapacityDetails] = Field(alias="userExperienceAnalyticsBatteryHealthCapacityDetails", default=None,)
	userExperienceAnalyticsBatteryHealthDeviceAppImpact: Optional[list[UserExperienceAnalyticsBatteryHealthDeviceAppImpact]] = Field(alias="userExperienceAnalyticsBatteryHealthDeviceAppImpact", default=None,)
	userExperienceAnalyticsBatteryHealthDevicePerformance: Optional[list[UserExperienceAnalyticsBatteryHealthDevicePerformance]] = Field(alias="userExperienceAnalyticsBatteryHealthDevicePerformance", default=None,)
	userExperienceAnalyticsBatteryHealthDeviceRuntimeHistory: Optional[list[UserExperienceAnalyticsBatteryHealthDeviceRuntimeHistory]] = Field(alias="userExperienceAnalyticsBatteryHealthDeviceRuntimeHistory", default=None,)
	userExperienceAnalyticsBatteryHealthModelPerformance: Optional[list[UserExperienceAnalyticsBatteryHealthModelPerformance]] = Field(alias="userExperienceAnalyticsBatteryHealthModelPerformance", default=None,)
	userExperienceAnalyticsBatteryHealthOsPerformance: Optional[list[UserExperienceAnalyticsBatteryHealthOsPerformance]] = Field(alias="userExperienceAnalyticsBatteryHealthOsPerformance", default=None,)
	userExperienceAnalyticsBatteryHealthRuntimeDetails: Optional[UserExperienceAnalyticsBatteryHealthRuntimeDetails] = Field(alias="userExperienceAnalyticsBatteryHealthRuntimeDetails", default=None,)
	userExperienceAnalyticsCategories: Optional[list[UserExperienceAnalyticsCategory]] = Field(alias="userExperienceAnalyticsCategories", default=None,)
	userExperienceAnalyticsDeviceMetricHistory: Optional[list[UserExperienceAnalyticsMetricHistory]] = Field(alias="userExperienceAnalyticsDeviceMetricHistory", default=None,)
	userExperienceAnalyticsDevicePerformance: Optional[list[UserExperienceAnalyticsDevicePerformance]] = Field(alias="userExperienceAnalyticsDevicePerformance", default=None,)
	userExperienceAnalyticsDeviceScope: Optional[UserExperienceAnalyticsDeviceScope] = Field(alias="userExperienceAnalyticsDeviceScope", default=None,)
	userExperienceAnalyticsDeviceScopes: Optional[list[UserExperienceAnalyticsDeviceScope]] = Field(alias="userExperienceAnalyticsDeviceScopes", default=None,)
	userExperienceAnalyticsDeviceScores: Optional[list[UserExperienceAnalyticsDeviceScores]] = Field(alias="userExperienceAnalyticsDeviceScores", default=None,)
	userExperienceAnalyticsDeviceStartupHistory: Optional[list[UserExperienceAnalyticsDeviceStartupHistory]] = Field(alias="userExperienceAnalyticsDeviceStartupHistory", default=None,)
	userExperienceAnalyticsDeviceStartupProcesses: Optional[list[UserExperienceAnalyticsDeviceStartupProcess]] = Field(alias="userExperienceAnalyticsDeviceStartupProcesses", default=None,)
	userExperienceAnalyticsDeviceStartupProcessPerformance: Optional[list[UserExperienceAnalyticsDeviceStartupProcessPerformance]] = Field(alias="userExperienceAnalyticsDeviceStartupProcessPerformance", default=None,)
	userExperienceAnalyticsDevicesWithoutCloudIdentity: Optional[list[UserExperienceAnalyticsDeviceWithoutCloudIdentity]] = Field(alias="userExperienceAnalyticsDevicesWithoutCloudIdentity", default=None,)
	userExperienceAnalyticsDeviceTimelineEvent: Optional[list[UserExperienceAnalyticsDeviceTimelineEvent]] = Field(alias="userExperienceAnalyticsDeviceTimelineEvent", default=None,)
	userExperienceAnalyticsImpactingProcess: Optional[list[UserExperienceAnalyticsImpactingProcess]] = Field(alias="userExperienceAnalyticsImpactingProcess", default=None,)
	userExperienceAnalyticsMetricHistory: Optional[list[UserExperienceAnalyticsMetricHistory]] = Field(alias="userExperienceAnalyticsMetricHistory", default=None,)
	userExperienceAnalyticsModelScores: Optional[list[UserExperienceAnalyticsModelScores]] = Field(alias="userExperienceAnalyticsModelScores", default=None,)
	userExperienceAnalyticsNotAutopilotReadyDevice: Optional[list[UserExperienceAnalyticsNotAutopilotReadyDevice]] = Field(alias="userExperienceAnalyticsNotAutopilotReadyDevice", default=None,)
	userExperienceAnalyticsOverview: Optional[UserExperienceAnalyticsOverview] = Field(alias="userExperienceAnalyticsOverview", default=None,)
	userExperienceAnalyticsRemoteConnection: Optional[list[UserExperienceAnalyticsRemoteConnection]] = Field(alias="userExperienceAnalyticsRemoteConnection", default=None,)
	userExperienceAnalyticsResourcePerformance: Optional[list[UserExperienceAnalyticsResourcePerformance]] = Field(alias="userExperienceAnalyticsResourcePerformance", default=None,)
	userExperienceAnalyticsScoreHistory: Optional[list[UserExperienceAnalyticsScoreHistory]] = Field(alias="userExperienceAnalyticsScoreHistory", default=None,)
	userExperienceAnalyticsWorkFromAnywhereHardwareReadinessMetric: Optional[UserExperienceAnalyticsWorkFromAnywhereHardwareReadinessMetric] = Field(alias="userExperienceAnalyticsWorkFromAnywhereHardwareReadinessMetric", default=None,)
	userExperienceAnalyticsWorkFromAnywhereMetrics: Optional[list[UserExperienceAnalyticsWorkFromAnywhereMetric]] = Field(alias="userExperienceAnalyticsWorkFromAnywhereMetrics", default=None,)
	userExperienceAnalyticsWorkFromAnywhereModelPerformance: Optional[list[UserExperienceAnalyticsWorkFromAnywhereModelPerformance]] = Field(alias="userExperienceAnalyticsWorkFromAnywhereModelPerformance", default=None,)
	userPfxCertificates: Optional[list[UserPFXCertificate]] = Field(alias="userPfxCertificates", default=None,)
	virtualEndpoint: Optional[VirtualEndpoint] = Field(alias="virtualEndpoint", default=None,)
	windowsAutopilotDeploymentProfiles: Optional[list[Annotated[Union[ActiveDirectoryWindowsAutopilotDeploymentProfile, AzureADWindowsAutopilotDeploymentProfile]],Field(discriminator="odata_type")]]] = Field(alias="windowsAutopilotDeploymentProfiles", default=None,)
	windowsAutopilotDeviceIdentities: Optional[list[WindowsAutopilotDeviceIdentity]] = Field(alias="windowsAutopilotDeviceIdentities", default=None,)
	windowsAutopilotSettings: Optional[WindowsAutopilotSettings] = Field(alias="windowsAutopilotSettings", default=None,)
	windowsDriverUpdateProfiles: Optional[list[WindowsDriverUpdateProfile]] = Field(alias="windowsDriverUpdateProfiles", default=None,)
	windowsFeatureUpdateProfiles: Optional[list[WindowsFeatureUpdateProfile]] = Field(alias="windowsFeatureUpdateProfiles", default=None,)
	windowsInformationProtectionAppLearningSummaries: Optional[list[WindowsInformationProtectionAppLearningSummary]] = Field(alias="windowsInformationProtectionAppLearningSummaries", default=None,)
	windowsInformationProtectionNetworkLearningSummaries: Optional[list[WindowsInformationProtectionNetworkLearningSummary]] = Field(alias="windowsInformationProtectionNetworkLearningSummaries", default=None,)
	windowsMalwareInformation: Optional[list[WindowsMalwareInformation]] = Field(alias="windowsMalwareInformation", default=None,)
	windowsQualityUpdatePolicies: Optional[list[WindowsQualityUpdatePolicy]] = Field(alias="windowsQualityUpdatePolicies", default=None,)
	windowsQualityUpdateProfiles: Optional[list[WindowsQualityUpdateProfile]] = Field(alias="windowsQualityUpdateProfiles", default=None,)
	windowsUpdateCatalogItems: Optional[list[Annotated[Union[WindowsFeatureUpdateCatalogItem, WindowsQualityUpdateCatalogItem]],Field(discriminator="odata_type")]]] = Field(alias="windowsUpdateCatalogItems", default=None,)
	zebraFotaArtifacts: Optional[list[ZebraFotaArtifact]] = Field(alias="zebraFotaArtifacts", default=None,)
	zebraFotaConnector: Optional[ZebraFotaConnector] = Field(alias="zebraFotaConnector", default=None,)
	zebraFotaDeployments: Optional[list[ZebraFotaDeployment]] = Field(alias="zebraFotaDeployments", default=None,)

from .admin_consent import AdminConsent
from .connector_status_details import ConnectorStatusDetails
from .data_processor_service_for_windows_features_onboarding import DataProcessorServiceForWindowsFeaturesOnboarding
from .device_protection_overview import DeviceProtectionOverview
from .intune_brand import IntuneBrand
from .managed_device_cleanup_settings import ManagedDeviceCleanupSettings
from .device_management_settings import DeviceManagementSettings
from .device_management_subscriptions import DeviceManagementSubscriptions
from .device_management_subscription_state import DeviceManagementSubscriptionState
from .user_experience_analytics_anomaly_severity_overview import UserExperienceAnalyticsAnomalySeverityOverview
from .user_experience_analytics_settings import UserExperienceAnalyticsSettings
from .windows_malware_overview import WindowsMalwareOverview
from .advanced_threat_protection_onboarding_state_summary import AdvancedThreatProtectionOnboardingStateSummary
from .android_device_owner_enrollment_profile import AndroidDeviceOwnerEnrollmentProfile
from .android_for_work_app_configuration_schema import AndroidForWorkAppConfigurationSchema
from .android_for_work_enrollment_profile import AndroidForWorkEnrollmentProfile
from .android_for_work_settings import AndroidForWorkSettings
from .android_managed_store_account_enterprise_settings import AndroidManagedStoreAccountEnterpriseSettings
from .android_managed_store_app_configuration_schema import AndroidManagedStoreAppConfigurationSchema
from .apple_push_notification_certificate import ApplePushNotificationCertificate
from .apple_user_initiated_enrollment_profile import AppleUserInitiatedEnrollmentProfile
from .payload_compatible_assignment_filter import PayloadCompatibleAssignmentFilter
from .audit_event import AuditEvent
from .device_management_autopilot_event import DeviceManagementAutopilotEvent
from .cart_to_class_association import CartToClassAssociation
from .device_management_intent_setting_category import DeviceManagementIntentSettingCategory
from .device_management_template_setting_category import DeviceManagementTemplateSettingCategory
from .certificate_connector_details import CertificateConnectorDetails
from .chrome_o_s_onboarding_settings import ChromeOSOnboardingSettings
from .cloud_certification_authority import CloudCertificationAuthority
from .cloud_certification_authority_leaf_certificate import CloudCertificationAuthorityLeafCertificate
from .cloud_p_c_connectivity_issue import CloudPCConnectivityIssue
from .windows_managed_device import WindowsManagedDevice
from .comanagement_eligible_device import ComanagementEligibleDevice
from .device_management_configuration_category import DeviceManagementConfigurationCategory
from .compliance_management_partner import ComplianceManagementPartner
from .device_management_compliance_policy import DeviceManagementCompliancePolicy
from .device_management_configuration_choice_setting_definition import DeviceManagementConfigurationChoiceSettingDefinition
from .device_management_configuration_choice_setting_collection_definition import DeviceManagementConfigurationChoiceSettingCollectionDefinition
from .device_management_configuration_redirect_setting_definition import DeviceManagementConfigurationRedirectSettingDefinition
from .device_management_configuration_setting_group_definition import DeviceManagementConfigurationSettingGroupDefinition
from .device_management_configuration_setting_group_collection_definition import DeviceManagementConfigurationSettingGroupCollectionDefinition
from .device_management_configuration_simple_setting_definition import DeviceManagementConfigurationSimpleSettingDefinition
from .device_management_configuration_simple_setting_collection_definition import DeviceManagementConfigurationSimpleSettingCollectionDefinition
from .on_premises_conditional_access_settings import OnPremisesConditionalAccessSettings
from .config_manager_collection import ConfigManagerCollection
from .device_management_configuration_category import DeviceManagementConfigurationCategory
from .device_management_configuration_policy import DeviceManagementConfigurationPolicy
from .device_management_configuration_policy_template import DeviceManagementConfigurationPolicyTemplate
from .device_management_configuration_choice_setting_definition import DeviceManagementConfigurationChoiceSettingDefinition
from .device_management_configuration_choice_setting_collection_definition import DeviceManagementConfigurationChoiceSettingCollectionDefinition
from .device_management_configuration_redirect_setting_definition import DeviceManagementConfigurationRedirectSettingDefinition
from .device_management_configuration_setting_group_definition import DeviceManagementConfigurationSettingGroupDefinition
from .device_management_configuration_setting_group_collection_definition import DeviceManagementConfigurationSettingGroupCollectionDefinition
from .device_management_configuration_simple_setting_definition import DeviceManagementConfigurationSimpleSettingDefinition
from .device_management_configuration_simple_setting_collection_definition import DeviceManagementConfigurationSimpleSettingCollectionDefinition
from .data_sharing_consent import DataSharingConsent
from .dep_onboarding_setting import DepOnboardingSetting
from .device_management_derived_credential_settings import DeviceManagementDerivedCredentialSettings
from .detected_app import DetectedApp
from .device_category import DeviceCategory
from .android_compliance_policy import AndroidCompliancePolicy
from .android_device_owner_compliance_policy import AndroidDeviceOwnerCompliancePolicy
from .android_for_work_compliance_policy import AndroidForWorkCompliancePolicy
from .android_work_profile_compliance_policy import AndroidWorkProfileCompliancePolicy
from .aosp_device_owner_compliance_policy import AospDeviceOwnerCompliancePolicy
from .default_device_compliance_policy import DefaultDeviceCompliancePolicy
from .ios_compliance_policy import IosCompliancePolicy
from .mac_o_s_compliance_policy import MacOSCompliancePolicy
from .windows10_compliance_policy import Windows10CompliancePolicy
from .windows10_mobile_compliance_policy import Windows10MobileCompliancePolicy
from .windows81_compliance_policy import Windows81CompliancePolicy
from .windows_phone81_compliance_policy import WindowsPhone81CompliancePolicy
from .device_compliance_policy_device_state_summary import DeviceCompliancePolicyDeviceStateSummary
from .device_compliance_policy_setting_state_summary import DeviceCompliancePolicySettingStateSummary
from .device_compliance_script import DeviceComplianceScript
from .device_configuration_conflict_summary import DeviceConfigurationConflictSummary
from .device_configuration_device_state_summary import DeviceConfigurationDeviceStateSummary
from .restricted_apps_violation import RestrictedAppsViolation
from .android_certificate_profile_base import AndroidCertificateProfileBase
from .android_for_work_imported_p_f_x_certificate_profile import AndroidForWorkImportedPFXCertificateProfile
from .android_imported_p_f_x_certificate_profile import AndroidImportedPFXCertificateProfile
from .android_pkcs_certificate_profile import AndroidPkcsCertificateProfile
from .android_scep_certificate_profile import AndroidScepCertificateProfile
from .android_custom_configuration import AndroidCustomConfiguration
from .android_device_owner_certificate_profile_base import AndroidDeviceOwnerCertificateProfileBase
from .android_device_owner_imported_p_f_x_certificate_profile import AndroidDeviceOwnerImportedPFXCertificateProfile
from .android_device_owner_pkcs_certificate_profile import AndroidDeviceOwnerPkcsCertificateProfile
from .android_device_owner_scep_certificate_profile import AndroidDeviceOwnerScepCertificateProfile
from .android_device_owner_derived_credential_authentication_configuration import AndroidDeviceOwnerDerivedCredentialAuthenticationConfiguration
from .android_device_owner_general_device_configuration import AndroidDeviceOwnerGeneralDeviceConfiguration
from .android_device_owner_trusted_root_certificate import AndroidDeviceOwnerTrustedRootCertificate
from .android_device_owner_wi_fi_configuration import AndroidDeviceOwnerWiFiConfiguration
from .android_device_owner_enterprise_wi_fi_configuration import AndroidDeviceOwnerEnterpriseWiFiConfiguration
from .android_eas_email_profile_configuration import AndroidEasEmailProfileConfiguration
from .android_for_work_certificate_profile_base import AndroidForWorkCertificateProfileBase
from .android_for_work_pkcs_certificate_profile import AndroidForWorkPkcsCertificateProfile
from .android_for_work_scep_certificate_profile import AndroidForWorkScepCertificateProfile
from .android_for_work_custom_configuration import AndroidForWorkCustomConfiguration
from .android_for_work_eas_email_profile_base import AndroidForWorkEasEmailProfileBase
from .android_for_work_gmail_eas_configuration import AndroidForWorkGmailEasConfiguration
from .android_for_work_nine_work_eas_configuration import AndroidForWorkNineWorkEasConfiguration
from .android_for_work_general_device_configuration import AndroidForWorkGeneralDeviceConfiguration
from .android_for_work_trusted_root_certificate import AndroidForWorkTrustedRootCertificate
from .android_for_work_vpn_configuration import AndroidForWorkVpnConfiguration
from .android_for_work_wi_fi_configuration import AndroidForWorkWiFiConfiguration
from .android_for_work_enterprise_wi_fi_configuration import AndroidForWorkEnterpriseWiFiConfiguration
from .android_general_device_configuration import AndroidGeneralDeviceConfiguration
from .android_oma_cp_configuration import AndroidOmaCpConfiguration
from .android_trusted_root_certificate import AndroidTrustedRootCertificate
from .android_vpn_configuration import AndroidVpnConfiguration
from .android_wi_fi_configuration import AndroidWiFiConfiguration
from .android_enterprise_wi_fi_configuration import AndroidEnterpriseWiFiConfiguration
from .android_work_profile_certificate_profile_base import AndroidWorkProfileCertificateProfileBase
from .android_work_profile_pkcs_certificate_profile import AndroidWorkProfilePkcsCertificateProfile
from .android_work_profile_scep_certificate_profile import AndroidWorkProfileScepCertificateProfile
from .android_work_profile_custom_configuration import AndroidWorkProfileCustomConfiguration
from .android_work_profile_eas_email_profile_base import AndroidWorkProfileEasEmailProfileBase
from .android_work_profile_gmail_eas_configuration import AndroidWorkProfileGmailEasConfiguration
from .android_work_profile_nine_work_eas_configuration import AndroidWorkProfileNineWorkEasConfiguration
from .android_work_profile_general_device_configuration import AndroidWorkProfileGeneralDeviceConfiguration
from .android_work_profile_trusted_root_certificate import AndroidWorkProfileTrustedRootCertificate
from .android_work_profile_vpn_configuration import AndroidWorkProfileVpnConfiguration
from .android_work_profile_wi_fi_configuration import AndroidWorkProfileWiFiConfiguration
from .android_work_profile_enterprise_wi_fi_configuration import AndroidWorkProfileEnterpriseWiFiConfiguration
from .aosp_device_owner_certificate_profile_base import AospDeviceOwnerCertificateProfileBase
from .aosp_device_owner_pkcs_certificate_profile import AospDeviceOwnerPkcsCertificateProfile
from .aosp_device_owner_scep_certificate_profile import AospDeviceOwnerScepCertificateProfile
from .aosp_device_owner_device_configuration import AospDeviceOwnerDeviceConfiguration
from .aosp_device_owner_trusted_root_certificate import AospDeviceOwnerTrustedRootCertificate
from .aosp_device_owner_wi_fi_configuration import AospDeviceOwnerWiFiConfiguration
from .aosp_device_owner_enterprise_wi_fi_configuration import AospDeviceOwnerEnterpriseWiFiConfiguration
from .apple_device_features_configuration_base import AppleDeviceFeaturesConfigurationBase
from .ios_device_features_configuration import IosDeviceFeaturesConfiguration
from .mac_o_s_device_features_configuration import MacOSDeviceFeaturesConfiguration
from .apple_expedited_checkin_configuration_base import AppleExpeditedCheckinConfigurationBase
from .ios_expedited_checkin_configuration import IosExpeditedCheckinConfiguration
from .apple_vpn_configuration import AppleVpnConfiguration
from .ios_vpn_configuration import IosVpnConfiguration
from .iosik_ev2_vpn_configuration import IosikEv2VpnConfiguration
from .mac_o_s_vpn_configuration import MacOSVpnConfiguration
from .eas_email_profile_configuration_base import EasEmailProfileConfigurationBase
from .ios_eas_email_profile_configuration import IosEasEmailProfileConfiguration
from .windows10_eas_email_profile_configuration import Windows10EasEmailProfileConfiguration
from .windows_phone_e_a_s_email_profile_configuration import WindowsPhoneEASEmailProfileConfiguration
from .edition_upgrade_configuration import EditionUpgradeConfiguration
from .ios_certificate_profile import IosCertificateProfile
from .ios_certificate_profile_base import IosCertificateProfileBase
from .ios_pkcs_certificate_profile import IosPkcsCertificateProfile
from .ios_scep_certificate_profile import IosScepCertificateProfile
from .ios_imported_p_f_x_certificate_profile import IosImportedPFXCertificateProfile
from .ios_custom_configuration import IosCustomConfiguration
from .ios_derived_credential_authentication_configuration import IosDerivedCredentialAuthenticationConfiguration
from .ios_education_device_configuration import IosEducationDeviceConfiguration
from .ios_edu_device_configuration import IosEduDeviceConfiguration
from .ios_general_device_configuration import IosGeneralDeviceConfiguration
from .ios_trusted_root_certificate import IosTrustedRootCertificate
from .ios_update_configuration import IosUpdateConfiguration
from .ios_wi_fi_configuration import IosWiFiConfiguration
from .ios_enterprise_wi_fi_configuration import IosEnterpriseWiFiConfiguration
from .mac_o_s_certificate_profile_base import MacOSCertificateProfileBase
from .mac_o_s_imported_p_f_x_certificate_profile import MacOSImportedPFXCertificateProfile
from .mac_o_s_pkcs_certificate_profile import MacOSPkcsCertificateProfile
from .mac_o_s_scep_certificate_profile import MacOSScepCertificateProfile
from .mac_o_s_custom_app_configuration import MacOSCustomAppConfiguration
from .mac_o_s_custom_configuration import MacOSCustomConfiguration
from .mac_o_s_endpoint_protection_configuration import MacOSEndpointProtectionConfiguration
from .mac_o_s_extensions_configuration import MacOSExtensionsConfiguration
from .mac_o_s_general_device_configuration import MacOSGeneralDeviceConfiguration
from .mac_o_s_software_update_configuration import MacOSSoftwareUpdateConfiguration
from .mac_o_s_trusted_root_certificate import MacOSTrustedRootCertificate
from .mac_o_s_wi_fi_configuration import MacOSWiFiConfiguration
from .mac_o_s_enterprise_wi_fi_configuration import MacOSEnterpriseWiFiConfiguration
from .mac_o_s_wired_network_configuration import MacOSWiredNetworkConfiguration
from .shared_p_c_configuration import SharedPCConfiguration
from .unsupported_device_configuration import UnsupportedDeviceConfiguration
from .vpn_configuration import VpnConfiguration
from .android_device_owner_vpn_configuration import AndroidDeviceOwnerVpnConfiguration
from .windows10_custom_configuration import Windows10CustomConfiguration
from .windows10_device_firmware_configuration_interface import Windows10DeviceFirmwareConfigurationInterface
from .windows10_endpoint_protection_configuration import Windows10EndpointProtectionConfiguration
from .windows10_enterprise_modern_app_management_configuration import Windows10EnterpriseModernAppManagementConfiguration
from .windows10_general_configuration import Windows10GeneralConfiguration
from .windows10_network_boundary_configuration import Windows10NetworkBoundaryConfiguration
from .windows10_p_f_x_import_certificate_profile import Windows10PFXImportCertificateProfile
from .windows10_secure_assessment_configuration import Windows10SecureAssessmentConfiguration
from .windows10_team_general_configuration import Windows10TeamGeneralConfiguration
from .windows81_general_configuration import Windows81GeneralConfiguration
from .windows81_trusted_root_certificate import Windows81TrustedRootCertificate
from .windows81_wifi_import_configuration import Windows81WifiImportConfiguration
from .windows_certificate_profile_base import WindowsCertificateProfileBase
from .windows10_certificate_profile_base import Windows10CertificateProfileBase
from .windows10_pkcs_certificate_profile import Windows10PkcsCertificateProfile
from .windows10_imported_p_f_x_certificate_profile import Windows10ImportedPFXCertificateProfile
from .windows81_certificate_profile_base import Windows81CertificateProfileBase
from .windows81_s_c_e_p_certificate_profile import Windows81SCEPCertificateProfile
from .windows_phone81_imported_p_f_x_certificate_profile import WindowsPhone81ImportedPFXCertificateProfile
from .windows_defender_advanced_threat_protection_configuration import WindowsDefenderAdvancedThreatProtectionConfiguration
from .windows_delivery_optimization_configuration import WindowsDeliveryOptimizationConfiguration
from .windows_domain_join_configuration import WindowsDomainJoinConfiguration
from .windows_health_monitoring_configuration import WindowsHealthMonitoringConfiguration
from .windows_identity_protection_configuration import WindowsIdentityProtectionConfiguration
from .windows_kiosk_configuration import WindowsKioskConfiguration
from .windows_phone81_certificate_profile_base import WindowsPhone81CertificateProfileBase
from .windows_phone81_s_c_e_p_certificate_profile import WindowsPhone81SCEPCertificateProfile
from .windows_phone81_custom_configuration import WindowsPhone81CustomConfiguration
from .windows_phone81_general_configuration import WindowsPhone81GeneralConfiguration
from .windows_phone81_trusted_root_certificate import WindowsPhone81TrustedRootCertificate
from .windows_update_for_business_configuration import WindowsUpdateForBusinessConfiguration
from .windows_vpn_configuration import WindowsVpnConfiguration
from .windows10_vpn_configuration import Windows10VpnConfiguration
from .windows81_vpn_configuration import Windows81VpnConfiguration
from .windows_phone81_vpn_configuration import WindowsPhone81VpnConfiguration
from .windows_wifi_configuration import WindowsWifiConfiguration
from .windows_wifi_enterprise_e_a_p_configuration import WindowsWifiEnterpriseEAPConfiguration
from .windows_wired_network_configuration import WindowsWiredNetworkConfiguration
from .managed_all_device_certificate_state import ManagedAllDeviceCertificateState
from .device_configuration_user_state_summary import DeviceConfigurationUserStateSummary
from .device_custom_attribute_shell_script import DeviceCustomAttributeShellScript
from .device_comanagement_authority_configuration import DeviceComanagementAuthorityConfiguration
from .device_enrollment_limit_configuration import DeviceEnrollmentLimitConfiguration
from .device_enrollment_notification_configuration import DeviceEnrollmentNotificationConfiguration
from .device_enrollment_platform_restriction_configuration import DeviceEnrollmentPlatformRestrictionConfiguration
from .device_enrollment_platform_restrictions_configuration import DeviceEnrollmentPlatformRestrictionsConfiguration
from .device_enrollment_windows_hello_for_business_configuration import DeviceEnrollmentWindowsHelloForBusinessConfiguration
from .windows10_enrollment_completion_page_configuration import Windows10EnrollmentCompletionPageConfiguration
from .device_health_script import DeviceHealthScript
from .device_management_partner import DeviceManagementPartner
from .device_management_script import DeviceManagementScript
from .device_shell_script import DeviceShellScript
from .device_management_domain_join_connector import DeviceManagementDomainJoinConnector
from .privilege_management_elevation_request import PrivilegeManagementElevationRequest
from .embedded_s_i_m_activation_code_pool import EmbeddedSIMActivationCodePool
from .endpoint_privilege_management_provisioning_status import EndpointPrivilegeManagementProvisioningStatus
from .device_management_exchange_connector import DeviceManagementExchangeConnector
from .device_management_exchange_on_premises_policy import DeviceManagementExchangeOnPremisesPolicy
from .device_management_exchange_on_premises_policy import DeviceManagementExchangeOnPremisesPolicy
from .group_policy_category import GroupPolicyCategory
from .group_policy_configuration import GroupPolicyConfiguration
from .group_policy_uploaded_definition_file import GroupPolicyUploadedDefinitionFile
from .group_policy_definition import GroupPolicyDefinition
from .group_policy_migration_report import GroupPolicyMigrationReport
from .group_policy_object_file import GroupPolicyObjectFile
from .group_policy_uploaded_definition_file import GroupPolicyUploadedDefinitionFile
from .hardware_configuration import HardwareConfiguration
from .hardware_password_detail import HardwarePasswordDetail
from .hardware_password_info import HardwarePasswordInfo
from .imported_device_identity_result import ImportedDeviceIdentityResult
from .imported_windows_autopilot_device_identity import ImportedWindowsAutopilotDeviceIdentity
from .device_management_intent import DeviceManagementIntent
from .intune_branding_profile import IntuneBrandingProfile
from .ios_update_device_status import IosUpdateDeviceStatus
from .mac_o_s_software_update_account_summary import MacOSSoftwareUpdateAccountSummary
from .managed_device_cleanup_rule import ManagedDeviceCleanupRule
from .managed_device_encryption_state import ManagedDeviceEncryptionState
from .managed_device_overview import ManagedDeviceOverview
from .windows_managed_device import WindowsManagedDevice
from .managed_device_windows_operating_system_image import ManagedDeviceWindowsOperatingSystemImage
from .microsoft_tunnel_configuration import MicrosoftTunnelConfiguration
from .microsoft_tunnel_health_threshold import MicrosoftTunnelHealthThreshold
from .microsoft_tunnel_server_log_collection_response import MicrosoftTunnelServerLogCollectionResponse
from .microsoft_tunnel_site import MicrosoftTunnelSite
from .mobile_app_troubleshooting_event import MobileAppTroubleshootingEvent
from .mobile_threat_defense_connector import MobileThreatDefenseConnector
from .device_management_monitoring import DeviceManagementMonitoring
from .ndes_connector import NdesConnector
from .notification_message_template import NotificationMessageTemplate
from .operation_approval_policy import OperationApprovalPolicy
from .operation_approval_request import OperationApprovalRequest
from .privilege_management_elevation import PrivilegeManagementElevation
from .remote_action_audit import RemoteActionAudit
from .remote_assistance_partner import RemoteAssistancePartner
from .remote_assistance_settings import RemoteAssistanceSettings
from .device_management_reports import DeviceManagementReports
from .windows10_x_certificate_profile import Windows10XCertificateProfile
from .windows10_x_s_c_e_p_certificate_profile import Windows10XSCEPCertificateProfile
from .windows10_x_trusted_root_certificate import Windows10XTrustedRootCertificate
from .windows10_x_vpn_configuration import Windows10XVpnConfiguration
from .windows10_x_wifi_configuration import Windows10XWifiConfiguration
from .resource_operation import ResourceOperation
from .device_management_reusable_policy_setting import DeviceManagementReusablePolicySetting
from .device_management_configuration_choice_setting_definition import DeviceManagementConfigurationChoiceSettingDefinition
from .device_management_configuration_choice_setting_collection_definition import DeviceManagementConfigurationChoiceSettingCollectionDefinition
from .device_management_configuration_redirect_setting_definition import DeviceManagementConfigurationRedirectSettingDefinition
from .device_management_configuration_setting_group_definition import DeviceManagementConfigurationSettingGroupDefinition
from .device_management_configuration_setting_group_collection_definition import DeviceManagementConfigurationSettingGroupCollectionDefinition
from .device_management_configuration_simple_setting_definition import DeviceManagementConfigurationSimpleSettingDefinition
from .device_management_configuration_simple_setting_collection_definition import DeviceManagementConfigurationSimpleSettingCollectionDefinition
from .device_and_app_management_role_assignment import DeviceAndAppManagementRoleAssignment
from .device_and_app_management_role_definition import DeviceAndAppManagementRoleDefinition
from .role_scope_tag import RoleScopeTag
from .service_now_connection import ServiceNowConnection
from .device_management_abstract_complex_setting_definition import DeviceManagementAbstractComplexSettingDefinition
from .device_management_collection_setting_definition import DeviceManagementCollectionSettingDefinition
from .device_management_complex_setting_definition import DeviceManagementComplexSettingDefinition
from .software_update_status_summary import SoftwareUpdateStatusSummary
from .telecom_expense_management_partner import TelecomExpenseManagementPartner
from .device_management_template_insights_definition import DeviceManagementTemplateInsightsDefinition
from .security_baseline_template import SecurityBaselineTemplate
from .device_management_configuration_setting_template import DeviceManagementConfigurationSettingTemplate
from .tenant_attach_r_b_a_c import TenantAttachRBAC
from .terms_and_conditions import TermsAndConditions
from .apple_vpp_token_troubleshooting_event import AppleVppTokenTroubleshootingEvent
from .enrollment_troubleshooting_event import EnrollmentTroubleshootingEvent
from .mobile_app_troubleshooting_event import MobileAppTroubleshootingEvent
from .user_experience_analytics_anomaly import UserExperienceAnalyticsAnomaly
from .user_experience_analytics_anomaly_correlation_group_overview import UserExperienceAnalyticsAnomalyCorrelationGroupOverview
from .user_experience_analytics_anomaly_device import UserExperienceAnalyticsAnomalyDevice
from .user_experience_analytics_app_health_application_performance import UserExperienceAnalyticsAppHealthApplicationPerformance
from .user_experience_analytics_app_health_app_performance_by_app_version import UserExperienceAnalyticsAppHealthAppPerformanceByAppVersion
from .user_experience_analytics_app_health_app_performance_by_app_version_details import UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionDetails
from .user_experience_analytics_app_health_app_performance_by_app_version_device_id import UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionDeviceId
from .user_experience_analytics_app_health_app_performance_by_o_s_version import UserExperienceAnalyticsAppHealthAppPerformanceByOSVersion
from .user_experience_analytics_app_health_device_model_performance import UserExperienceAnalyticsAppHealthDeviceModelPerformance
from .user_experience_analytics_app_health_device_performance import UserExperienceAnalyticsAppHealthDevicePerformance
from .user_experience_analytics_app_health_device_performance_details import UserExperienceAnalyticsAppHealthDevicePerformanceDetails
from .user_experience_analytics_app_health_o_s_version_performance import UserExperienceAnalyticsAppHealthOSVersionPerformance
from .user_experience_analytics_category import UserExperienceAnalyticsCategory
from .user_experience_analytics_baseline import UserExperienceAnalyticsBaseline
from .user_experience_analytics_battery_health_app_impact import UserExperienceAnalyticsBatteryHealthAppImpact
from .user_experience_analytics_battery_health_capacity_details import UserExperienceAnalyticsBatteryHealthCapacityDetails
from .user_experience_analytics_battery_health_device_app_impact import UserExperienceAnalyticsBatteryHealthDeviceAppImpact
from .user_experience_analytics_battery_health_device_performance import UserExperienceAnalyticsBatteryHealthDevicePerformance
from .user_experience_analytics_battery_health_device_runtime_history import UserExperienceAnalyticsBatteryHealthDeviceRuntimeHistory
from .user_experience_analytics_battery_health_model_performance import UserExperienceAnalyticsBatteryHealthModelPerformance
from .user_experience_analytics_battery_health_os_performance import UserExperienceAnalyticsBatteryHealthOsPerformance
from .user_experience_analytics_battery_health_runtime_details import UserExperienceAnalyticsBatteryHealthRuntimeDetails
from .user_experience_analytics_category import UserExperienceAnalyticsCategory
from .user_experience_analytics_metric_history import UserExperienceAnalyticsMetricHistory
from .user_experience_analytics_device_performance import UserExperienceAnalyticsDevicePerformance
from .user_experience_analytics_device_scope import UserExperienceAnalyticsDeviceScope
from .user_experience_analytics_device_scope import UserExperienceAnalyticsDeviceScope
from .user_experience_analytics_device_scores import UserExperienceAnalyticsDeviceScores
from .user_experience_analytics_device_startup_history import UserExperienceAnalyticsDeviceStartupHistory
from .user_experience_analytics_device_startup_process import UserExperienceAnalyticsDeviceStartupProcess
from .user_experience_analytics_device_startup_process_performance import UserExperienceAnalyticsDeviceStartupProcessPerformance
from .user_experience_analytics_device_without_cloud_identity import UserExperienceAnalyticsDeviceWithoutCloudIdentity
from .user_experience_analytics_device_timeline_event import UserExperienceAnalyticsDeviceTimelineEvent
from .user_experience_analytics_impacting_process import UserExperienceAnalyticsImpactingProcess
from .user_experience_analytics_metric_history import UserExperienceAnalyticsMetricHistory
from .user_experience_analytics_model_scores import UserExperienceAnalyticsModelScores
from .user_experience_analytics_not_autopilot_ready_device import UserExperienceAnalyticsNotAutopilotReadyDevice
from .user_experience_analytics_overview import UserExperienceAnalyticsOverview
from .user_experience_analytics_remote_connection import UserExperienceAnalyticsRemoteConnection
from .user_experience_analytics_resource_performance import UserExperienceAnalyticsResourcePerformance
from .user_experience_analytics_score_history import UserExperienceAnalyticsScoreHistory
from .user_experience_analytics_work_from_anywhere_hardware_readiness_metric import UserExperienceAnalyticsWorkFromAnywhereHardwareReadinessMetric
from .user_experience_analytics_work_from_anywhere_metric import UserExperienceAnalyticsWorkFromAnywhereMetric
from .user_experience_analytics_work_from_anywhere_model_performance import UserExperienceAnalyticsWorkFromAnywhereModelPerformance
from .user_p_f_x_certificate import UserPFXCertificate
from .virtual_endpoint import VirtualEndpoint
from .active_directory_windows_autopilot_deployment_profile import ActiveDirectoryWindowsAutopilotDeploymentProfile
from .azure_a_d_windows_autopilot_deployment_profile import AzureADWindowsAutopilotDeploymentProfile
from .windows_autopilot_device_identity import WindowsAutopilotDeviceIdentity
from .windows_autopilot_settings import WindowsAutopilotSettings
from .windows_driver_update_profile import WindowsDriverUpdateProfile
from .windows_feature_update_profile import WindowsFeatureUpdateProfile
from .windows_information_protection_app_learning_summary import WindowsInformationProtectionAppLearningSummary
from .windows_information_protection_network_learning_summary import WindowsInformationProtectionNetworkLearningSummary
from .windows_malware_information import WindowsMalwareInformation
from .windows_quality_update_policy import WindowsQualityUpdatePolicy
from .windows_quality_update_profile import WindowsQualityUpdateProfile
from .windows_feature_update_catalog_item import WindowsFeatureUpdateCatalogItem
from .windows_quality_update_catalog_item import WindowsQualityUpdateCatalogItem
from .zebra_fota_artifact import ZebraFotaArtifact
from .zebra_fota_connector import ZebraFotaConnector
from .zebra_fota_deployment import ZebraFotaDeployment

