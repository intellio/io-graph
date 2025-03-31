from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class Windows10EndpointProtectionConfiguration(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.windows10EndpointProtectionConfiguration"] = Field(alias="@odata.type", default="#microsoft.graph.windows10EndpointProtectionConfiguration")
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	deviceManagementApplicabilityRuleDeviceMode: Optional[DeviceManagementApplicabilityRuleDeviceMode] = Field(alias="deviceManagementApplicabilityRuleDeviceMode", default=None,)
	deviceManagementApplicabilityRuleOsEdition: Optional[DeviceManagementApplicabilityRuleOsEdition] = Field(alias="deviceManagementApplicabilityRuleOsEdition", default=None,)
	deviceManagementApplicabilityRuleOsVersion: Optional[DeviceManagementApplicabilityRuleOsVersion] = Field(alias="deviceManagementApplicabilityRuleOsVersion", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	roleScopeTagIds: Optional[list[str]] = Field(alias="roleScopeTagIds", default=None,)
	supportsScopeTags: Optional[bool] = Field(alias="supportsScopeTags", default=None,)
	version: Optional[int] = Field(alias="version", default=None,)
	assignments: Optional[list[DeviceConfigurationAssignment]] = Field(alias="assignments", default=None,)
	deviceSettingStateSummaries: Optional[list[SettingStateDeviceSummary]] = Field(alias="deviceSettingStateSummaries", default=None,)
	deviceStatuses: Optional[list[DeviceConfigurationDeviceStatus]] = Field(alias="deviceStatuses", default=None,)
	deviceStatusOverview: Optional[DeviceConfigurationDeviceOverview] = Field(alias="deviceStatusOverview", default=None,)
	groupAssignments: Optional[list[DeviceConfigurationGroupAssignment]] = Field(alias="groupAssignments", default=None,)
	userStatuses: Optional[list[DeviceConfigurationUserStatus]] = Field(alias="userStatuses", default=None,)
	userStatusOverview: Optional[DeviceConfigurationUserOverview] = Field(alias="userStatusOverview", default=None,)
	applicationGuardAllowCameraMicrophoneRedirection: Optional[bool] = Field(alias="applicationGuardAllowCameraMicrophoneRedirection", default=None,)
	applicationGuardAllowFileSaveOnHost: Optional[bool] = Field(alias="applicationGuardAllowFileSaveOnHost", default=None,)
	applicationGuardAllowPersistence: Optional[bool] = Field(alias="applicationGuardAllowPersistence", default=None,)
	applicationGuardAllowPrintToLocalPrinters: Optional[bool] = Field(alias="applicationGuardAllowPrintToLocalPrinters", default=None,)
	applicationGuardAllowPrintToNetworkPrinters: Optional[bool] = Field(alias="applicationGuardAllowPrintToNetworkPrinters", default=None,)
	applicationGuardAllowPrintToPDF: Optional[bool] = Field(alias="applicationGuardAllowPrintToPDF", default=None,)
	applicationGuardAllowPrintToXPS: Optional[bool] = Field(alias="applicationGuardAllowPrintToXPS", default=None,)
	applicationGuardAllowVirtualGPU: Optional[bool] = Field(alias="applicationGuardAllowVirtualGPU", default=None,)
	applicationGuardBlockClipboardSharing: Optional[ApplicationGuardBlockClipboardSharingType | str] = Field(alias="applicationGuardBlockClipboardSharing", default=None,)
	applicationGuardBlockFileTransfer: Optional[ApplicationGuardBlockFileTransferType | str] = Field(alias="applicationGuardBlockFileTransfer", default=None,)
	applicationGuardBlockNonEnterpriseContent: Optional[bool] = Field(alias="applicationGuardBlockNonEnterpriseContent", default=None,)
	applicationGuardCertificateThumbprints: Optional[list[str]] = Field(alias="applicationGuardCertificateThumbprints", default=None,)
	applicationGuardEnabled: Optional[bool] = Field(alias="applicationGuardEnabled", default=None,)
	applicationGuardEnabledOptions: Optional[ApplicationGuardEnabledOptions | str] = Field(alias="applicationGuardEnabledOptions", default=None,)
	applicationGuardForceAuditing: Optional[bool] = Field(alias="applicationGuardForceAuditing", default=None,)
	appLockerApplicationControl: Optional[AppLockerApplicationControlType | str] = Field(alias="appLockerApplicationControl", default=None,)
	bitLockerAllowStandardUserEncryption: Optional[bool] = Field(alias="bitLockerAllowStandardUserEncryption", default=None,)
	bitLockerDisableWarningForOtherDiskEncryption: Optional[bool] = Field(alias="bitLockerDisableWarningForOtherDiskEncryption", default=None,)
	bitLockerEnableStorageCardEncryptionOnMobile: Optional[bool] = Field(alias="bitLockerEnableStorageCardEncryptionOnMobile", default=None,)
	bitLockerEncryptDevice: Optional[bool] = Field(alias="bitLockerEncryptDevice", default=None,)
	bitLockerFixedDrivePolicy: Optional[BitLockerFixedDrivePolicy] = Field(alias="bitLockerFixedDrivePolicy", default=None,)
	bitLockerRecoveryPasswordRotation: Optional[BitLockerRecoveryPasswordRotationType | str] = Field(alias="bitLockerRecoveryPasswordRotation", default=None,)
	bitLockerRemovableDrivePolicy: Optional[BitLockerRemovableDrivePolicy] = Field(alias="bitLockerRemovableDrivePolicy", default=None,)
	bitLockerSystemDrivePolicy: Optional[BitLockerSystemDrivePolicy] = Field(alias="bitLockerSystemDrivePolicy", default=None,)
	defenderAdditionalGuardedFolders: Optional[list[str]] = Field(alias="defenderAdditionalGuardedFolders", default=None,)
	defenderAdobeReaderLaunchChildProcess: Optional[DefenderProtectionType | str] = Field(alias="defenderAdobeReaderLaunchChildProcess", default=None,)
	defenderAdvancedRansomewareProtectionType: Optional[DefenderProtectionType | str] = Field(alias="defenderAdvancedRansomewareProtectionType", default=None,)
	defenderAllowBehaviorMonitoring: Optional[bool] = Field(alias="defenderAllowBehaviorMonitoring", default=None,)
	defenderAllowCloudProtection: Optional[bool] = Field(alias="defenderAllowCloudProtection", default=None,)
	defenderAllowEndUserAccess: Optional[bool] = Field(alias="defenderAllowEndUserAccess", default=None,)
	defenderAllowIntrusionPreventionSystem: Optional[bool] = Field(alias="defenderAllowIntrusionPreventionSystem", default=None,)
	defenderAllowOnAccessProtection: Optional[bool] = Field(alias="defenderAllowOnAccessProtection", default=None,)
	defenderAllowRealTimeMonitoring: Optional[bool] = Field(alias="defenderAllowRealTimeMonitoring", default=None,)
	defenderAllowScanArchiveFiles: Optional[bool] = Field(alias="defenderAllowScanArchiveFiles", default=None,)
	defenderAllowScanDownloads: Optional[bool] = Field(alias="defenderAllowScanDownloads", default=None,)
	defenderAllowScanNetworkFiles: Optional[bool] = Field(alias="defenderAllowScanNetworkFiles", default=None,)
	defenderAllowScanRemovableDrivesDuringFullScan: Optional[bool] = Field(alias="defenderAllowScanRemovableDrivesDuringFullScan", default=None,)
	defenderAllowScanScriptsLoadedInInternetExplorer: Optional[bool] = Field(alias="defenderAllowScanScriptsLoadedInInternetExplorer", default=None,)
	defenderAttackSurfaceReductionExcludedPaths: Optional[list[str]] = Field(alias="defenderAttackSurfaceReductionExcludedPaths", default=None,)
	defenderBlockEndUserAccess: Optional[bool] = Field(alias="defenderBlockEndUserAccess", default=None,)
	defenderBlockPersistenceThroughWmiType: Optional[DefenderAttackSurfaceType | str] = Field(alias="defenderBlockPersistenceThroughWmiType", default=None,)
	defenderCheckForSignaturesBeforeRunningScan: Optional[bool] = Field(alias="defenderCheckForSignaturesBeforeRunningScan", default=None,)
	defenderCloudBlockLevel: Optional[DefenderCloudBlockLevelType | str] = Field(alias="defenderCloudBlockLevel", default=None,)
	defenderCloudExtendedTimeoutInSeconds: Optional[int] = Field(alias="defenderCloudExtendedTimeoutInSeconds", default=None,)
	defenderDaysBeforeDeletingQuarantinedMalware: Optional[int] = Field(alias="defenderDaysBeforeDeletingQuarantinedMalware", default=None,)
	defenderDetectedMalwareActions: Optional[DefenderDetectedMalwareActions] = Field(alias="defenderDetectedMalwareActions", default=None,)
	defenderDisableBehaviorMonitoring: Optional[bool] = Field(alias="defenderDisableBehaviorMonitoring", default=None,)
	defenderDisableCatchupFullScan: Optional[bool] = Field(alias="defenderDisableCatchupFullScan", default=None,)
	defenderDisableCatchupQuickScan: Optional[bool] = Field(alias="defenderDisableCatchupQuickScan", default=None,)
	defenderDisableCloudProtection: Optional[bool] = Field(alias="defenderDisableCloudProtection", default=None,)
	defenderDisableIntrusionPreventionSystem: Optional[bool] = Field(alias="defenderDisableIntrusionPreventionSystem", default=None,)
	defenderDisableOnAccessProtection: Optional[bool] = Field(alias="defenderDisableOnAccessProtection", default=None,)
	defenderDisableRealTimeMonitoring: Optional[bool] = Field(alias="defenderDisableRealTimeMonitoring", default=None,)
	defenderDisableScanArchiveFiles: Optional[bool] = Field(alias="defenderDisableScanArchiveFiles", default=None,)
	defenderDisableScanDownloads: Optional[bool] = Field(alias="defenderDisableScanDownloads", default=None,)
	defenderDisableScanNetworkFiles: Optional[bool] = Field(alias="defenderDisableScanNetworkFiles", default=None,)
	defenderDisableScanRemovableDrivesDuringFullScan: Optional[bool] = Field(alias="defenderDisableScanRemovableDrivesDuringFullScan", default=None,)
	defenderDisableScanScriptsLoadedInInternetExplorer: Optional[bool] = Field(alias="defenderDisableScanScriptsLoadedInInternetExplorer", default=None,)
	defenderEmailContentExecution: Optional[DefenderProtectionType | str] = Field(alias="defenderEmailContentExecution", default=None,)
	defenderEmailContentExecutionType: Optional[DefenderAttackSurfaceType | str] = Field(alias="defenderEmailContentExecutionType", default=None,)
	defenderEnableLowCpuPriority: Optional[bool] = Field(alias="defenderEnableLowCpuPriority", default=None,)
	defenderEnableScanIncomingMail: Optional[bool] = Field(alias="defenderEnableScanIncomingMail", default=None,)
	defenderEnableScanMappedNetworkDrivesDuringFullScan: Optional[bool] = Field(alias="defenderEnableScanMappedNetworkDrivesDuringFullScan", default=None,)
	defenderExploitProtectionXml: Optional[str] = Field(alias="defenderExploitProtectionXml", default=None,)
	defenderExploitProtectionXmlFileName: Optional[str] = Field(alias="defenderExploitProtectionXmlFileName", default=None,)
	defenderFileExtensionsToExclude: Optional[list[str]] = Field(alias="defenderFileExtensionsToExclude", default=None,)
	defenderFilesAndFoldersToExclude: Optional[list[str]] = Field(alias="defenderFilesAndFoldersToExclude", default=None,)
	defenderGuardedFoldersAllowedAppPaths: Optional[list[str]] = Field(alias="defenderGuardedFoldersAllowedAppPaths", default=None,)
	defenderGuardMyFoldersType: Optional[FolderProtectionType | str] = Field(alias="defenderGuardMyFoldersType", default=None,)
	defenderNetworkProtectionType: Optional[DefenderProtectionType | str] = Field(alias="defenderNetworkProtectionType", default=None,)
	defenderOfficeAppsExecutableContentCreationOrLaunch: Optional[DefenderProtectionType | str] = Field(alias="defenderOfficeAppsExecutableContentCreationOrLaunch", default=None,)
	defenderOfficeAppsExecutableContentCreationOrLaunchType: Optional[DefenderAttackSurfaceType | str] = Field(alias="defenderOfficeAppsExecutableContentCreationOrLaunchType", default=None,)
	defenderOfficeAppsLaunchChildProcess: Optional[DefenderProtectionType | str] = Field(alias="defenderOfficeAppsLaunchChildProcess", default=None,)
	defenderOfficeAppsLaunchChildProcessType: Optional[DefenderAttackSurfaceType | str] = Field(alias="defenderOfficeAppsLaunchChildProcessType", default=None,)
	defenderOfficeAppsOtherProcessInjection: Optional[DefenderProtectionType | str] = Field(alias="defenderOfficeAppsOtherProcessInjection", default=None,)
	defenderOfficeAppsOtherProcessInjectionType: Optional[DefenderAttackSurfaceType | str] = Field(alias="defenderOfficeAppsOtherProcessInjectionType", default=None,)
	defenderOfficeCommunicationAppsLaunchChildProcess: Optional[DefenderProtectionType | str] = Field(alias="defenderOfficeCommunicationAppsLaunchChildProcess", default=None,)
	defenderOfficeMacroCodeAllowWin32Imports: Optional[DefenderProtectionType | str] = Field(alias="defenderOfficeMacroCodeAllowWin32Imports", default=None,)
	defenderOfficeMacroCodeAllowWin32ImportsType: Optional[DefenderAttackSurfaceType | str] = Field(alias="defenderOfficeMacroCodeAllowWin32ImportsType", default=None,)
	defenderPotentiallyUnwantedAppAction: Optional[DefenderProtectionType | str] = Field(alias="defenderPotentiallyUnwantedAppAction", default=None,)
	defenderPreventCredentialStealingType: Optional[DefenderProtectionType | str] = Field(alias="defenderPreventCredentialStealingType", default=None,)
	defenderProcessCreation: Optional[DefenderProtectionType | str] = Field(alias="defenderProcessCreation", default=None,)
	defenderProcessCreationType: Optional[DefenderAttackSurfaceType | str] = Field(alias="defenderProcessCreationType", default=None,)
	defenderProcessesToExclude: Optional[list[str]] = Field(alias="defenderProcessesToExclude", default=None,)
	defenderScanDirection: Optional[DefenderRealtimeScanDirection | str] = Field(alias="defenderScanDirection", default=None,)
	defenderScanMaxCpuPercentage: Optional[int] = Field(alias="defenderScanMaxCpuPercentage", default=None,)
	defenderScanType: Optional[DefenderScanType | str] = Field(alias="defenderScanType", default=None,)
	defenderScheduledQuickScanTime: Optional[str] = Field(alias="defenderScheduledQuickScanTime", default=None,)
	defenderScheduledScanDay: Optional[WeeklySchedule | str] = Field(alias="defenderScheduledScanDay", default=None,)
	defenderScheduledScanTime: Optional[str] = Field(alias="defenderScheduledScanTime", default=None,)
	defenderScriptDownloadedPayloadExecution: Optional[DefenderProtectionType | str] = Field(alias="defenderScriptDownloadedPayloadExecution", default=None,)
	defenderScriptDownloadedPayloadExecutionType: Optional[DefenderAttackSurfaceType | str] = Field(alias="defenderScriptDownloadedPayloadExecutionType", default=None,)
	defenderScriptObfuscatedMacroCode: Optional[DefenderProtectionType | str] = Field(alias="defenderScriptObfuscatedMacroCode", default=None,)
	defenderScriptObfuscatedMacroCodeType: Optional[DefenderAttackSurfaceType | str] = Field(alias="defenderScriptObfuscatedMacroCodeType", default=None,)
	defenderSecurityCenterBlockExploitProtectionOverride: Optional[bool] = Field(alias="defenderSecurityCenterBlockExploitProtectionOverride", default=None,)
	defenderSecurityCenterDisableAccountUI: Optional[bool] = Field(alias="defenderSecurityCenterDisableAccountUI", default=None,)
	defenderSecurityCenterDisableAppBrowserUI: Optional[bool] = Field(alias="defenderSecurityCenterDisableAppBrowserUI", default=None,)
	defenderSecurityCenterDisableClearTpmUI: Optional[bool] = Field(alias="defenderSecurityCenterDisableClearTpmUI", default=None,)
	defenderSecurityCenterDisableFamilyUI: Optional[bool] = Field(alias="defenderSecurityCenterDisableFamilyUI", default=None,)
	defenderSecurityCenterDisableHardwareUI: Optional[bool] = Field(alias="defenderSecurityCenterDisableHardwareUI", default=None,)
	defenderSecurityCenterDisableHealthUI: Optional[bool] = Field(alias="defenderSecurityCenterDisableHealthUI", default=None,)
	defenderSecurityCenterDisableNetworkUI: Optional[bool] = Field(alias="defenderSecurityCenterDisableNetworkUI", default=None,)
	defenderSecurityCenterDisableNotificationAreaUI: Optional[bool] = Field(alias="defenderSecurityCenterDisableNotificationAreaUI", default=None,)
	defenderSecurityCenterDisableRansomwareUI: Optional[bool] = Field(alias="defenderSecurityCenterDisableRansomwareUI", default=None,)
	defenderSecurityCenterDisableSecureBootUI: Optional[bool] = Field(alias="defenderSecurityCenterDisableSecureBootUI", default=None,)
	defenderSecurityCenterDisableTroubleshootingUI: Optional[bool] = Field(alias="defenderSecurityCenterDisableTroubleshootingUI", default=None,)
	defenderSecurityCenterDisableVirusUI: Optional[bool] = Field(alias="defenderSecurityCenterDisableVirusUI", default=None,)
	defenderSecurityCenterDisableVulnerableTpmFirmwareUpdateUI: Optional[bool] = Field(alias="defenderSecurityCenterDisableVulnerableTpmFirmwareUpdateUI", default=None,)
	defenderSecurityCenterHelpEmail: Optional[str] = Field(alias="defenderSecurityCenterHelpEmail", default=None,)
	defenderSecurityCenterHelpPhone: Optional[str] = Field(alias="defenderSecurityCenterHelpPhone", default=None,)
	defenderSecurityCenterHelpURL: Optional[str] = Field(alias="defenderSecurityCenterHelpURL", default=None,)
	defenderSecurityCenterITContactDisplay: Optional[DefenderSecurityCenterITContactDisplayType | str] = Field(alias="defenderSecurityCenterITContactDisplay", default=None,)
	defenderSecurityCenterNotificationsFromApp: Optional[DefenderSecurityCenterNotificationsFromAppType | str] = Field(alias="defenderSecurityCenterNotificationsFromApp", default=None,)
	defenderSecurityCenterOrganizationDisplayName: Optional[str] = Field(alias="defenderSecurityCenterOrganizationDisplayName", default=None,)
	defenderSignatureUpdateIntervalInHours: Optional[int] = Field(alias="defenderSignatureUpdateIntervalInHours", default=None,)
	defenderSubmitSamplesConsentType: Optional[DefenderSubmitSamplesConsentType | str] = Field(alias="defenderSubmitSamplesConsentType", default=None,)
	defenderUntrustedExecutable: Optional[DefenderProtectionType | str] = Field(alias="defenderUntrustedExecutable", default=None,)
	defenderUntrustedExecutableType: Optional[DefenderAttackSurfaceType | str] = Field(alias="defenderUntrustedExecutableType", default=None,)
	defenderUntrustedUSBProcess: Optional[DefenderProtectionType | str] = Field(alias="defenderUntrustedUSBProcess", default=None,)
	defenderUntrustedUSBProcessType: Optional[DefenderAttackSurfaceType | str] = Field(alias="defenderUntrustedUSBProcessType", default=None,)
	deviceGuardEnableSecureBootWithDMA: Optional[bool] = Field(alias="deviceGuardEnableSecureBootWithDMA", default=None,)
	deviceGuardEnableVirtualizationBasedSecurity: Optional[bool] = Field(alias="deviceGuardEnableVirtualizationBasedSecurity", default=None,)
	deviceGuardLaunchSystemGuard: Optional[Enablement | str] = Field(alias="deviceGuardLaunchSystemGuard", default=None,)
	deviceGuardLocalSystemAuthorityCredentialGuardSettings: Optional[DeviceGuardLocalSystemAuthorityCredentialGuardType | str] = Field(alias="deviceGuardLocalSystemAuthorityCredentialGuardSettings", default=None,)
	deviceGuardSecureBootWithDMA: Optional[SecureBootWithDMAType | str] = Field(alias="deviceGuardSecureBootWithDMA", default=None,)
	dmaGuardDeviceEnumerationPolicy: Optional[DmaGuardDeviceEnumerationPolicyType | str] = Field(alias="dmaGuardDeviceEnumerationPolicy", default=None,)
	firewallBlockStatefulFTP: Optional[bool] = Field(alias="firewallBlockStatefulFTP", default=None,)
	firewallCertificateRevocationListCheckMethod: Optional[FirewallCertificateRevocationListCheckMethodType | str] = Field(alias="firewallCertificateRevocationListCheckMethod", default=None,)
	firewallIdleTimeoutForSecurityAssociationInSeconds: Optional[int] = Field(alias="firewallIdleTimeoutForSecurityAssociationInSeconds", default=None,)
	firewallIPSecExemptionsAllowDHCP: Optional[bool] = Field(alias="firewallIPSecExemptionsAllowDHCP", default=None,)
	firewallIPSecExemptionsAllowICMP: Optional[bool] = Field(alias="firewallIPSecExemptionsAllowICMP", default=None,)
	firewallIPSecExemptionsAllowNeighborDiscovery: Optional[bool] = Field(alias="firewallIPSecExemptionsAllowNeighborDiscovery", default=None,)
	firewallIPSecExemptionsAllowRouterDiscovery: Optional[bool] = Field(alias="firewallIPSecExemptionsAllowRouterDiscovery", default=None,)
	firewallIPSecExemptionsNone: Optional[bool] = Field(alias="firewallIPSecExemptionsNone", default=None,)
	firewallMergeKeyingModuleSettings: Optional[bool] = Field(alias="firewallMergeKeyingModuleSettings", default=None,)
	firewallPacketQueueingMethod: Optional[FirewallPacketQueueingMethodType | str] = Field(alias="firewallPacketQueueingMethod", default=None,)
	firewallPreSharedKeyEncodingMethod: Optional[FirewallPreSharedKeyEncodingMethodType | str] = Field(alias="firewallPreSharedKeyEncodingMethod", default=None,)
	firewallProfileDomain: Optional[WindowsFirewallNetworkProfile] = Field(alias="firewallProfileDomain", default=None,)
	firewallProfilePrivate: Optional[WindowsFirewallNetworkProfile] = Field(alias="firewallProfilePrivate", default=None,)
	firewallProfilePublic: Optional[WindowsFirewallNetworkProfile] = Field(alias="firewallProfilePublic", default=None,)
	firewallRules: Optional[list[WindowsFirewallRule]] = Field(alias="firewallRules", default=None,)
	lanManagerAuthenticationLevel: Optional[LanManagerAuthenticationLevel | str] = Field(alias="lanManagerAuthenticationLevel", default=None,)
	lanManagerWorkstationDisableInsecureGuestLogons: Optional[bool] = Field(alias="lanManagerWorkstationDisableInsecureGuestLogons", default=None,)
	localSecurityOptionsAdministratorAccountName: Optional[str] = Field(alias="localSecurityOptionsAdministratorAccountName", default=None,)
	localSecurityOptionsAdministratorElevationPromptBehavior: Optional[LocalSecurityOptionsAdministratorElevationPromptBehaviorType | str] = Field(alias="localSecurityOptionsAdministratorElevationPromptBehavior", default=None,)
	localSecurityOptionsAllowAnonymousEnumerationOfSAMAccountsAndShares: Optional[bool] = Field(alias="localSecurityOptionsAllowAnonymousEnumerationOfSAMAccountsAndShares", default=None,)
	localSecurityOptionsAllowPKU2UAuthenticationRequests: Optional[bool] = Field(alias="localSecurityOptionsAllowPKU2UAuthenticationRequests", default=None,)
	localSecurityOptionsAllowRemoteCallsToSecurityAccountsManager: Optional[str] = Field(alias="localSecurityOptionsAllowRemoteCallsToSecurityAccountsManager", default=None,)
	localSecurityOptionsAllowRemoteCallsToSecurityAccountsManagerHelperBool: Optional[bool] = Field(alias="localSecurityOptionsAllowRemoteCallsToSecurityAccountsManagerHelperBool", default=None,)
	localSecurityOptionsAllowSystemToBeShutDownWithoutHavingToLogOn: Optional[bool] = Field(alias="localSecurityOptionsAllowSystemToBeShutDownWithoutHavingToLogOn", default=None,)
	localSecurityOptionsAllowUIAccessApplicationElevation: Optional[bool] = Field(alias="localSecurityOptionsAllowUIAccessApplicationElevation", default=None,)
	localSecurityOptionsAllowUIAccessApplicationsForSecureLocations: Optional[bool] = Field(alias="localSecurityOptionsAllowUIAccessApplicationsForSecureLocations", default=None,)
	localSecurityOptionsAllowUndockWithoutHavingToLogon: Optional[bool] = Field(alias="localSecurityOptionsAllowUndockWithoutHavingToLogon", default=None,)
	localSecurityOptionsBlockMicrosoftAccounts: Optional[bool] = Field(alias="localSecurityOptionsBlockMicrosoftAccounts", default=None,)
	localSecurityOptionsBlockRemoteLogonWithBlankPassword: Optional[bool] = Field(alias="localSecurityOptionsBlockRemoteLogonWithBlankPassword", default=None,)
	localSecurityOptionsBlockRemoteOpticalDriveAccess: Optional[bool] = Field(alias="localSecurityOptionsBlockRemoteOpticalDriveAccess", default=None,)
	localSecurityOptionsBlockUsersInstallingPrinterDrivers: Optional[bool] = Field(alias="localSecurityOptionsBlockUsersInstallingPrinterDrivers", default=None,)
	localSecurityOptionsClearVirtualMemoryPageFile: Optional[bool] = Field(alias="localSecurityOptionsClearVirtualMemoryPageFile", default=None,)
	localSecurityOptionsClientDigitallySignCommunicationsAlways: Optional[bool] = Field(alias="localSecurityOptionsClientDigitallySignCommunicationsAlways", default=None,)
	localSecurityOptionsClientSendUnencryptedPasswordToThirdPartySMBServers: Optional[bool] = Field(alias="localSecurityOptionsClientSendUnencryptedPasswordToThirdPartySMBServers", default=None,)
	localSecurityOptionsDetectApplicationInstallationsAndPromptForElevation: Optional[bool] = Field(alias="localSecurityOptionsDetectApplicationInstallationsAndPromptForElevation", default=None,)
	localSecurityOptionsDisableAdministratorAccount: Optional[bool] = Field(alias="localSecurityOptionsDisableAdministratorAccount", default=None,)
	localSecurityOptionsDisableClientDigitallySignCommunicationsIfServerAgrees: Optional[bool] = Field(alias="localSecurityOptionsDisableClientDigitallySignCommunicationsIfServerAgrees", default=None,)
	localSecurityOptionsDisableGuestAccount: Optional[bool] = Field(alias="localSecurityOptionsDisableGuestAccount", default=None,)
	localSecurityOptionsDisableServerDigitallySignCommunicationsAlways: Optional[bool] = Field(alias="localSecurityOptionsDisableServerDigitallySignCommunicationsAlways", default=None,)
	localSecurityOptionsDisableServerDigitallySignCommunicationsIfClientAgrees: Optional[bool] = Field(alias="localSecurityOptionsDisableServerDigitallySignCommunicationsIfClientAgrees", default=None,)
	localSecurityOptionsDoNotAllowAnonymousEnumerationOfSAMAccounts: Optional[bool] = Field(alias="localSecurityOptionsDoNotAllowAnonymousEnumerationOfSAMAccounts", default=None,)
	localSecurityOptionsDoNotRequireCtrlAltDel: Optional[bool] = Field(alias="localSecurityOptionsDoNotRequireCtrlAltDel", default=None,)
	localSecurityOptionsDoNotStoreLANManagerHashValueOnNextPasswordChange: Optional[bool] = Field(alias="localSecurityOptionsDoNotStoreLANManagerHashValueOnNextPasswordChange", default=None,)
	localSecurityOptionsFormatAndEjectOfRemovableMediaAllowedUser: Optional[LocalSecurityOptionsFormatAndEjectOfRemovableMediaAllowedUserType | str] = Field(alias="localSecurityOptionsFormatAndEjectOfRemovableMediaAllowedUser", default=None,)
	localSecurityOptionsGuestAccountName: Optional[str] = Field(alias="localSecurityOptionsGuestAccountName", default=None,)
	localSecurityOptionsHideLastSignedInUser: Optional[bool] = Field(alias="localSecurityOptionsHideLastSignedInUser", default=None,)
	localSecurityOptionsHideUsernameAtSignIn: Optional[bool] = Field(alias="localSecurityOptionsHideUsernameAtSignIn", default=None,)
	localSecurityOptionsInformationDisplayedOnLockScreen: Optional[LocalSecurityOptionsInformationDisplayedOnLockScreenType | str] = Field(alias="localSecurityOptionsInformationDisplayedOnLockScreen", default=None,)
	localSecurityOptionsInformationShownOnLockScreen: Optional[LocalSecurityOptionsInformationShownOnLockScreenType | str] = Field(alias="localSecurityOptionsInformationShownOnLockScreen", default=None,)
	localSecurityOptionsLogOnMessageText: Optional[str] = Field(alias="localSecurityOptionsLogOnMessageText", default=None,)
	localSecurityOptionsLogOnMessageTitle: Optional[str] = Field(alias="localSecurityOptionsLogOnMessageTitle", default=None,)
	localSecurityOptionsMachineInactivityLimit: Optional[int] = Field(alias="localSecurityOptionsMachineInactivityLimit", default=None,)
	localSecurityOptionsMachineInactivityLimitInMinutes: Optional[int] = Field(alias="localSecurityOptionsMachineInactivityLimitInMinutes", default=None,)
	localSecurityOptionsMinimumSessionSecurityForNtlmSspBasedClients: Optional[LocalSecurityOptionsMinimumSessionSecurity | str] = Field(alias="localSecurityOptionsMinimumSessionSecurityForNtlmSspBasedClients", default=None,)
	localSecurityOptionsMinimumSessionSecurityForNtlmSspBasedServers: Optional[LocalSecurityOptionsMinimumSessionSecurity | str] = Field(alias="localSecurityOptionsMinimumSessionSecurityForNtlmSspBasedServers", default=None,)
	localSecurityOptionsOnlyElevateSignedExecutables: Optional[bool] = Field(alias="localSecurityOptionsOnlyElevateSignedExecutables", default=None,)
	localSecurityOptionsRestrictAnonymousAccessToNamedPipesAndShares: Optional[bool] = Field(alias="localSecurityOptionsRestrictAnonymousAccessToNamedPipesAndShares", default=None,)
	localSecurityOptionsSmartCardRemovalBehavior: Optional[LocalSecurityOptionsSmartCardRemovalBehaviorType | str] = Field(alias="localSecurityOptionsSmartCardRemovalBehavior", default=None,)
	localSecurityOptionsStandardUserElevationPromptBehavior: Optional[LocalSecurityOptionsStandardUserElevationPromptBehaviorType | str] = Field(alias="localSecurityOptionsStandardUserElevationPromptBehavior", default=None,)
	localSecurityOptionsSwitchToSecureDesktopWhenPromptingForElevation: Optional[bool] = Field(alias="localSecurityOptionsSwitchToSecureDesktopWhenPromptingForElevation", default=None,)
	localSecurityOptionsUseAdminApprovalMode: Optional[bool] = Field(alias="localSecurityOptionsUseAdminApprovalMode", default=None,)
	localSecurityOptionsUseAdminApprovalModeForAdministrators: Optional[bool] = Field(alias="localSecurityOptionsUseAdminApprovalModeForAdministrators", default=None,)
	localSecurityOptionsVirtualizeFileAndRegistryWriteFailuresToPerUserLocations: Optional[bool] = Field(alias="localSecurityOptionsVirtualizeFileAndRegistryWriteFailuresToPerUserLocations", default=None,)
	smartScreenBlockOverrideForFiles: Optional[bool] = Field(alias="smartScreenBlockOverrideForFiles", default=None,)
	smartScreenEnableInShell: Optional[bool] = Field(alias="smartScreenEnableInShell", default=None,)
	userRightsAccessCredentialManagerAsTrustedCaller: Optional[DeviceManagementUserRightsSetting] = Field(alias="userRightsAccessCredentialManagerAsTrustedCaller", default=None,)
	userRightsActAsPartOfTheOperatingSystem: Optional[DeviceManagementUserRightsSetting] = Field(alias="userRightsActAsPartOfTheOperatingSystem", default=None,)
	userRightsAllowAccessFromNetwork: Optional[DeviceManagementUserRightsSetting] = Field(alias="userRightsAllowAccessFromNetwork", default=None,)
	userRightsBackupData: Optional[DeviceManagementUserRightsSetting] = Field(alias="userRightsBackupData", default=None,)
	userRightsBlockAccessFromNetwork: Optional[DeviceManagementUserRightsSetting] = Field(alias="userRightsBlockAccessFromNetwork", default=None,)
	userRightsChangeSystemTime: Optional[DeviceManagementUserRightsSetting] = Field(alias="userRightsChangeSystemTime", default=None,)
	userRightsCreateGlobalObjects: Optional[DeviceManagementUserRightsSetting] = Field(alias="userRightsCreateGlobalObjects", default=None,)
	userRightsCreatePageFile: Optional[DeviceManagementUserRightsSetting] = Field(alias="userRightsCreatePageFile", default=None,)
	userRightsCreatePermanentSharedObjects: Optional[DeviceManagementUserRightsSetting] = Field(alias="userRightsCreatePermanentSharedObjects", default=None,)
	userRightsCreateSymbolicLinks: Optional[DeviceManagementUserRightsSetting] = Field(alias="userRightsCreateSymbolicLinks", default=None,)
	userRightsCreateToken: Optional[DeviceManagementUserRightsSetting] = Field(alias="userRightsCreateToken", default=None,)
	userRightsDebugPrograms: Optional[DeviceManagementUserRightsSetting] = Field(alias="userRightsDebugPrograms", default=None,)
	userRightsDelegation: Optional[DeviceManagementUserRightsSetting] = Field(alias="userRightsDelegation", default=None,)
	userRightsDenyLocalLogOn: Optional[DeviceManagementUserRightsSetting] = Field(alias="userRightsDenyLocalLogOn", default=None,)
	userRightsGenerateSecurityAudits: Optional[DeviceManagementUserRightsSetting] = Field(alias="userRightsGenerateSecurityAudits", default=None,)
	userRightsImpersonateClient: Optional[DeviceManagementUserRightsSetting] = Field(alias="userRightsImpersonateClient", default=None,)
	userRightsIncreaseSchedulingPriority: Optional[DeviceManagementUserRightsSetting] = Field(alias="userRightsIncreaseSchedulingPriority", default=None,)
	userRightsLoadUnloadDrivers: Optional[DeviceManagementUserRightsSetting] = Field(alias="userRightsLoadUnloadDrivers", default=None,)
	userRightsLocalLogOn: Optional[DeviceManagementUserRightsSetting] = Field(alias="userRightsLocalLogOn", default=None,)
	userRightsLockMemory: Optional[DeviceManagementUserRightsSetting] = Field(alias="userRightsLockMemory", default=None,)
	userRightsManageAuditingAndSecurityLogs: Optional[DeviceManagementUserRightsSetting] = Field(alias="userRightsManageAuditingAndSecurityLogs", default=None,)
	userRightsManageVolumes: Optional[DeviceManagementUserRightsSetting] = Field(alias="userRightsManageVolumes", default=None,)
	userRightsModifyFirmwareEnvironment: Optional[DeviceManagementUserRightsSetting] = Field(alias="userRightsModifyFirmwareEnvironment", default=None,)
	userRightsModifyObjectLabels: Optional[DeviceManagementUserRightsSetting] = Field(alias="userRightsModifyObjectLabels", default=None,)
	userRightsProfileSingleProcess: Optional[DeviceManagementUserRightsSetting] = Field(alias="userRightsProfileSingleProcess", default=None,)
	userRightsRemoteDesktopServicesLogOn: Optional[DeviceManagementUserRightsSetting] = Field(alias="userRightsRemoteDesktopServicesLogOn", default=None,)
	userRightsRemoteShutdown: Optional[DeviceManagementUserRightsSetting] = Field(alias="userRightsRemoteShutdown", default=None,)
	userRightsRestoreData: Optional[DeviceManagementUserRightsSetting] = Field(alias="userRightsRestoreData", default=None,)
	userRightsTakeOwnership: Optional[DeviceManagementUserRightsSetting] = Field(alias="userRightsTakeOwnership", default=None,)
	windowsDefenderTamperProtection: Optional[WindowsDefenderTamperProtectionOptions | str] = Field(alias="windowsDefenderTamperProtection", default=None,)
	xboxServicesAccessoryManagementServiceStartupMode: Optional[ServiceStartType | str] = Field(alias="xboxServicesAccessoryManagementServiceStartupMode", default=None,)
	xboxServicesEnableXboxGameSaveTask: Optional[bool] = Field(alias="xboxServicesEnableXboxGameSaveTask", default=None,)
	xboxServicesLiveAuthManagerServiceStartupMode: Optional[ServiceStartType | str] = Field(alias="xboxServicesLiveAuthManagerServiceStartupMode", default=None,)
	xboxServicesLiveGameSaveServiceStartupMode: Optional[ServiceStartType | str] = Field(alias="xboxServicesLiveGameSaveServiceStartupMode", default=None,)
	xboxServicesLiveNetworkingServiceStartupMode: Optional[ServiceStartType | str] = Field(alias="xboxServicesLiveNetworkingServiceStartupMode", default=None,)

from .device_management_applicability_rule_device_mode import DeviceManagementApplicabilityRuleDeviceMode
from .device_management_applicability_rule_os_edition import DeviceManagementApplicabilityRuleOsEdition
from .device_management_applicability_rule_os_version import DeviceManagementApplicabilityRuleOsVersion
from .device_configuration_assignment import DeviceConfigurationAssignment
from .setting_state_device_summary import SettingStateDeviceSummary
from .device_configuration_device_status import DeviceConfigurationDeviceStatus
from .device_configuration_device_overview import DeviceConfigurationDeviceOverview
from .device_configuration_group_assignment import DeviceConfigurationGroupAssignment
from .device_configuration_user_status import DeviceConfigurationUserStatus
from .device_configuration_user_overview import DeviceConfigurationUserOverview
from .application_guard_block_clipboard_sharing_type import ApplicationGuardBlockClipboardSharingType
from .application_guard_block_file_transfer_type import ApplicationGuardBlockFileTransferType
from .application_guard_enabled_options import ApplicationGuardEnabledOptions
from .app_locker_application_control_type import AppLockerApplicationControlType
from .bit_locker_fixed_drive_policy import BitLockerFixedDrivePolicy
from .bit_locker_recovery_password_rotation_type import BitLockerRecoveryPasswordRotationType
from .bit_locker_removable_drive_policy import BitLockerRemovableDrivePolicy
from .bit_locker_system_drive_policy import BitLockerSystemDrivePolicy
from .defender_protection_type import DefenderProtectionType
from .defender_attack_surface_type import DefenderAttackSurfaceType
from .defender_cloud_block_level_type import DefenderCloudBlockLevelType
from .defender_detected_malware_actions import DefenderDetectedMalwareActions
from .folder_protection_type import FolderProtectionType
from .defender_realtime_scan_direction import DefenderRealtimeScanDirection
from .defender_scan_type import DefenderScanType
from .weekly_schedule import WeeklySchedule
from .defender_security_center_i_t_contact_display_type import DefenderSecurityCenterITContactDisplayType
from .defender_security_center_notifications_from_app_type import DefenderSecurityCenterNotificationsFromAppType
from .defender_submit_samples_consent_type import DefenderSubmitSamplesConsentType
from .enablement import Enablement
from .device_guard_local_system_authority_credential_guard_type import DeviceGuardLocalSystemAuthorityCredentialGuardType
from .secure_boot_with_d_m_a_type import SecureBootWithDMAType
from .dma_guard_device_enumeration_policy_type import DmaGuardDeviceEnumerationPolicyType
from .firewall_certificate_revocation_list_check_method_type import FirewallCertificateRevocationListCheckMethodType
from .firewall_packet_queueing_method_type import FirewallPacketQueueingMethodType
from .firewall_pre_shared_key_encoding_method_type import FirewallPreSharedKeyEncodingMethodType
from .windows_firewall_network_profile import WindowsFirewallNetworkProfile
from .windows_firewall_rule import WindowsFirewallRule
from .lan_manager_authentication_level import LanManagerAuthenticationLevel
from .local_security_options_administrator_elevation_prompt_behavior_type import LocalSecurityOptionsAdministratorElevationPromptBehaviorType
from .local_security_options_format_and_eject_of_removable_media_allowed_user_type import LocalSecurityOptionsFormatAndEjectOfRemovableMediaAllowedUserType
from .local_security_options_information_displayed_on_lock_screen_type import LocalSecurityOptionsInformationDisplayedOnLockScreenType
from .local_security_options_information_shown_on_lock_screen_type import LocalSecurityOptionsInformationShownOnLockScreenType
from .local_security_options_minimum_session_security import LocalSecurityOptionsMinimumSessionSecurity
from .local_security_options_smart_card_removal_behavior_type import LocalSecurityOptionsSmartCardRemovalBehaviorType
from .local_security_options_standard_user_elevation_prompt_behavior_type import LocalSecurityOptionsStandardUserElevationPromptBehaviorType
from .device_management_user_rights_setting import DeviceManagementUserRightsSetting
from .windows_defender_tamper_protection_options import WindowsDefenderTamperProtectionOptions
from .service_start_type import ServiceStartType
