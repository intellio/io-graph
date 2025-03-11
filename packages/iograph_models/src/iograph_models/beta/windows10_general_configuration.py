from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class Windows10GeneralConfiguration(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	deviceManagementApplicabilityRuleDeviceMode: Optional[DeviceManagementApplicabilityRuleDeviceMode] = Field(alias="deviceManagementApplicabilityRuleDeviceMode",default=None,)
	deviceManagementApplicabilityRuleOsEdition: Optional[DeviceManagementApplicabilityRuleOsEdition] = Field(alias="deviceManagementApplicabilityRuleOsEdition",default=None,)
	deviceManagementApplicabilityRuleOsVersion: Optional[DeviceManagementApplicabilityRuleOsVersion] = Field(alias="deviceManagementApplicabilityRuleOsVersion",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	roleScopeTagIds: Optional[list[str]] = Field(alias="roleScopeTagIds",default=None,)
	supportsScopeTags: Optional[bool] = Field(alias="supportsScopeTags",default=None,)
	version: Optional[int] = Field(alias="version",default=None,)
	assignments: Optional[list[DeviceConfigurationAssignment]] = Field(alias="assignments",default=None,)
	deviceSettingStateSummaries: Optional[list[SettingStateDeviceSummary]] = Field(alias="deviceSettingStateSummaries",default=None,)
	deviceStatuses: Optional[list[DeviceConfigurationDeviceStatus]] = Field(alias="deviceStatuses",default=None,)
	deviceStatusOverview: Optional[DeviceConfigurationDeviceOverview] = Field(alias="deviceStatusOverview",default=None,)
	groupAssignments: Optional[list[DeviceConfigurationGroupAssignment]] = Field(alias="groupAssignments",default=None,)
	userStatuses: Optional[list[DeviceConfigurationUserStatus]] = Field(alias="userStatuses",default=None,)
	userStatusOverview: Optional[DeviceConfigurationUserOverview] = Field(alias="userStatusOverview",default=None,)
	accountsBlockAddingNonMicrosoftAccountEmail: Optional[bool] = Field(alias="accountsBlockAddingNonMicrosoftAccountEmail",default=None,)
	activateAppsWithVoice: Optional[Enablement | str] = Field(alias="activateAppsWithVoice",default=None,)
	antiTheftModeBlocked: Optional[bool] = Field(alias="antiTheftModeBlocked",default=None,)
	appManagementMSIAllowUserControlOverInstall: Optional[bool] = Field(alias="appManagementMSIAllowUserControlOverInstall",default=None,)
	appManagementMSIAlwaysInstallWithElevatedPrivileges: Optional[bool] = Field(alias="appManagementMSIAlwaysInstallWithElevatedPrivileges",default=None,)
	appManagementPackageFamilyNamesToLaunchAfterLogOn: Optional[list[str]] = Field(alias="appManagementPackageFamilyNamesToLaunchAfterLogOn",default=None,)
	appsAllowTrustedAppsSideloading: Optional[StateManagementSetting | str] = Field(alias="appsAllowTrustedAppsSideloading",default=None,)
	appsBlockWindowsStoreOriginatedApps: Optional[bool] = Field(alias="appsBlockWindowsStoreOriginatedApps",default=None,)
	authenticationAllowSecondaryDevice: Optional[bool] = Field(alias="authenticationAllowSecondaryDevice",default=None,)
	authenticationPreferredAzureADTenantDomainName: Optional[str] = Field(alias="authenticationPreferredAzureADTenantDomainName",default=None,)
	authenticationWebSignIn: Optional[Enablement | str] = Field(alias="authenticationWebSignIn",default=None,)
	bluetoothAllowedServices: Optional[list[str]] = Field(alias="bluetoothAllowedServices",default=None,)
	bluetoothBlockAdvertising: Optional[bool] = Field(alias="bluetoothBlockAdvertising",default=None,)
	bluetoothBlockDiscoverableMode: Optional[bool] = Field(alias="bluetoothBlockDiscoverableMode",default=None,)
	bluetoothBlocked: Optional[bool] = Field(alias="bluetoothBlocked",default=None,)
	bluetoothBlockPrePairing: Optional[bool] = Field(alias="bluetoothBlockPrePairing",default=None,)
	bluetoothBlockPromptedProximalConnections: Optional[bool] = Field(alias="bluetoothBlockPromptedProximalConnections",default=None,)
	cameraBlocked: Optional[bool] = Field(alias="cameraBlocked",default=None,)
	cellularBlockDataWhenRoaming: Optional[bool] = Field(alias="cellularBlockDataWhenRoaming",default=None,)
	cellularBlockVpn: Optional[bool] = Field(alias="cellularBlockVpn",default=None,)
	cellularBlockVpnWhenRoaming: Optional[bool] = Field(alias="cellularBlockVpnWhenRoaming",default=None,)
	cellularData: Optional[ConfigurationUsage | str] = Field(alias="cellularData",default=None,)
	certificatesBlockManualRootCertificateInstallation: Optional[bool] = Field(alias="certificatesBlockManualRootCertificateInstallation",default=None,)
	configureTimeZone: Optional[str] = Field(alias="configureTimeZone",default=None,)
	connectedDevicesServiceBlocked: Optional[bool] = Field(alias="connectedDevicesServiceBlocked",default=None,)
	copyPasteBlocked: Optional[bool] = Field(alias="copyPasteBlocked",default=None,)
	cortanaBlocked: Optional[bool] = Field(alias="cortanaBlocked",default=None,)
	cryptographyAllowFipsAlgorithmPolicy: Optional[bool] = Field(alias="cryptographyAllowFipsAlgorithmPolicy",default=None,)
	dataProtectionBlockDirectMemoryAccess: Optional[bool] = Field(alias="dataProtectionBlockDirectMemoryAccess",default=None,)
	defenderBlockEndUserAccess: Optional[bool] = Field(alias="defenderBlockEndUserAccess",default=None,)
	defenderBlockOnAccessProtection: Optional[bool] = Field(alias="defenderBlockOnAccessProtection",default=None,)
	defenderCloudBlockLevel: Optional[DefenderCloudBlockLevelType | str] = Field(alias="defenderCloudBlockLevel",default=None,)
	defenderCloudExtendedTimeout: Optional[int] = Field(alias="defenderCloudExtendedTimeout",default=None,)
	defenderCloudExtendedTimeoutInSeconds: Optional[int] = Field(alias="defenderCloudExtendedTimeoutInSeconds",default=None,)
	defenderDaysBeforeDeletingQuarantinedMalware: Optional[int] = Field(alias="defenderDaysBeforeDeletingQuarantinedMalware",default=None,)
	defenderDetectedMalwareActions: Optional[DefenderDetectedMalwareActions] = Field(alias="defenderDetectedMalwareActions",default=None,)
	defenderDisableCatchupFullScan: Optional[bool] = Field(alias="defenderDisableCatchupFullScan",default=None,)
	defenderDisableCatchupQuickScan: Optional[bool] = Field(alias="defenderDisableCatchupQuickScan",default=None,)
	defenderFileExtensionsToExclude: Optional[list[str]] = Field(alias="defenderFileExtensionsToExclude",default=None,)
	defenderFilesAndFoldersToExclude: Optional[list[str]] = Field(alias="defenderFilesAndFoldersToExclude",default=None,)
	defenderMonitorFileActivity: Optional[DefenderMonitorFileActivity | str] = Field(alias="defenderMonitorFileActivity",default=None,)
	defenderPotentiallyUnwantedAppAction: Optional[DefenderPotentiallyUnwantedAppAction | str] = Field(alias="defenderPotentiallyUnwantedAppAction",default=None,)
	defenderPotentiallyUnwantedAppActionSetting: Optional[DefenderProtectionType | str] = Field(alias="defenderPotentiallyUnwantedAppActionSetting",default=None,)
	defenderProcessesToExclude: Optional[list[str]] = Field(alias="defenderProcessesToExclude",default=None,)
	defenderPromptForSampleSubmission: Optional[DefenderPromptForSampleSubmission | str] = Field(alias="defenderPromptForSampleSubmission",default=None,)
	defenderRequireBehaviorMonitoring: Optional[bool] = Field(alias="defenderRequireBehaviorMonitoring",default=None,)
	defenderRequireCloudProtection: Optional[bool] = Field(alias="defenderRequireCloudProtection",default=None,)
	defenderRequireNetworkInspectionSystem: Optional[bool] = Field(alias="defenderRequireNetworkInspectionSystem",default=None,)
	defenderRequireRealTimeMonitoring: Optional[bool] = Field(alias="defenderRequireRealTimeMonitoring",default=None,)
	defenderScanArchiveFiles: Optional[bool] = Field(alias="defenderScanArchiveFiles",default=None,)
	defenderScanDownloads: Optional[bool] = Field(alias="defenderScanDownloads",default=None,)
	defenderScanIncomingMail: Optional[bool] = Field(alias="defenderScanIncomingMail",default=None,)
	defenderScanMappedNetworkDrivesDuringFullScan: Optional[bool] = Field(alias="defenderScanMappedNetworkDrivesDuringFullScan",default=None,)
	defenderScanMaxCpu: Optional[int] = Field(alias="defenderScanMaxCpu",default=None,)
	defenderScanNetworkFiles: Optional[bool] = Field(alias="defenderScanNetworkFiles",default=None,)
	defenderScanRemovableDrivesDuringFullScan: Optional[bool] = Field(alias="defenderScanRemovableDrivesDuringFullScan",default=None,)
	defenderScanScriptsLoadedInInternetExplorer: Optional[bool] = Field(alias="defenderScanScriptsLoadedInInternetExplorer",default=None,)
	defenderScanType: Optional[DefenderScanType | str] = Field(alias="defenderScanType",default=None,)
	defenderScheduledQuickScanTime: Optional[str] = Field(alias="defenderScheduledQuickScanTime",default=None,)
	defenderScheduledScanTime: Optional[str] = Field(alias="defenderScheduledScanTime",default=None,)
	defenderScheduleScanEnableLowCpuPriority: Optional[bool] = Field(alias="defenderScheduleScanEnableLowCpuPriority",default=None,)
	defenderSignatureUpdateIntervalInHours: Optional[int] = Field(alias="defenderSignatureUpdateIntervalInHours",default=None,)
	defenderSubmitSamplesConsentType: Optional[DefenderSubmitSamplesConsentType | str] = Field(alias="defenderSubmitSamplesConsentType",default=None,)
	defenderSystemScanSchedule: Optional[WeeklySchedule | str] = Field(alias="defenderSystemScanSchedule",default=None,)
	developerUnlockSetting: Optional[StateManagementSetting | str] = Field(alias="developerUnlockSetting",default=None,)
	deviceManagementBlockFactoryResetOnMobile: Optional[bool] = Field(alias="deviceManagementBlockFactoryResetOnMobile",default=None,)
	deviceManagementBlockManualUnenroll: Optional[bool] = Field(alias="deviceManagementBlockManualUnenroll",default=None,)
	diagnosticsDataSubmissionMode: Optional[DiagnosticDataSubmissionMode | str] = Field(alias="diagnosticsDataSubmissionMode",default=None,)
	displayAppListWithGdiDPIScalingTurnedOff: Optional[list[str]] = Field(alias="displayAppListWithGdiDPIScalingTurnedOff",default=None,)
	displayAppListWithGdiDPIScalingTurnedOn: Optional[list[str]] = Field(alias="displayAppListWithGdiDPIScalingTurnedOn",default=None,)
	edgeAllowStartPagesModification: Optional[bool] = Field(alias="edgeAllowStartPagesModification",default=None,)
	edgeBlockAccessToAboutFlags: Optional[bool] = Field(alias="edgeBlockAccessToAboutFlags",default=None,)
	edgeBlockAddressBarDropdown: Optional[bool] = Field(alias="edgeBlockAddressBarDropdown",default=None,)
	edgeBlockAutofill: Optional[bool] = Field(alias="edgeBlockAutofill",default=None,)
	edgeBlockCompatibilityList: Optional[bool] = Field(alias="edgeBlockCompatibilityList",default=None,)
	edgeBlockDeveloperTools: Optional[bool] = Field(alias="edgeBlockDeveloperTools",default=None,)
	edgeBlocked: Optional[bool] = Field(alias="edgeBlocked",default=None,)
	edgeBlockEditFavorites: Optional[bool] = Field(alias="edgeBlockEditFavorites",default=None,)
	edgeBlockExtensions: Optional[bool] = Field(alias="edgeBlockExtensions",default=None,)
	edgeBlockFullScreenMode: Optional[bool] = Field(alias="edgeBlockFullScreenMode",default=None,)
	edgeBlockInPrivateBrowsing: Optional[bool] = Field(alias="edgeBlockInPrivateBrowsing",default=None,)
	edgeBlockJavaScript: Optional[bool] = Field(alias="edgeBlockJavaScript",default=None,)
	edgeBlockLiveTileDataCollection: Optional[bool] = Field(alias="edgeBlockLiveTileDataCollection",default=None,)
	edgeBlockPasswordManager: Optional[bool] = Field(alias="edgeBlockPasswordManager",default=None,)
	edgeBlockPopups: Optional[bool] = Field(alias="edgeBlockPopups",default=None,)
	edgeBlockPrelaunch: Optional[bool] = Field(alias="edgeBlockPrelaunch",default=None,)
	edgeBlockPrinting: Optional[bool] = Field(alias="edgeBlockPrinting",default=None,)
	edgeBlockSavingHistory: Optional[bool] = Field(alias="edgeBlockSavingHistory",default=None,)
	edgeBlockSearchEngineCustomization: Optional[bool] = Field(alias="edgeBlockSearchEngineCustomization",default=None,)
	edgeBlockSearchSuggestions: Optional[bool] = Field(alias="edgeBlockSearchSuggestions",default=None,)
	edgeBlockSendingDoNotTrackHeader: Optional[bool] = Field(alias="edgeBlockSendingDoNotTrackHeader",default=None,)
	edgeBlockSendingIntranetTrafficToInternetExplorer: Optional[bool] = Field(alias="edgeBlockSendingIntranetTrafficToInternetExplorer",default=None,)
	edgeBlockSideloadingExtensions: Optional[bool] = Field(alias="edgeBlockSideloadingExtensions",default=None,)
	edgeBlockTabPreloading: Optional[bool] = Field(alias="edgeBlockTabPreloading",default=None,)
	edgeBlockWebContentOnNewTabPage: Optional[bool] = Field(alias="edgeBlockWebContentOnNewTabPage",default=None,)
	edgeClearBrowsingDataOnExit: Optional[bool] = Field(alias="edgeClearBrowsingDataOnExit",default=None,)
	edgeCookiePolicy: Optional[EdgeCookiePolicy | str] = Field(alias="edgeCookiePolicy",default=None,)
	edgeDisableFirstRunPage: Optional[bool] = Field(alias="edgeDisableFirstRunPage",default=None,)
	edgeEnterpriseModeSiteListLocation: Optional[str] = Field(alias="edgeEnterpriseModeSiteListLocation",default=None,)
	edgeFavoritesBarVisibility: Optional[VisibilitySetting | str] = Field(alias="edgeFavoritesBarVisibility",default=None,)
	edgeFavoritesListLocation: Optional[str] = Field(alias="edgeFavoritesListLocation",default=None,)
	edgeFirstRunUrl: Optional[str] = Field(alias="edgeFirstRunUrl",default=None,)
	edgeHomeButtonConfiguration: SerializeAsAny[Optional[EdgeHomeButtonConfiguration]] = Field(alias="edgeHomeButtonConfiguration",default=None,)
	edgeHomeButtonConfigurationEnabled: Optional[bool] = Field(alias="edgeHomeButtonConfigurationEnabled",default=None,)
	edgeHomepageUrls: Optional[list[str]] = Field(alias="edgeHomepageUrls",default=None,)
	edgeKioskModeRestriction: Optional[EdgeKioskModeRestrictionType | str] = Field(alias="edgeKioskModeRestriction",default=None,)
	edgeKioskResetAfterIdleTimeInMinutes: Optional[int] = Field(alias="edgeKioskResetAfterIdleTimeInMinutes",default=None,)
	edgeNewTabPageURL: Optional[str] = Field(alias="edgeNewTabPageURL",default=None,)
	edgeOpensWith: Optional[EdgeOpenOptions | str] = Field(alias="edgeOpensWith",default=None,)
	edgePreventCertificateErrorOverride: Optional[bool] = Field(alias="edgePreventCertificateErrorOverride",default=None,)
	edgeRequiredExtensionPackageFamilyNames: Optional[list[str]] = Field(alias="edgeRequiredExtensionPackageFamilyNames",default=None,)
	edgeRequireSmartScreen: Optional[bool] = Field(alias="edgeRequireSmartScreen",default=None,)
	edgeSearchEngine: SerializeAsAny[Optional[EdgeSearchEngineBase]] = Field(alias="edgeSearchEngine",default=None,)
	edgeSendIntranetTrafficToInternetExplorer: Optional[bool] = Field(alias="edgeSendIntranetTrafficToInternetExplorer",default=None,)
	edgeShowMessageWhenOpeningInternetExplorerSites: Optional[InternetExplorerMessageSetting | str] = Field(alias="edgeShowMessageWhenOpeningInternetExplorerSites",default=None,)
	edgeSyncFavoritesWithInternetExplorer: Optional[bool] = Field(alias="edgeSyncFavoritesWithInternetExplorer",default=None,)
	edgeTelemetryForMicrosoft365Analytics: Optional[EdgeTelemetryMode | str] = Field(alias="edgeTelemetryForMicrosoft365Analytics",default=None,)
	enableAutomaticRedeployment: Optional[bool] = Field(alias="enableAutomaticRedeployment",default=None,)
	energySaverOnBatteryThresholdPercentage: Optional[int] = Field(alias="energySaverOnBatteryThresholdPercentage",default=None,)
	energySaverPluggedInThresholdPercentage: Optional[int] = Field(alias="energySaverPluggedInThresholdPercentage",default=None,)
	enterpriseCloudPrintDiscoveryEndPoint: Optional[str] = Field(alias="enterpriseCloudPrintDiscoveryEndPoint",default=None,)
	enterpriseCloudPrintDiscoveryMaxLimit: Optional[int] = Field(alias="enterpriseCloudPrintDiscoveryMaxLimit",default=None,)
	enterpriseCloudPrintMopriaDiscoveryResourceIdentifier: Optional[str] = Field(alias="enterpriseCloudPrintMopriaDiscoveryResourceIdentifier",default=None,)
	enterpriseCloudPrintOAuthAuthority: Optional[str] = Field(alias="enterpriseCloudPrintOAuthAuthority",default=None,)
	enterpriseCloudPrintOAuthClientIdentifier: Optional[str] = Field(alias="enterpriseCloudPrintOAuthClientIdentifier",default=None,)
	enterpriseCloudPrintResourceIdentifier: Optional[str] = Field(alias="enterpriseCloudPrintResourceIdentifier",default=None,)
	experienceBlockDeviceDiscovery: Optional[bool] = Field(alias="experienceBlockDeviceDiscovery",default=None,)
	experienceBlockErrorDialogWhenNoSIM: Optional[bool] = Field(alias="experienceBlockErrorDialogWhenNoSIM",default=None,)
	experienceBlockTaskSwitcher: Optional[bool] = Field(alias="experienceBlockTaskSwitcher",default=None,)
	experienceDoNotSyncBrowserSettings: Optional[BrowserSyncSetting | str] = Field(alias="experienceDoNotSyncBrowserSettings",default=None,)
	findMyFiles: Optional[Enablement | str] = Field(alias="findMyFiles",default=None,)
	gameDvrBlocked: Optional[bool] = Field(alias="gameDvrBlocked",default=None,)
	inkWorkspaceAccess: Optional[InkAccessSetting | str] = Field(alias="inkWorkspaceAccess",default=None,)
	inkWorkspaceAccessState: Optional[StateManagementSetting | str] = Field(alias="inkWorkspaceAccessState",default=None,)
	inkWorkspaceBlockSuggestedApps: Optional[bool] = Field(alias="inkWorkspaceBlockSuggestedApps",default=None,)
	internetSharingBlocked: Optional[bool] = Field(alias="internetSharingBlocked",default=None,)
	locationServicesBlocked: Optional[bool] = Field(alias="locationServicesBlocked",default=None,)
	lockScreenActivateAppsWithVoice: Optional[Enablement | str] = Field(alias="lockScreenActivateAppsWithVoice",default=None,)
	lockScreenAllowTimeoutConfiguration: Optional[bool] = Field(alias="lockScreenAllowTimeoutConfiguration",default=None,)
	lockScreenBlockActionCenterNotifications: Optional[bool] = Field(alias="lockScreenBlockActionCenterNotifications",default=None,)
	lockScreenBlockCortana: Optional[bool] = Field(alias="lockScreenBlockCortana",default=None,)
	lockScreenBlockToastNotifications: Optional[bool] = Field(alias="lockScreenBlockToastNotifications",default=None,)
	lockScreenTimeoutInSeconds: Optional[int] = Field(alias="lockScreenTimeoutInSeconds",default=None,)
	logonBlockFastUserSwitching: Optional[bool] = Field(alias="logonBlockFastUserSwitching",default=None,)
	messagingBlockMMS: Optional[bool] = Field(alias="messagingBlockMMS",default=None,)
	messagingBlockRichCommunicationServices: Optional[bool] = Field(alias="messagingBlockRichCommunicationServices",default=None,)
	messagingBlockSync: Optional[bool] = Field(alias="messagingBlockSync",default=None,)
	microsoftAccountBlocked: Optional[bool] = Field(alias="microsoftAccountBlocked",default=None,)
	microsoftAccountBlockSettingsSync: Optional[bool] = Field(alias="microsoftAccountBlockSettingsSync",default=None,)
	microsoftAccountSignInAssistantSettings: Optional[SignInAssistantOptions | str] = Field(alias="microsoftAccountSignInAssistantSettings",default=None,)
	networkProxyApplySettingsDeviceWide: Optional[bool] = Field(alias="networkProxyApplySettingsDeviceWide",default=None,)
	networkProxyAutomaticConfigurationUrl: Optional[str] = Field(alias="networkProxyAutomaticConfigurationUrl",default=None,)
	networkProxyDisableAutoDetect: Optional[bool] = Field(alias="networkProxyDisableAutoDetect",default=None,)
	networkProxyServer: Optional[Windows10NetworkProxyServer] = Field(alias="networkProxyServer",default=None,)
	nfcBlocked: Optional[bool] = Field(alias="nfcBlocked",default=None,)
	oneDriveDisableFileSync: Optional[bool] = Field(alias="oneDriveDisableFileSync",default=None,)
	passwordBlockSimple: Optional[bool] = Field(alias="passwordBlockSimple",default=None,)
	passwordExpirationDays: Optional[int] = Field(alias="passwordExpirationDays",default=None,)
	passwordMinimumAgeInDays: Optional[int] = Field(alias="passwordMinimumAgeInDays",default=None,)
	passwordMinimumCharacterSetCount: Optional[int] = Field(alias="passwordMinimumCharacterSetCount",default=None,)
	passwordMinimumLength: Optional[int] = Field(alias="passwordMinimumLength",default=None,)
	passwordMinutesOfInactivityBeforeScreenTimeout: Optional[int] = Field(alias="passwordMinutesOfInactivityBeforeScreenTimeout",default=None,)
	passwordPreviousPasswordBlockCount: Optional[int] = Field(alias="passwordPreviousPasswordBlockCount",default=None,)
	passwordRequired: Optional[bool] = Field(alias="passwordRequired",default=None,)
	passwordRequiredType: Optional[RequiredPasswordType | str] = Field(alias="passwordRequiredType",default=None,)
	passwordRequireWhenResumeFromIdleState: Optional[bool] = Field(alias="passwordRequireWhenResumeFromIdleState",default=None,)
	passwordSignInFailureCountBeforeFactoryReset: Optional[int] = Field(alias="passwordSignInFailureCountBeforeFactoryReset",default=None,)
	personalizationDesktopImageUrl: Optional[str] = Field(alias="personalizationDesktopImageUrl",default=None,)
	personalizationLockScreenImageUrl: Optional[str] = Field(alias="personalizationLockScreenImageUrl",default=None,)
	powerButtonActionOnBattery: Optional[PowerActionType | str] = Field(alias="powerButtonActionOnBattery",default=None,)
	powerButtonActionPluggedIn: Optional[PowerActionType | str] = Field(alias="powerButtonActionPluggedIn",default=None,)
	powerHybridSleepOnBattery: Optional[Enablement | str] = Field(alias="powerHybridSleepOnBattery",default=None,)
	powerHybridSleepPluggedIn: Optional[Enablement | str] = Field(alias="powerHybridSleepPluggedIn",default=None,)
	powerLidCloseActionOnBattery: Optional[PowerActionType | str] = Field(alias="powerLidCloseActionOnBattery",default=None,)
	powerLidCloseActionPluggedIn: Optional[PowerActionType | str] = Field(alias="powerLidCloseActionPluggedIn",default=None,)
	powerSleepButtonActionOnBattery: Optional[PowerActionType | str] = Field(alias="powerSleepButtonActionOnBattery",default=None,)
	powerSleepButtonActionPluggedIn: Optional[PowerActionType | str] = Field(alias="powerSleepButtonActionPluggedIn",default=None,)
	printerBlockAddition: Optional[bool] = Field(alias="printerBlockAddition",default=None,)
	printerDefaultName: Optional[str] = Field(alias="printerDefaultName",default=None,)
	printerNames: Optional[list[str]] = Field(alias="printerNames",default=None,)
	privacyAdvertisingId: Optional[StateManagementSetting | str] = Field(alias="privacyAdvertisingId",default=None,)
	privacyAutoAcceptPairingAndConsentPrompts: Optional[bool] = Field(alias="privacyAutoAcceptPairingAndConsentPrompts",default=None,)
	privacyBlockActivityFeed: Optional[bool] = Field(alias="privacyBlockActivityFeed",default=None,)
	privacyBlockInputPersonalization: Optional[bool] = Field(alias="privacyBlockInputPersonalization",default=None,)
	privacyBlockPublishUserActivities: Optional[bool] = Field(alias="privacyBlockPublishUserActivities",default=None,)
	privacyDisableLaunchExperience: Optional[bool] = Field(alias="privacyDisableLaunchExperience",default=None,)
	resetProtectionModeBlocked: Optional[bool] = Field(alias="resetProtectionModeBlocked",default=None,)
	safeSearchFilter: Optional[SafeSearchFilterType | str] = Field(alias="safeSearchFilter",default=None,)
	screenCaptureBlocked: Optional[bool] = Field(alias="screenCaptureBlocked",default=None,)
	searchBlockDiacritics: Optional[bool] = Field(alias="searchBlockDiacritics",default=None,)
	searchBlockWebResults: Optional[bool] = Field(alias="searchBlockWebResults",default=None,)
	searchDisableAutoLanguageDetection: Optional[bool] = Field(alias="searchDisableAutoLanguageDetection",default=None,)
	searchDisableIndexerBackoff: Optional[bool] = Field(alias="searchDisableIndexerBackoff",default=None,)
	searchDisableIndexingEncryptedItems: Optional[bool] = Field(alias="searchDisableIndexingEncryptedItems",default=None,)
	searchDisableIndexingRemovableDrive: Optional[bool] = Field(alias="searchDisableIndexingRemovableDrive",default=None,)
	searchDisableLocation: Optional[bool] = Field(alias="searchDisableLocation",default=None,)
	searchDisableUseLocation: Optional[bool] = Field(alias="searchDisableUseLocation",default=None,)
	searchEnableAutomaticIndexSizeManangement: Optional[bool] = Field(alias="searchEnableAutomaticIndexSizeManangement",default=None,)
	searchEnableRemoteQueries: Optional[bool] = Field(alias="searchEnableRemoteQueries",default=None,)
	securityBlockAzureADJoinedDevicesAutoEncryption: Optional[bool] = Field(alias="securityBlockAzureADJoinedDevicesAutoEncryption",default=None,)
	settingsBlockAccountsPage: Optional[bool] = Field(alias="settingsBlockAccountsPage",default=None,)
	settingsBlockAddProvisioningPackage: Optional[bool] = Field(alias="settingsBlockAddProvisioningPackage",default=None,)
	settingsBlockAppsPage: Optional[bool] = Field(alias="settingsBlockAppsPage",default=None,)
	settingsBlockChangeLanguage: Optional[bool] = Field(alias="settingsBlockChangeLanguage",default=None,)
	settingsBlockChangePowerSleep: Optional[bool] = Field(alias="settingsBlockChangePowerSleep",default=None,)
	settingsBlockChangeRegion: Optional[bool] = Field(alias="settingsBlockChangeRegion",default=None,)
	settingsBlockChangeSystemTime: Optional[bool] = Field(alias="settingsBlockChangeSystemTime",default=None,)
	settingsBlockDevicesPage: Optional[bool] = Field(alias="settingsBlockDevicesPage",default=None,)
	settingsBlockEaseOfAccessPage: Optional[bool] = Field(alias="settingsBlockEaseOfAccessPage",default=None,)
	settingsBlockEditDeviceName: Optional[bool] = Field(alias="settingsBlockEditDeviceName",default=None,)
	settingsBlockGamingPage: Optional[bool] = Field(alias="settingsBlockGamingPage",default=None,)
	settingsBlockNetworkInternetPage: Optional[bool] = Field(alias="settingsBlockNetworkInternetPage",default=None,)
	settingsBlockPersonalizationPage: Optional[bool] = Field(alias="settingsBlockPersonalizationPage",default=None,)
	settingsBlockPrivacyPage: Optional[bool] = Field(alias="settingsBlockPrivacyPage",default=None,)
	settingsBlockRemoveProvisioningPackage: Optional[bool] = Field(alias="settingsBlockRemoveProvisioningPackage",default=None,)
	settingsBlockSettingsApp: Optional[bool] = Field(alias="settingsBlockSettingsApp",default=None,)
	settingsBlockSystemPage: Optional[bool] = Field(alias="settingsBlockSystemPage",default=None,)
	settingsBlockTimeLanguagePage: Optional[bool] = Field(alias="settingsBlockTimeLanguagePage",default=None,)
	settingsBlockUpdateSecurityPage: Optional[bool] = Field(alias="settingsBlockUpdateSecurityPage",default=None,)
	sharedUserAppDataAllowed: Optional[bool] = Field(alias="sharedUserAppDataAllowed",default=None,)
	smartScreenAppInstallControl: Optional[AppInstallControlType | str] = Field(alias="smartScreenAppInstallControl",default=None,)
	smartScreenBlockPromptOverride: Optional[bool] = Field(alias="smartScreenBlockPromptOverride",default=None,)
	smartScreenBlockPromptOverrideForFiles: Optional[bool] = Field(alias="smartScreenBlockPromptOverrideForFiles",default=None,)
	smartScreenEnableAppInstallControl: Optional[bool] = Field(alias="smartScreenEnableAppInstallControl",default=None,)
	startBlockUnpinningAppsFromTaskbar: Optional[bool] = Field(alias="startBlockUnpinningAppsFromTaskbar",default=None,)
	startMenuAppListVisibility: Optional[WindowsStartMenuAppListVisibilityType | str] = Field(alias="startMenuAppListVisibility",default=None,)
	startMenuHideChangeAccountSettings: Optional[bool] = Field(alias="startMenuHideChangeAccountSettings",default=None,)
	startMenuHideFrequentlyUsedApps: Optional[bool] = Field(alias="startMenuHideFrequentlyUsedApps",default=None,)
	startMenuHideHibernate: Optional[bool] = Field(alias="startMenuHideHibernate",default=None,)
	startMenuHideLock: Optional[bool] = Field(alias="startMenuHideLock",default=None,)
	startMenuHidePowerButton: Optional[bool] = Field(alias="startMenuHidePowerButton",default=None,)
	startMenuHideRecentJumpLists: Optional[bool] = Field(alias="startMenuHideRecentJumpLists",default=None,)
	startMenuHideRecentlyAddedApps: Optional[bool] = Field(alias="startMenuHideRecentlyAddedApps",default=None,)
	startMenuHideRestartOptions: Optional[bool] = Field(alias="startMenuHideRestartOptions",default=None,)
	startMenuHideShutDown: Optional[bool] = Field(alias="startMenuHideShutDown",default=None,)
	startMenuHideSignOut: Optional[bool] = Field(alias="startMenuHideSignOut",default=None,)
	startMenuHideSleep: Optional[bool] = Field(alias="startMenuHideSleep",default=None,)
	startMenuHideSwitchAccount: Optional[bool] = Field(alias="startMenuHideSwitchAccount",default=None,)
	startMenuHideUserTile: Optional[bool] = Field(alias="startMenuHideUserTile",default=None,)
	startMenuLayoutEdgeAssetsXml: Optional[str] = Field(alias="startMenuLayoutEdgeAssetsXml",default=None,)
	startMenuLayoutXml: Optional[str] = Field(alias="startMenuLayoutXml",default=None,)
	startMenuMode: Optional[WindowsStartMenuModeType | str] = Field(alias="startMenuMode",default=None,)
	startMenuPinnedFolderDocuments: Optional[VisibilitySetting | str] = Field(alias="startMenuPinnedFolderDocuments",default=None,)
	startMenuPinnedFolderDownloads: Optional[VisibilitySetting | str] = Field(alias="startMenuPinnedFolderDownloads",default=None,)
	startMenuPinnedFolderFileExplorer: Optional[VisibilitySetting | str] = Field(alias="startMenuPinnedFolderFileExplorer",default=None,)
	startMenuPinnedFolderHomeGroup: Optional[VisibilitySetting | str] = Field(alias="startMenuPinnedFolderHomeGroup",default=None,)
	startMenuPinnedFolderMusic: Optional[VisibilitySetting | str] = Field(alias="startMenuPinnedFolderMusic",default=None,)
	startMenuPinnedFolderNetwork: Optional[VisibilitySetting | str] = Field(alias="startMenuPinnedFolderNetwork",default=None,)
	startMenuPinnedFolderPersonalFolder: Optional[VisibilitySetting | str] = Field(alias="startMenuPinnedFolderPersonalFolder",default=None,)
	startMenuPinnedFolderPictures: Optional[VisibilitySetting | str] = Field(alias="startMenuPinnedFolderPictures",default=None,)
	startMenuPinnedFolderSettings: Optional[VisibilitySetting | str] = Field(alias="startMenuPinnedFolderSettings",default=None,)
	startMenuPinnedFolderVideos: Optional[VisibilitySetting | str] = Field(alias="startMenuPinnedFolderVideos",default=None,)
	storageBlockRemovableStorage: Optional[bool] = Field(alias="storageBlockRemovableStorage",default=None,)
	storageRequireMobileDeviceEncryption: Optional[bool] = Field(alias="storageRequireMobileDeviceEncryption",default=None,)
	storageRestrictAppDataToSystemVolume: Optional[bool] = Field(alias="storageRestrictAppDataToSystemVolume",default=None,)
	storageRestrictAppInstallToSystemVolume: Optional[bool] = Field(alias="storageRestrictAppInstallToSystemVolume",default=None,)
	systemTelemetryProxyServer: Optional[str] = Field(alias="systemTelemetryProxyServer",default=None,)
	taskManagerBlockEndTask: Optional[bool] = Field(alias="taskManagerBlockEndTask",default=None,)
	tenantLockdownRequireNetworkDuringOutOfBoxExperience: Optional[bool] = Field(alias="tenantLockdownRequireNetworkDuringOutOfBoxExperience",default=None,)
	uninstallBuiltInApps: Optional[bool] = Field(alias="uninstallBuiltInApps",default=None,)
	usbBlocked: Optional[bool] = Field(alias="usbBlocked",default=None,)
	voiceRecordingBlocked: Optional[bool] = Field(alias="voiceRecordingBlocked",default=None,)
	webRtcBlockLocalhostIpAddress: Optional[bool] = Field(alias="webRtcBlockLocalhostIpAddress",default=None,)
	wiFiBlockAutomaticConnectHotspots: Optional[bool] = Field(alias="wiFiBlockAutomaticConnectHotspots",default=None,)
	wiFiBlocked: Optional[bool] = Field(alias="wiFiBlocked",default=None,)
	wiFiBlockManualConfiguration: Optional[bool] = Field(alias="wiFiBlockManualConfiguration",default=None,)
	wiFiScanInterval: Optional[int] = Field(alias="wiFiScanInterval",default=None,)
	windows10AppsForceUpdateSchedule: Optional[Windows10AppsForceUpdateSchedule] = Field(alias="windows10AppsForceUpdateSchedule",default=None,)
	windowsSpotlightBlockConsumerSpecificFeatures: Optional[bool] = Field(alias="windowsSpotlightBlockConsumerSpecificFeatures",default=None,)
	windowsSpotlightBlocked: Optional[bool] = Field(alias="windowsSpotlightBlocked",default=None,)
	windowsSpotlightBlockOnActionCenter: Optional[bool] = Field(alias="windowsSpotlightBlockOnActionCenter",default=None,)
	windowsSpotlightBlockTailoredExperiences: Optional[bool] = Field(alias="windowsSpotlightBlockTailoredExperiences",default=None,)
	windowsSpotlightBlockThirdPartyNotifications: Optional[bool] = Field(alias="windowsSpotlightBlockThirdPartyNotifications",default=None,)
	windowsSpotlightBlockWelcomeExperience: Optional[bool] = Field(alias="windowsSpotlightBlockWelcomeExperience",default=None,)
	windowsSpotlightBlockWindowsTips: Optional[bool] = Field(alias="windowsSpotlightBlockWindowsTips",default=None,)
	windowsSpotlightConfigureOnLockScreen: Optional[WindowsSpotlightEnablementSettings | str] = Field(alias="windowsSpotlightConfigureOnLockScreen",default=None,)
	windowsStoreBlockAutoUpdate: Optional[bool] = Field(alias="windowsStoreBlockAutoUpdate",default=None,)
	windowsStoreBlocked: Optional[bool] = Field(alias="windowsStoreBlocked",default=None,)
	windowsStoreEnablePrivateStoreOnly: Optional[bool] = Field(alias="windowsStoreEnablePrivateStoreOnly",default=None,)
	wirelessDisplayBlockProjectionToThisDevice: Optional[bool] = Field(alias="wirelessDisplayBlockProjectionToThisDevice",default=None,)
	wirelessDisplayBlockUserInputFromReceiver: Optional[bool] = Field(alias="wirelessDisplayBlockUserInputFromReceiver",default=None,)
	wirelessDisplayRequirePinForPairing: Optional[bool] = Field(alias="wirelessDisplayRequirePinForPairing",default=None,)
	privacyAccessControls: Optional[list[WindowsPrivacyDataAccessControlItem]] = Field(alias="privacyAccessControls",default=None,)

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
from .enablement import Enablement
from .state_management_setting import StateManagementSetting
from .enablement import Enablement
from .configuration_usage import ConfigurationUsage
from .defender_cloud_block_level_type import DefenderCloudBlockLevelType
from .defender_detected_malware_actions import DefenderDetectedMalwareActions
from .defender_monitor_file_activity import DefenderMonitorFileActivity
from .defender_potentially_unwanted_app_action import DefenderPotentiallyUnwantedAppAction
from .defender_protection_type import DefenderProtectionType
from .defender_prompt_for_sample_submission import DefenderPromptForSampleSubmission
from .defender_scan_type import DefenderScanType
from .defender_submit_samples_consent_type import DefenderSubmitSamplesConsentType
from .weekly_schedule import WeeklySchedule
from .state_management_setting import StateManagementSetting
from .diagnostic_data_submission_mode import DiagnosticDataSubmissionMode
from .edge_cookie_policy import EdgeCookiePolicy
from .visibility_setting import VisibilitySetting
from .edge_home_button_configuration import EdgeHomeButtonConfiguration
from .edge_kiosk_mode_restriction_type import EdgeKioskModeRestrictionType
from .edge_open_options import EdgeOpenOptions
from .edge_search_engine_base import EdgeSearchEngineBase
from .internet_explorer_message_setting import InternetExplorerMessageSetting
from .edge_telemetry_mode import EdgeTelemetryMode
from .browser_sync_setting import BrowserSyncSetting
from .enablement import Enablement
from .ink_access_setting import InkAccessSetting
from .state_management_setting import StateManagementSetting
from .enablement import Enablement
from .sign_in_assistant_options import SignInAssistantOptions
from .windows10_network_proxy_server import Windows10NetworkProxyServer
from .required_password_type import RequiredPasswordType
from .power_action_type import PowerActionType
from .power_action_type import PowerActionType
from .enablement import Enablement
from .enablement import Enablement
from .power_action_type import PowerActionType
from .power_action_type import PowerActionType
from .power_action_type import PowerActionType
from .power_action_type import PowerActionType
from .state_management_setting import StateManagementSetting
from .safe_search_filter_type import SafeSearchFilterType
from .app_install_control_type import AppInstallControlType
from .windows_start_menu_app_list_visibility_type import WindowsStartMenuAppListVisibilityType
from .windows_start_menu_mode_type import WindowsStartMenuModeType
from .visibility_setting import VisibilitySetting
from .visibility_setting import VisibilitySetting
from .visibility_setting import VisibilitySetting
from .visibility_setting import VisibilitySetting
from .visibility_setting import VisibilitySetting
from .visibility_setting import VisibilitySetting
from .visibility_setting import VisibilitySetting
from .visibility_setting import VisibilitySetting
from .visibility_setting import VisibilitySetting
from .visibility_setting import VisibilitySetting
from .windows10_apps_force_update_schedule import Windows10AppsForceUpdateSchedule
from .windows_spotlight_enablement_settings import WindowsSpotlightEnablementSettings
from .windows_privacy_data_access_control_item import WindowsPrivacyDataAccessControlItem

