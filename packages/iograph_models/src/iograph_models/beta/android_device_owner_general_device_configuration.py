from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class AndroidDeviceOwnerGeneralDeviceConfiguration(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.androidDeviceOwnerGeneralDeviceConfiguration"] = Field(alias="@odata.type", default="#microsoft.graph.androidDeviceOwnerGeneralDeviceConfiguration")
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
	accountsBlockModification: Optional[bool] = Field(alias="accountsBlockModification", default=None,)
	androidDeviceOwnerDelegatedScopeAppSettings: Optional[list[AndroidDeviceOwnerDelegatedScopeAppSetting]] = Field(alias="androidDeviceOwnerDelegatedScopeAppSettings", default=None,)
	appsAllowInstallFromUnknownSources: Optional[bool] = Field(alias="appsAllowInstallFromUnknownSources", default=None,)
	appsAutoUpdatePolicy: Optional[AndroidDeviceOwnerAppAutoUpdatePolicyType | str] = Field(alias="appsAutoUpdatePolicy", default=None,)
	appsDefaultPermissionPolicy: Optional[AndroidDeviceOwnerDefaultAppPermissionPolicyType | str] = Field(alias="appsDefaultPermissionPolicy", default=None,)
	appsRecommendSkippingFirstUseHints: Optional[bool] = Field(alias="appsRecommendSkippingFirstUseHints", default=None,)
	azureAdSharedDeviceDataClearApps: Optional[list[Annotated[Union[AppleAppListItem],Field(discriminator="odata_type")]]] = Field(alias="azureAdSharedDeviceDataClearApps", default=None,)
	bluetoothBlockConfiguration: Optional[bool] = Field(alias="bluetoothBlockConfiguration", default=None,)
	bluetoothBlockContactSharing: Optional[bool] = Field(alias="bluetoothBlockContactSharing", default=None,)
	cameraBlocked: Optional[bool] = Field(alias="cameraBlocked", default=None,)
	cellularBlockWiFiTethering: Optional[bool] = Field(alias="cellularBlockWiFiTethering", default=None,)
	certificateCredentialConfigurationDisabled: Optional[bool] = Field(alias="certificateCredentialConfigurationDisabled", default=None,)
	crossProfilePoliciesAllowCopyPaste: Optional[bool] = Field(alias="crossProfilePoliciesAllowCopyPaste", default=None,)
	crossProfilePoliciesAllowDataSharing: Optional[AndroidDeviceOwnerCrossProfileDataSharing | str] = Field(alias="crossProfilePoliciesAllowDataSharing", default=None,)
	crossProfilePoliciesShowWorkContactsInPersonalProfile: Optional[bool] = Field(alias="crossProfilePoliciesShowWorkContactsInPersonalProfile", default=None,)
	dataRoamingBlocked: Optional[bool] = Field(alias="dataRoamingBlocked", default=None,)
	dateTimeConfigurationBlocked: Optional[bool] = Field(alias="dateTimeConfigurationBlocked", default=None,)
	detailedHelpText: Optional[AndroidDeviceOwnerUserFacingMessage] = Field(alias="detailedHelpText", default=None,)
	deviceLocationMode: Optional[AndroidDeviceOwnerLocationMode | str] = Field(alias="deviceLocationMode", default=None,)
	deviceOwnerLockScreenMessage: Optional[AndroidDeviceOwnerUserFacingMessage] = Field(alias="deviceOwnerLockScreenMessage", default=None,)
	enrollmentProfile: Optional[AndroidDeviceOwnerEnrollmentProfileType | str] = Field(alias="enrollmentProfile", default=None,)
	factoryResetBlocked: Optional[bool] = Field(alias="factoryResetBlocked", default=None,)
	factoryResetDeviceAdministratorEmails: Optional[list[str]] = Field(alias="factoryResetDeviceAdministratorEmails", default=None,)
	globalProxy: Optional[Union[AndroidDeviceOwnerGlobalProxyAutoConfig, AndroidDeviceOwnerGlobalProxyDirect]] = Field(alias="globalProxy", default=None,discriminator="odata_type", )
	googleAccountsBlocked: Optional[bool] = Field(alias="googleAccountsBlocked", default=None,)
	kioskCustomizationDeviceSettingsBlocked: Optional[bool] = Field(alias="kioskCustomizationDeviceSettingsBlocked", default=None,)
	kioskCustomizationPowerButtonActionsBlocked: Optional[bool] = Field(alias="kioskCustomizationPowerButtonActionsBlocked", default=None,)
	kioskCustomizationStatusBar: Optional[AndroidDeviceOwnerKioskCustomizationStatusBar | str] = Field(alias="kioskCustomizationStatusBar", default=None,)
	kioskCustomizationSystemErrorWarnings: Optional[bool] = Field(alias="kioskCustomizationSystemErrorWarnings", default=None,)
	kioskCustomizationSystemNavigation: Optional[AndroidDeviceOwnerKioskCustomizationSystemNavigation | str] = Field(alias="kioskCustomizationSystemNavigation", default=None,)
	kioskModeAppOrderEnabled: Optional[bool] = Field(alias="kioskModeAppOrderEnabled", default=None,)
	kioskModeAppPositions: Optional[list[AndroidDeviceOwnerKioskModeAppPositionItem]] = Field(alias="kioskModeAppPositions", default=None,)
	kioskModeApps: Optional[list[Annotated[Union[AppleAppListItem],Field(discriminator="odata_type")]]] = Field(alias="kioskModeApps", default=None,)
	kioskModeAppsInFolderOrderedByName: Optional[bool] = Field(alias="kioskModeAppsInFolderOrderedByName", default=None,)
	kioskModeBluetoothConfigurationEnabled: Optional[bool] = Field(alias="kioskModeBluetoothConfigurationEnabled", default=None,)
	kioskModeDebugMenuEasyAccessEnabled: Optional[bool] = Field(alias="kioskModeDebugMenuEasyAccessEnabled", default=None,)
	kioskModeExitCode: Optional[str] = Field(alias="kioskModeExitCode", default=None,)
	kioskModeFlashlightConfigurationEnabled: Optional[bool] = Field(alias="kioskModeFlashlightConfigurationEnabled", default=None,)
	kioskModeFolderIcon: Optional[AndroidDeviceOwnerKioskModeFolderIcon | str] = Field(alias="kioskModeFolderIcon", default=None,)
	kioskModeGridHeight: Optional[int] = Field(alias="kioskModeGridHeight", default=None,)
	kioskModeGridWidth: Optional[int] = Field(alias="kioskModeGridWidth", default=None,)
	kioskModeIconSize: Optional[AndroidDeviceOwnerKioskModeIconSize | str] = Field(alias="kioskModeIconSize", default=None,)
	kioskModeLockHomeScreen: Optional[bool] = Field(alias="kioskModeLockHomeScreen", default=None,)
	kioskModeManagedFolders: Optional[list[AndroidDeviceOwnerKioskModeManagedFolder]] = Field(alias="kioskModeManagedFolders", default=None,)
	kioskModeManagedHomeScreenAutoSignout: Optional[bool] = Field(alias="kioskModeManagedHomeScreenAutoSignout", default=None,)
	kioskModeManagedHomeScreenInactiveSignOutDelayInSeconds: Optional[int] = Field(alias="kioskModeManagedHomeScreenInactiveSignOutDelayInSeconds", default=None,)
	kioskModeManagedHomeScreenInactiveSignOutNoticeInSeconds: Optional[int] = Field(alias="kioskModeManagedHomeScreenInactiveSignOutNoticeInSeconds", default=None,)
	kioskModeManagedHomeScreenPinComplexity: Optional[KioskModeManagedHomeScreenPinComplexity | str] = Field(alias="kioskModeManagedHomeScreenPinComplexity", default=None,)
	kioskModeManagedHomeScreenPinRequired: Optional[bool] = Field(alias="kioskModeManagedHomeScreenPinRequired", default=None,)
	kioskModeManagedHomeScreenPinRequiredToResume: Optional[bool] = Field(alias="kioskModeManagedHomeScreenPinRequiredToResume", default=None,)
	kioskModeManagedHomeScreenSignInBackground: Optional[str] = Field(alias="kioskModeManagedHomeScreenSignInBackground", default=None,)
	kioskModeManagedHomeScreenSignInBrandingLogo: Optional[str] = Field(alias="kioskModeManagedHomeScreenSignInBrandingLogo", default=None,)
	kioskModeManagedHomeScreenSignInEnabled: Optional[bool] = Field(alias="kioskModeManagedHomeScreenSignInEnabled", default=None,)
	kioskModeManagedSettingsEntryDisabled: Optional[bool] = Field(alias="kioskModeManagedSettingsEntryDisabled", default=None,)
	kioskModeMediaVolumeConfigurationEnabled: Optional[bool] = Field(alias="kioskModeMediaVolumeConfigurationEnabled", default=None,)
	kioskModeScreenOrientation: Optional[AndroidDeviceOwnerKioskModeScreenOrientation | str] = Field(alias="kioskModeScreenOrientation", default=None,)
	kioskModeScreenSaverConfigurationEnabled: Optional[bool] = Field(alias="kioskModeScreenSaverConfigurationEnabled", default=None,)
	kioskModeScreenSaverDetectMediaDisabled: Optional[bool] = Field(alias="kioskModeScreenSaverDetectMediaDisabled", default=None,)
	kioskModeScreenSaverDisplayTimeInSeconds: Optional[int] = Field(alias="kioskModeScreenSaverDisplayTimeInSeconds", default=None,)
	kioskModeScreenSaverImageUrl: Optional[str] = Field(alias="kioskModeScreenSaverImageUrl", default=None,)
	kioskModeScreenSaverStartDelayInSeconds: Optional[int] = Field(alias="kioskModeScreenSaverStartDelayInSeconds", default=None,)
	kioskModeShowAppNotificationBadge: Optional[bool] = Field(alias="kioskModeShowAppNotificationBadge", default=None,)
	kioskModeShowDeviceInfo: Optional[bool] = Field(alias="kioskModeShowDeviceInfo", default=None,)
	kioskModeUseManagedHomeScreenApp: Optional[KioskModeType | str] = Field(alias="kioskModeUseManagedHomeScreenApp", default=None,)
	kioskModeVirtualHomeButtonEnabled: Optional[bool] = Field(alias="kioskModeVirtualHomeButtonEnabled", default=None,)
	kioskModeVirtualHomeButtonType: Optional[AndroidDeviceOwnerVirtualHomeButtonType | str] = Field(alias="kioskModeVirtualHomeButtonType", default=None,)
	kioskModeWallpaperUrl: Optional[str] = Field(alias="kioskModeWallpaperUrl", default=None,)
	kioskModeWifiAllowedSsids: Optional[list[str]] = Field(alias="kioskModeWifiAllowedSsids", default=None,)
	kioskModeWiFiConfigurationEnabled: Optional[bool] = Field(alias="kioskModeWiFiConfigurationEnabled", default=None,)
	locateDeviceLostModeEnabled: Optional[bool] = Field(alias="locateDeviceLostModeEnabled", default=None,)
	locateDeviceUserlessDisabled: Optional[bool] = Field(alias="locateDeviceUserlessDisabled", default=None,)
	microphoneForceMute: Optional[bool] = Field(alias="microphoneForceMute", default=None,)
	microsoftLauncherConfigurationEnabled: Optional[bool] = Field(alias="microsoftLauncherConfigurationEnabled", default=None,)
	microsoftLauncherCustomWallpaperAllowUserModification: Optional[bool] = Field(alias="microsoftLauncherCustomWallpaperAllowUserModification", default=None,)
	microsoftLauncherCustomWallpaperEnabled: Optional[bool] = Field(alias="microsoftLauncherCustomWallpaperEnabled", default=None,)
	microsoftLauncherCustomWallpaperImageUrl: Optional[str] = Field(alias="microsoftLauncherCustomWallpaperImageUrl", default=None,)
	microsoftLauncherDockPresenceAllowUserModification: Optional[bool] = Field(alias="microsoftLauncherDockPresenceAllowUserModification", default=None,)
	microsoftLauncherDockPresenceConfiguration: Optional[MicrosoftLauncherDockPresence | str] = Field(alias="microsoftLauncherDockPresenceConfiguration", default=None,)
	microsoftLauncherFeedAllowUserModification: Optional[bool] = Field(alias="microsoftLauncherFeedAllowUserModification", default=None,)
	microsoftLauncherFeedEnabled: Optional[bool] = Field(alias="microsoftLauncherFeedEnabled", default=None,)
	microsoftLauncherSearchBarPlacementConfiguration: Optional[MicrosoftLauncherSearchBarPlacement | str] = Field(alias="microsoftLauncherSearchBarPlacementConfiguration", default=None,)
	networkEscapeHatchAllowed: Optional[bool] = Field(alias="networkEscapeHatchAllowed", default=None,)
	nfcBlockOutgoingBeam: Optional[bool] = Field(alias="nfcBlockOutgoingBeam", default=None,)
	passwordBlockKeyguard: Optional[bool] = Field(alias="passwordBlockKeyguard", default=None,)
	passwordBlockKeyguardFeatures: Optional[list[AndroidKeyguardFeature | str]] = Field(alias="passwordBlockKeyguardFeatures", default=None,)
	passwordExpirationDays: Optional[int] = Field(alias="passwordExpirationDays", default=None,)
	passwordMinimumLength: Optional[int] = Field(alias="passwordMinimumLength", default=None,)
	passwordMinimumLetterCharacters: Optional[int] = Field(alias="passwordMinimumLetterCharacters", default=None,)
	passwordMinimumLowerCaseCharacters: Optional[int] = Field(alias="passwordMinimumLowerCaseCharacters", default=None,)
	passwordMinimumNonLetterCharacters: Optional[int] = Field(alias="passwordMinimumNonLetterCharacters", default=None,)
	passwordMinimumNumericCharacters: Optional[int] = Field(alias="passwordMinimumNumericCharacters", default=None,)
	passwordMinimumSymbolCharacters: Optional[int] = Field(alias="passwordMinimumSymbolCharacters", default=None,)
	passwordMinimumUpperCaseCharacters: Optional[int] = Field(alias="passwordMinimumUpperCaseCharacters", default=None,)
	passwordMinutesOfInactivityBeforeScreenTimeout: Optional[int] = Field(alias="passwordMinutesOfInactivityBeforeScreenTimeout", default=None,)
	passwordPreviousPasswordCountToBlock: Optional[int] = Field(alias="passwordPreviousPasswordCountToBlock", default=None,)
	passwordRequiredType: Optional[AndroidDeviceOwnerRequiredPasswordType | str] = Field(alias="passwordRequiredType", default=None,)
	passwordRequireUnlock: Optional[AndroidDeviceOwnerRequiredPasswordUnlock | str] = Field(alias="passwordRequireUnlock", default=None,)
	passwordSignInFailureCountBeforeFactoryReset: Optional[int] = Field(alias="passwordSignInFailureCountBeforeFactoryReset", default=None,)
	personalProfileAppsAllowInstallFromUnknownSources: Optional[bool] = Field(alias="personalProfileAppsAllowInstallFromUnknownSources", default=None,)
	personalProfileCameraBlocked: Optional[bool] = Field(alias="personalProfileCameraBlocked", default=None,)
	personalProfilePersonalApplications: Optional[list[Annotated[Union[AppleAppListItem],Field(discriminator="odata_type")]]] = Field(alias="personalProfilePersonalApplications", default=None,)
	personalProfilePlayStoreMode: Optional[PersonalProfilePersonalPlayStoreMode | str] = Field(alias="personalProfilePlayStoreMode", default=None,)
	personalProfileScreenCaptureBlocked: Optional[bool] = Field(alias="personalProfileScreenCaptureBlocked", default=None,)
	playStoreMode: Optional[AndroidDeviceOwnerPlayStoreMode | str] = Field(alias="playStoreMode", default=None,)
	screenCaptureBlocked: Optional[bool] = Field(alias="screenCaptureBlocked", default=None,)
	securityCommonCriteriaModeEnabled: Optional[bool] = Field(alias="securityCommonCriteriaModeEnabled", default=None,)
	securityDeveloperSettingsEnabled: Optional[bool] = Field(alias="securityDeveloperSettingsEnabled", default=None,)
	securityRequireVerifyApps: Optional[bool] = Field(alias="securityRequireVerifyApps", default=None,)
	shareDeviceLocationDisabled: Optional[bool] = Field(alias="shareDeviceLocationDisabled", default=None,)
	shortHelpText: Optional[AndroidDeviceOwnerUserFacingMessage] = Field(alias="shortHelpText", default=None,)
	statusBarBlocked: Optional[bool] = Field(alias="statusBarBlocked", default=None,)
	stayOnModes: Optional[list[AndroidDeviceOwnerBatteryPluggedMode | str]] = Field(alias="stayOnModes", default=None,)
	storageAllowUsb: Optional[bool] = Field(alias="storageAllowUsb", default=None,)
	storageBlockExternalMedia: Optional[bool] = Field(alias="storageBlockExternalMedia", default=None,)
	storageBlockUsbFileTransfer: Optional[bool] = Field(alias="storageBlockUsbFileTransfer", default=None,)
	systemUpdateFreezePeriods: Optional[list[AndroidDeviceOwnerSystemUpdateFreezePeriod]] = Field(alias="systemUpdateFreezePeriods", default=None,)
	systemUpdateInstallType: Optional[AndroidDeviceOwnerSystemUpdateInstallType | str] = Field(alias="systemUpdateInstallType", default=None,)
	systemUpdateWindowEndMinutesAfterMidnight: Optional[int] = Field(alias="systemUpdateWindowEndMinutesAfterMidnight", default=None,)
	systemUpdateWindowStartMinutesAfterMidnight: Optional[int] = Field(alias="systemUpdateWindowStartMinutesAfterMidnight", default=None,)
	systemWindowsBlocked: Optional[bool] = Field(alias="systemWindowsBlocked", default=None,)
	usersBlockAdd: Optional[bool] = Field(alias="usersBlockAdd", default=None,)
	usersBlockRemove: Optional[bool] = Field(alias="usersBlockRemove", default=None,)
	volumeBlockAdjustment: Optional[bool] = Field(alias="volumeBlockAdjustment", default=None,)
	vpnAlwaysOnLockdownMode: Optional[bool] = Field(alias="vpnAlwaysOnLockdownMode", default=None,)
	vpnAlwaysOnPackageIdentifier: Optional[str] = Field(alias="vpnAlwaysOnPackageIdentifier", default=None,)
	wifiBlockEditConfigurations: Optional[bool] = Field(alias="wifiBlockEditConfigurations", default=None,)
	wifiBlockEditPolicyDefinedConfigurations: Optional[bool] = Field(alias="wifiBlockEditPolicyDefinedConfigurations", default=None,)
	workProfilePasswordExpirationDays: Optional[int] = Field(alias="workProfilePasswordExpirationDays", default=None,)
	workProfilePasswordMinimumLength: Optional[int] = Field(alias="workProfilePasswordMinimumLength", default=None,)
	workProfilePasswordMinimumLetterCharacters: Optional[int] = Field(alias="workProfilePasswordMinimumLetterCharacters", default=None,)
	workProfilePasswordMinimumLowerCaseCharacters: Optional[int] = Field(alias="workProfilePasswordMinimumLowerCaseCharacters", default=None,)
	workProfilePasswordMinimumNonLetterCharacters: Optional[int] = Field(alias="workProfilePasswordMinimumNonLetterCharacters", default=None,)
	workProfilePasswordMinimumNumericCharacters: Optional[int] = Field(alias="workProfilePasswordMinimumNumericCharacters", default=None,)
	workProfilePasswordMinimumSymbolCharacters: Optional[int] = Field(alias="workProfilePasswordMinimumSymbolCharacters", default=None,)
	workProfilePasswordMinimumUpperCaseCharacters: Optional[int] = Field(alias="workProfilePasswordMinimumUpperCaseCharacters", default=None,)
	workProfilePasswordPreviousPasswordCountToBlock: Optional[int] = Field(alias="workProfilePasswordPreviousPasswordCountToBlock", default=None,)
	workProfilePasswordRequiredType: Optional[AndroidDeviceOwnerRequiredPasswordType | str] = Field(alias="workProfilePasswordRequiredType", default=None,)
	workProfilePasswordRequireUnlock: Optional[AndroidDeviceOwnerRequiredPasswordUnlock | str] = Field(alias="workProfilePasswordRequireUnlock", default=None,)
	workProfilePasswordSignInFailureCountBeforeFactoryReset: Optional[int] = Field(alias="workProfilePasswordSignInFailureCountBeforeFactoryReset", default=None,)

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
from .android_device_owner_delegated_scope_app_setting import AndroidDeviceOwnerDelegatedScopeAppSetting
from .android_device_owner_app_auto_update_policy_type import AndroidDeviceOwnerAppAutoUpdatePolicyType
from .android_device_owner_default_app_permission_policy_type import AndroidDeviceOwnerDefaultAppPermissionPolicyType
from .apple_app_list_item import AppleAppListItem
from .android_device_owner_cross_profile_data_sharing import AndroidDeviceOwnerCrossProfileDataSharing
from .android_device_owner_user_facing_message import AndroidDeviceOwnerUserFacingMessage
from .android_device_owner_location_mode import AndroidDeviceOwnerLocationMode
from .android_device_owner_user_facing_message import AndroidDeviceOwnerUserFacingMessage
from .android_device_owner_enrollment_profile_type import AndroidDeviceOwnerEnrollmentProfileType
from .android_device_owner_global_proxy_auto_config import AndroidDeviceOwnerGlobalProxyAutoConfig
from .android_device_owner_global_proxy_direct import AndroidDeviceOwnerGlobalProxyDirect
from .android_device_owner_kiosk_customization_status_bar import AndroidDeviceOwnerKioskCustomizationStatusBar
from .android_device_owner_kiosk_customization_system_navigation import AndroidDeviceOwnerKioskCustomizationSystemNavigation
from .android_device_owner_kiosk_mode_app_position_item import AndroidDeviceOwnerKioskModeAppPositionItem
from .apple_app_list_item import AppleAppListItem
from .android_device_owner_kiosk_mode_folder_icon import AndroidDeviceOwnerKioskModeFolderIcon
from .android_device_owner_kiosk_mode_icon_size import AndroidDeviceOwnerKioskModeIconSize
from .android_device_owner_kiosk_mode_managed_folder import AndroidDeviceOwnerKioskModeManagedFolder
from .kiosk_mode_managed_home_screen_pin_complexity import KioskModeManagedHomeScreenPinComplexity
from .android_device_owner_kiosk_mode_screen_orientation import AndroidDeviceOwnerKioskModeScreenOrientation
from .kiosk_mode_type import KioskModeType
from .android_device_owner_virtual_home_button_type import AndroidDeviceOwnerVirtualHomeButtonType
from .microsoft_launcher_dock_presence import MicrosoftLauncherDockPresence
from .microsoft_launcher_search_bar_placement import MicrosoftLauncherSearchBarPlacement
from .android_keyguard_feature import AndroidKeyguardFeature
from .android_device_owner_required_password_type import AndroidDeviceOwnerRequiredPasswordType
from .android_device_owner_required_password_unlock import AndroidDeviceOwnerRequiredPasswordUnlock
from .apple_app_list_item import AppleAppListItem
from .personal_profile_personal_play_store_mode import PersonalProfilePersonalPlayStoreMode
from .android_device_owner_play_store_mode import AndroidDeviceOwnerPlayStoreMode
from .android_device_owner_user_facing_message import AndroidDeviceOwnerUserFacingMessage
from .android_device_owner_battery_plugged_mode import AndroidDeviceOwnerBatteryPluggedMode
from .android_device_owner_system_update_freeze_period import AndroidDeviceOwnerSystemUpdateFreezePeriod
from .android_device_owner_system_update_install_type import AndroidDeviceOwnerSystemUpdateInstallType
from .android_device_owner_required_password_type import AndroidDeviceOwnerRequiredPasswordType
from .android_device_owner_required_password_unlock import AndroidDeviceOwnerRequiredPasswordUnlock

