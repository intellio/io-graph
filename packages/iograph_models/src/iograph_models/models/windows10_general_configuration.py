from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class Windows10GeneralConfiguration(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	version: Optional[int] = Field(default=None,alias="version",)
	assignments: Optional[list[DeviceConfigurationAssignment]] = Field(default=None,alias="assignments",)
	deviceSettingStateSummaries: Optional[list[SettingStateDeviceSummary]] = Field(default=None,alias="deviceSettingStateSummaries",)
	deviceStatuses: Optional[list[DeviceConfigurationDeviceStatus]] = Field(default=None,alias="deviceStatuses",)
	deviceStatusOverview: Optional[DeviceConfigurationDeviceOverview] = Field(default=None,alias="deviceStatusOverview",)
	userStatuses: Optional[list[DeviceConfigurationUserStatus]] = Field(default=None,alias="userStatuses",)
	userStatusOverview: Optional[DeviceConfigurationUserOverview] = Field(default=None,alias="userStatusOverview",)
	accountsBlockAddingNonMicrosoftAccountEmail: Optional[bool] = Field(default=None,alias="accountsBlockAddingNonMicrosoftAccountEmail",)
	antiTheftModeBlocked: Optional[bool] = Field(default=None,alias="antiTheftModeBlocked",)
	appsAllowTrustedAppsSideloading: Optional[StateManagementSetting] = Field(default=None,alias="appsAllowTrustedAppsSideloading",)
	appsBlockWindowsStoreOriginatedApps: Optional[bool] = Field(default=None,alias="appsBlockWindowsStoreOriginatedApps",)
	bluetoothAllowedServices: Optional[list[str]] = Field(default=None,alias="bluetoothAllowedServices",)
	bluetoothBlockAdvertising: Optional[bool] = Field(default=None,alias="bluetoothBlockAdvertising",)
	bluetoothBlockDiscoverableMode: Optional[bool] = Field(default=None,alias="bluetoothBlockDiscoverableMode",)
	bluetoothBlocked: Optional[bool] = Field(default=None,alias="bluetoothBlocked",)
	bluetoothBlockPrePairing: Optional[bool] = Field(default=None,alias="bluetoothBlockPrePairing",)
	cameraBlocked: Optional[bool] = Field(default=None,alias="cameraBlocked",)
	cellularBlockDataWhenRoaming: Optional[bool] = Field(default=None,alias="cellularBlockDataWhenRoaming",)
	cellularBlockVpn: Optional[bool] = Field(default=None,alias="cellularBlockVpn",)
	cellularBlockVpnWhenRoaming: Optional[bool] = Field(default=None,alias="cellularBlockVpnWhenRoaming",)
	certificatesBlockManualRootCertificateInstallation: Optional[bool] = Field(default=None,alias="certificatesBlockManualRootCertificateInstallation",)
	connectedDevicesServiceBlocked: Optional[bool] = Field(default=None,alias="connectedDevicesServiceBlocked",)
	copyPasteBlocked: Optional[bool] = Field(default=None,alias="copyPasteBlocked",)
	cortanaBlocked: Optional[bool] = Field(default=None,alias="cortanaBlocked",)
	defenderBlockEndUserAccess: Optional[bool] = Field(default=None,alias="defenderBlockEndUserAccess",)
	defenderCloudBlockLevel: Optional[DefenderCloudBlockLevelType] = Field(default=None,alias="defenderCloudBlockLevel",)
	defenderDaysBeforeDeletingQuarantinedMalware: Optional[int] = Field(default=None,alias="defenderDaysBeforeDeletingQuarantinedMalware",)
	defenderDetectedMalwareActions: Optional[DefenderDetectedMalwareActions] = Field(default=None,alias="defenderDetectedMalwareActions",)
	defenderFileExtensionsToExclude: Optional[list[str]] = Field(default=None,alias="defenderFileExtensionsToExclude",)
	defenderFilesAndFoldersToExclude: Optional[list[str]] = Field(default=None,alias="defenderFilesAndFoldersToExclude",)
	defenderMonitorFileActivity: Optional[DefenderMonitorFileActivity] = Field(default=None,alias="defenderMonitorFileActivity",)
	defenderProcessesToExclude: Optional[list[str]] = Field(default=None,alias="defenderProcessesToExclude",)
	defenderPromptForSampleSubmission: Optional[DefenderPromptForSampleSubmission] = Field(default=None,alias="defenderPromptForSampleSubmission",)
	defenderRequireBehaviorMonitoring: Optional[bool] = Field(default=None,alias="defenderRequireBehaviorMonitoring",)
	defenderRequireCloudProtection: Optional[bool] = Field(default=None,alias="defenderRequireCloudProtection",)
	defenderRequireNetworkInspectionSystem: Optional[bool] = Field(default=None,alias="defenderRequireNetworkInspectionSystem",)
	defenderRequireRealTimeMonitoring: Optional[bool] = Field(default=None,alias="defenderRequireRealTimeMonitoring",)
	defenderScanArchiveFiles: Optional[bool] = Field(default=None,alias="defenderScanArchiveFiles",)
	defenderScanDownloads: Optional[bool] = Field(default=None,alias="defenderScanDownloads",)
	defenderScanIncomingMail: Optional[bool] = Field(default=None,alias="defenderScanIncomingMail",)
	defenderScanMappedNetworkDrivesDuringFullScan: Optional[bool] = Field(default=None,alias="defenderScanMappedNetworkDrivesDuringFullScan",)
	defenderScanMaxCpu: Optional[int] = Field(default=None,alias="defenderScanMaxCpu",)
	defenderScanNetworkFiles: Optional[bool] = Field(default=None,alias="defenderScanNetworkFiles",)
	defenderScanRemovableDrivesDuringFullScan: Optional[bool] = Field(default=None,alias="defenderScanRemovableDrivesDuringFullScan",)
	defenderScanScriptsLoadedInInternetExplorer: Optional[bool] = Field(default=None,alias="defenderScanScriptsLoadedInInternetExplorer",)
	defenderScanType: Optional[DefenderScanType] = Field(default=None,alias="defenderScanType",)
	defenderScheduledQuickScanTime: Optional[str] = Field(default=None,alias="defenderScheduledQuickScanTime",)
	defenderScheduledScanTime: Optional[str] = Field(default=None,alias="defenderScheduledScanTime",)
	defenderSignatureUpdateIntervalInHours: Optional[int] = Field(default=None,alias="defenderSignatureUpdateIntervalInHours",)
	defenderSystemScanSchedule: Optional[WeeklySchedule] = Field(default=None,alias="defenderSystemScanSchedule",)
	developerUnlockSetting: Optional[StateManagementSetting] = Field(default=None,alias="developerUnlockSetting",)
	deviceManagementBlockFactoryResetOnMobile: Optional[bool] = Field(default=None,alias="deviceManagementBlockFactoryResetOnMobile",)
	deviceManagementBlockManualUnenroll: Optional[bool] = Field(default=None,alias="deviceManagementBlockManualUnenroll",)
	diagnosticsDataSubmissionMode: Optional[DiagnosticDataSubmissionMode] = Field(default=None,alias="diagnosticsDataSubmissionMode",)
	edgeAllowStartPagesModification: Optional[bool] = Field(default=None,alias="edgeAllowStartPagesModification",)
	edgeBlockAccessToAboutFlags: Optional[bool] = Field(default=None,alias="edgeBlockAccessToAboutFlags",)
	edgeBlockAddressBarDropdown: Optional[bool] = Field(default=None,alias="edgeBlockAddressBarDropdown",)
	edgeBlockAutofill: Optional[bool] = Field(default=None,alias="edgeBlockAutofill",)
	edgeBlockCompatibilityList: Optional[bool] = Field(default=None,alias="edgeBlockCompatibilityList",)
	edgeBlockDeveloperTools: Optional[bool] = Field(default=None,alias="edgeBlockDeveloperTools",)
	edgeBlocked: Optional[bool] = Field(default=None,alias="edgeBlocked",)
	edgeBlockExtensions: Optional[bool] = Field(default=None,alias="edgeBlockExtensions",)
	edgeBlockInPrivateBrowsing: Optional[bool] = Field(default=None,alias="edgeBlockInPrivateBrowsing",)
	edgeBlockJavaScript: Optional[bool] = Field(default=None,alias="edgeBlockJavaScript",)
	edgeBlockLiveTileDataCollection: Optional[bool] = Field(default=None,alias="edgeBlockLiveTileDataCollection",)
	edgeBlockPasswordManager: Optional[bool] = Field(default=None,alias="edgeBlockPasswordManager",)
	edgeBlockPopups: Optional[bool] = Field(default=None,alias="edgeBlockPopups",)
	edgeBlockSearchSuggestions: Optional[bool] = Field(default=None,alias="edgeBlockSearchSuggestions",)
	edgeBlockSendingDoNotTrackHeader: Optional[bool] = Field(default=None,alias="edgeBlockSendingDoNotTrackHeader",)
	edgeBlockSendingIntranetTrafficToInternetExplorer: Optional[bool] = Field(default=None,alias="edgeBlockSendingIntranetTrafficToInternetExplorer",)
	edgeClearBrowsingDataOnExit: Optional[bool] = Field(default=None,alias="edgeClearBrowsingDataOnExit",)
	edgeCookiePolicy: Optional[EdgeCookiePolicy] = Field(default=None,alias="edgeCookiePolicy",)
	edgeDisableFirstRunPage: Optional[bool] = Field(default=None,alias="edgeDisableFirstRunPage",)
	edgeEnterpriseModeSiteListLocation: Optional[str] = Field(default=None,alias="edgeEnterpriseModeSiteListLocation",)
	edgeFirstRunUrl: Optional[str] = Field(default=None,alias="edgeFirstRunUrl",)
	edgeHomepageUrls: Optional[list[str]] = Field(default=None,alias="edgeHomepageUrls",)
	edgeRequireSmartScreen: Optional[bool] = Field(default=None,alias="edgeRequireSmartScreen",)
	edgeSearchEngine: Optional[EdgeSearchEngineBase] = Field(default=None,alias="edgeSearchEngine",)
	edgeSendIntranetTrafficToInternetExplorer: Optional[bool] = Field(default=None,alias="edgeSendIntranetTrafficToInternetExplorer",)
	edgeSyncFavoritesWithInternetExplorer: Optional[bool] = Field(default=None,alias="edgeSyncFavoritesWithInternetExplorer",)
	enterpriseCloudPrintDiscoveryEndPoint: Optional[str] = Field(default=None,alias="enterpriseCloudPrintDiscoveryEndPoint",)
	enterpriseCloudPrintDiscoveryMaxLimit: Optional[int] = Field(default=None,alias="enterpriseCloudPrintDiscoveryMaxLimit",)
	enterpriseCloudPrintMopriaDiscoveryResourceIdentifier: Optional[str] = Field(default=None,alias="enterpriseCloudPrintMopriaDiscoveryResourceIdentifier",)
	enterpriseCloudPrintOAuthAuthority: Optional[str] = Field(default=None,alias="enterpriseCloudPrintOAuthAuthority",)
	enterpriseCloudPrintOAuthClientIdentifier: Optional[str] = Field(default=None,alias="enterpriseCloudPrintOAuthClientIdentifier",)
	enterpriseCloudPrintResourceIdentifier: Optional[str] = Field(default=None,alias="enterpriseCloudPrintResourceIdentifier",)
	experienceBlockDeviceDiscovery: Optional[bool] = Field(default=None,alias="experienceBlockDeviceDiscovery",)
	experienceBlockErrorDialogWhenNoSIM: Optional[bool] = Field(default=None,alias="experienceBlockErrorDialogWhenNoSIM",)
	experienceBlockTaskSwitcher: Optional[bool] = Field(default=None,alias="experienceBlockTaskSwitcher",)
	gameDvrBlocked: Optional[bool] = Field(default=None,alias="gameDvrBlocked",)
	internetSharingBlocked: Optional[bool] = Field(default=None,alias="internetSharingBlocked",)
	locationServicesBlocked: Optional[bool] = Field(default=None,alias="locationServicesBlocked",)
	lockScreenAllowTimeoutConfiguration: Optional[bool] = Field(default=None,alias="lockScreenAllowTimeoutConfiguration",)
	lockScreenBlockActionCenterNotifications: Optional[bool] = Field(default=None,alias="lockScreenBlockActionCenterNotifications",)
	lockScreenBlockCortana: Optional[bool] = Field(default=None,alias="lockScreenBlockCortana",)
	lockScreenBlockToastNotifications: Optional[bool] = Field(default=None,alias="lockScreenBlockToastNotifications",)
	lockScreenTimeoutInSeconds: Optional[int] = Field(default=None,alias="lockScreenTimeoutInSeconds",)
	logonBlockFastUserSwitching: Optional[bool] = Field(default=None,alias="logonBlockFastUserSwitching",)
	microsoftAccountBlocked: Optional[bool] = Field(default=None,alias="microsoftAccountBlocked",)
	microsoftAccountBlockSettingsSync: Optional[bool] = Field(default=None,alias="microsoftAccountBlockSettingsSync",)
	networkProxyApplySettingsDeviceWide: Optional[bool] = Field(default=None,alias="networkProxyApplySettingsDeviceWide",)
	networkProxyAutomaticConfigurationUrl: Optional[str] = Field(default=None,alias="networkProxyAutomaticConfigurationUrl",)
	networkProxyDisableAutoDetect: Optional[bool] = Field(default=None,alias="networkProxyDisableAutoDetect",)
	networkProxyServer: Optional[Windows10NetworkProxyServer] = Field(default=None,alias="networkProxyServer",)
	nfcBlocked: Optional[bool] = Field(default=None,alias="nfcBlocked",)
	oneDriveDisableFileSync: Optional[bool] = Field(default=None,alias="oneDriveDisableFileSync",)
	passwordBlockSimple: Optional[bool] = Field(default=None,alias="passwordBlockSimple",)
	passwordExpirationDays: Optional[int] = Field(default=None,alias="passwordExpirationDays",)
	passwordMinimumCharacterSetCount: Optional[int] = Field(default=None,alias="passwordMinimumCharacterSetCount",)
	passwordMinimumLength: Optional[int] = Field(default=None,alias="passwordMinimumLength",)
	passwordMinutesOfInactivityBeforeScreenTimeout: Optional[int] = Field(default=None,alias="passwordMinutesOfInactivityBeforeScreenTimeout",)
	passwordPreviousPasswordBlockCount: Optional[int] = Field(default=None,alias="passwordPreviousPasswordBlockCount",)
	passwordRequired: Optional[bool] = Field(default=None,alias="passwordRequired",)
	passwordRequiredType: Optional[RequiredPasswordType] = Field(default=None,alias="passwordRequiredType",)
	passwordRequireWhenResumeFromIdleState: Optional[bool] = Field(default=None,alias="passwordRequireWhenResumeFromIdleState",)
	passwordSignInFailureCountBeforeFactoryReset: Optional[int] = Field(default=None,alias="passwordSignInFailureCountBeforeFactoryReset",)
	personalizationDesktopImageUrl: Optional[str] = Field(default=None,alias="personalizationDesktopImageUrl",)
	personalizationLockScreenImageUrl: Optional[str] = Field(default=None,alias="personalizationLockScreenImageUrl",)
	privacyAdvertisingId: Optional[StateManagementSetting] = Field(default=None,alias="privacyAdvertisingId",)
	privacyAutoAcceptPairingAndConsentPrompts: Optional[bool] = Field(default=None,alias="privacyAutoAcceptPairingAndConsentPrompts",)
	privacyBlockInputPersonalization: Optional[bool] = Field(default=None,alias="privacyBlockInputPersonalization",)
	resetProtectionModeBlocked: Optional[bool] = Field(default=None,alias="resetProtectionModeBlocked",)
	safeSearchFilter: Optional[SafeSearchFilterType] = Field(default=None,alias="safeSearchFilter",)
	screenCaptureBlocked: Optional[bool] = Field(default=None,alias="screenCaptureBlocked",)
	searchBlockDiacritics: Optional[bool] = Field(default=None,alias="searchBlockDiacritics",)
	searchDisableAutoLanguageDetection: Optional[bool] = Field(default=None,alias="searchDisableAutoLanguageDetection",)
	searchDisableIndexerBackoff: Optional[bool] = Field(default=None,alias="searchDisableIndexerBackoff",)
	searchDisableIndexingEncryptedItems: Optional[bool] = Field(default=None,alias="searchDisableIndexingEncryptedItems",)
	searchDisableIndexingRemovableDrive: Optional[bool] = Field(default=None,alias="searchDisableIndexingRemovableDrive",)
	searchEnableAutomaticIndexSizeManangement: Optional[bool] = Field(default=None,alias="searchEnableAutomaticIndexSizeManangement",)
	searchEnableRemoteQueries: Optional[bool] = Field(default=None,alias="searchEnableRemoteQueries",)
	settingsBlockAccountsPage: Optional[bool] = Field(default=None,alias="settingsBlockAccountsPage",)
	settingsBlockAddProvisioningPackage: Optional[bool] = Field(default=None,alias="settingsBlockAddProvisioningPackage",)
	settingsBlockAppsPage: Optional[bool] = Field(default=None,alias="settingsBlockAppsPage",)
	settingsBlockChangeLanguage: Optional[bool] = Field(default=None,alias="settingsBlockChangeLanguage",)
	settingsBlockChangePowerSleep: Optional[bool] = Field(default=None,alias="settingsBlockChangePowerSleep",)
	settingsBlockChangeRegion: Optional[bool] = Field(default=None,alias="settingsBlockChangeRegion",)
	settingsBlockChangeSystemTime: Optional[bool] = Field(default=None,alias="settingsBlockChangeSystemTime",)
	settingsBlockDevicesPage: Optional[bool] = Field(default=None,alias="settingsBlockDevicesPage",)
	settingsBlockEaseOfAccessPage: Optional[bool] = Field(default=None,alias="settingsBlockEaseOfAccessPage",)
	settingsBlockEditDeviceName: Optional[bool] = Field(default=None,alias="settingsBlockEditDeviceName",)
	settingsBlockGamingPage: Optional[bool] = Field(default=None,alias="settingsBlockGamingPage",)
	settingsBlockNetworkInternetPage: Optional[bool] = Field(default=None,alias="settingsBlockNetworkInternetPage",)
	settingsBlockPersonalizationPage: Optional[bool] = Field(default=None,alias="settingsBlockPersonalizationPage",)
	settingsBlockPrivacyPage: Optional[bool] = Field(default=None,alias="settingsBlockPrivacyPage",)
	settingsBlockRemoveProvisioningPackage: Optional[bool] = Field(default=None,alias="settingsBlockRemoveProvisioningPackage",)
	settingsBlockSettingsApp: Optional[bool] = Field(default=None,alias="settingsBlockSettingsApp",)
	settingsBlockSystemPage: Optional[bool] = Field(default=None,alias="settingsBlockSystemPage",)
	settingsBlockTimeLanguagePage: Optional[bool] = Field(default=None,alias="settingsBlockTimeLanguagePage",)
	settingsBlockUpdateSecurityPage: Optional[bool] = Field(default=None,alias="settingsBlockUpdateSecurityPage",)
	sharedUserAppDataAllowed: Optional[bool] = Field(default=None,alias="sharedUserAppDataAllowed",)
	smartScreenBlockPromptOverride: Optional[bool] = Field(default=None,alias="smartScreenBlockPromptOverride",)
	smartScreenBlockPromptOverrideForFiles: Optional[bool] = Field(default=None,alias="smartScreenBlockPromptOverrideForFiles",)
	smartScreenEnableAppInstallControl: Optional[bool] = Field(default=None,alias="smartScreenEnableAppInstallControl",)
	startBlockUnpinningAppsFromTaskbar: Optional[bool] = Field(default=None,alias="startBlockUnpinningAppsFromTaskbar",)
	startMenuAppListVisibility: Optional[WindowsStartMenuAppListVisibilityType] = Field(default=None,alias="startMenuAppListVisibility",)
	startMenuHideChangeAccountSettings: Optional[bool] = Field(default=None,alias="startMenuHideChangeAccountSettings",)
	startMenuHideFrequentlyUsedApps: Optional[bool] = Field(default=None,alias="startMenuHideFrequentlyUsedApps",)
	startMenuHideHibernate: Optional[bool] = Field(default=None,alias="startMenuHideHibernate",)
	startMenuHideLock: Optional[bool] = Field(default=None,alias="startMenuHideLock",)
	startMenuHidePowerButton: Optional[bool] = Field(default=None,alias="startMenuHidePowerButton",)
	startMenuHideRecentJumpLists: Optional[bool] = Field(default=None,alias="startMenuHideRecentJumpLists",)
	startMenuHideRecentlyAddedApps: Optional[bool] = Field(default=None,alias="startMenuHideRecentlyAddedApps",)
	startMenuHideRestartOptions: Optional[bool] = Field(default=None,alias="startMenuHideRestartOptions",)
	startMenuHideShutDown: Optional[bool] = Field(default=None,alias="startMenuHideShutDown",)
	startMenuHideSignOut: Optional[bool] = Field(default=None,alias="startMenuHideSignOut",)
	startMenuHideSleep: Optional[bool] = Field(default=None,alias="startMenuHideSleep",)
	startMenuHideSwitchAccount: Optional[bool] = Field(default=None,alias="startMenuHideSwitchAccount",)
	startMenuHideUserTile: Optional[bool] = Field(default=None,alias="startMenuHideUserTile",)
	startMenuLayoutEdgeAssetsXml: Optional[str] = Field(default=None,alias="startMenuLayoutEdgeAssetsXml",)
	startMenuLayoutXml: Optional[str] = Field(default=None,alias="startMenuLayoutXml",)
	startMenuMode: Optional[WindowsStartMenuModeType] = Field(default=None,alias="startMenuMode",)
	startMenuPinnedFolderDocuments: Optional[VisibilitySetting] = Field(default=None,alias="startMenuPinnedFolderDocuments",)
	startMenuPinnedFolderDownloads: Optional[VisibilitySetting] = Field(default=None,alias="startMenuPinnedFolderDownloads",)
	startMenuPinnedFolderFileExplorer: Optional[VisibilitySetting] = Field(default=None,alias="startMenuPinnedFolderFileExplorer",)
	startMenuPinnedFolderHomeGroup: Optional[VisibilitySetting] = Field(default=None,alias="startMenuPinnedFolderHomeGroup",)
	startMenuPinnedFolderMusic: Optional[VisibilitySetting] = Field(default=None,alias="startMenuPinnedFolderMusic",)
	startMenuPinnedFolderNetwork: Optional[VisibilitySetting] = Field(default=None,alias="startMenuPinnedFolderNetwork",)
	startMenuPinnedFolderPersonalFolder: Optional[VisibilitySetting] = Field(default=None,alias="startMenuPinnedFolderPersonalFolder",)
	startMenuPinnedFolderPictures: Optional[VisibilitySetting] = Field(default=None,alias="startMenuPinnedFolderPictures",)
	startMenuPinnedFolderSettings: Optional[VisibilitySetting] = Field(default=None,alias="startMenuPinnedFolderSettings",)
	startMenuPinnedFolderVideos: Optional[VisibilitySetting] = Field(default=None,alias="startMenuPinnedFolderVideos",)
	storageBlockRemovableStorage: Optional[bool] = Field(default=None,alias="storageBlockRemovableStorage",)
	storageRequireMobileDeviceEncryption: Optional[bool] = Field(default=None,alias="storageRequireMobileDeviceEncryption",)
	storageRestrictAppDataToSystemVolume: Optional[bool] = Field(default=None,alias="storageRestrictAppDataToSystemVolume",)
	storageRestrictAppInstallToSystemVolume: Optional[bool] = Field(default=None,alias="storageRestrictAppInstallToSystemVolume",)
	tenantLockdownRequireNetworkDuringOutOfBoxExperience: Optional[bool] = Field(default=None,alias="tenantLockdownRequireNetworkDuringOutOfBoxExperience",)
	usbBlocked: Optional[bool] = Field(default=None,alias="usbBlocked",)
	voiceRecordingBlocked: Optional[bool] = Field(default=None,alias="voiceRecordingBlocked",)
	webRtcBlockLocalhostIpAddress: Optional[bool] = Field(default=None,alias="webRtcBlockLocalhostIpAddress",)
	wiFiBlockAutomaticConnectHotspots: Optional[bool] = Field(default=None,alias="wiFiBlockAutomaticConnectHotspots",)
	wiFiBlocked: Optional[bool] = Field(default=None,alias="wiFiBlocked",)
	wiFiBlockManualConfiguration: Optional[bool] = Field(default=None,alias="wiFiBlockManualConfiguration",)
	wiFiScanInterval: Optional[int] = Field(default=None,alias="wiFiScanInterval",)
	windowsSpotlightBlockConsumerSpecificFeatures: Optional[bool] = Field(default=None,alias="windowsSpotlightBlockConsumerSpecificFeatures",)
	windowsSpotlightBlocked: Optional[bool] = Field(default=None,alias="windowsSpotlightBlocked",)
	windowsSpotlightBlockOnActionCenter: Optional[bool] = Field(default=None,alias="windowsSpotlightBlockOnActionCenter",)
	windowsSpotlightBlockTailoredExperiences: Optional[bool] = Field(default=None,alias="windowsSpotlightBlockTailoredExperiences",)
	windowsSpotlightBlockThirdPartyNotifications: Optional[bool] = Field(default=None,alias="windowsSpotlightBlockThirdPartyNotifications",)
	windowsSpotlightBlockWelcomeExperience: Optional[bool] = Field(default=None,alias="windowsSpotlightBlockWelcomeExperience",)
	windowsSpotlightBlockWindowsTips: Optional[bool] = Field(default=None,alias="windowsSpotlightBlockWindowsTips",)
	windowsSpotlightConfigureOnLockScreen: Optional[WindowsSpotlightEnablementSettings] = Field(default=None,alias="windowsSpotlightConfigureOnLockScreen",)
	windowsStoreBlockAutoUpdate: Optional[bool] = Field(default=None,alias="windowsStoreBlockAutoUpdate",)
	windowsStoreBlocked: Optional[bool] = Field(default=None,alias="windowsStoreBlocked",)
	windowsStoreEnablePrivateStoreOnly: Optional[bool] = Field(default=None,alias="windowsStoreEnablePrivateStoreOnly",)
	wirelessDisplayBlockProjectionToThisDevice: Optional[bool] = Field(default=None,alias="wirelessDisplayBlockProjectionToThisDevice",)
	wirelessDisplayBlockUserInputFromReceiver: Optional[bool] = Field(default=None,alias="wirelessDisplayBlockUserInputFromReceiver",)
	wirelessDisplayRequirePinForPairing: Optional[bool] = Field(default=None,alias="wirelessDisplayRequirePinForPairing",)

from .device_configuration_assignment import DeviceConfigurationAssignment
from .setting_state_device_summary import SettingStateDeviceSummary
from .device_configuration_device_status import DeviceConfigurationDeviceStatus
from .device_configuration_device_overview import DeviceConfigurationDeviceOverview
from .device_configuration_user_status import DeviceConfigurationUserStatus
from .device_configuration_user_overview import DeviceConfigurationUserOverview
from .state_management_setting import StateManagementSetting
from .defender_cloud_block_level_type import DefenderCloudBlockLevelType
from .defender_detected_malware_actions import DefenderDetectedMalwareActions
from .defender_monitor_file_activity import DefenderMonitorFileActivity
from .defender_prompt_for_sample_submission import DefenderPromptForSampleSubmission
from .defender_scan_type import DefenderScanType
from .weekly_schedule import WeeklySchedule
from .state_management_setting import StateManagementSetting
from .diagnostic_data_submission_mode import DiagnosticDataSubmissionMode
from .edge_cookie_policy import EdgeCookiePolicy
from .edge_search_engine_base import EdgeSearchEngineBase
from .windows10_network_proxy_server import Windows10NetworkProxyServer
from .required_password_type import RequiredPasswordType
from .state_management_setting import StateManagementSetting
from .safe_search_filter_type import SafeSearchFilterType
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
from .windows_spotlight_enablement_settings import WindowsSpotlightEnablementSettings

