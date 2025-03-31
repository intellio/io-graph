from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class AndroidGeneralDeviceConfiguration(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.androidGeneralDeviceConfiguration"] = Field(alias="@odata.type", default="#microsoft.graph.androidGeneralDeviceConfiguration")
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	version: Optional[int] = Field(alias="version", default=None,)
	assignments: Optional[list[DeviceConfigurationAssignment]] = Field(alias="assignments", default=None,)
	deviceSettingStateSummaries: Optional[list[SettingStateDeviceSummary]] = Field(alias="deviceSettingStateSummaries", default=None,)
	deviceStatuses: Optional[list[DeviceConfigurationDeviceStatus]] = Field(alias="deviceStatuses", default=None,)
	deviceStatusOverview: Optional[DeviceConfigurationDeviceOverview] = Field(alias="deviceStatusOverview", default=None,)
	userStatuses: Optional[list[DeviceConfigurationUserStatus]] = Field(alias="userStatuses", default=None,)
	userStatusOverview: Optional[DeviceConfigurationUserOverview] = Field(alias="userStatusOverview", default=None,)
	appsBlockClipboardSharing: Optional[bool] = Field(alias="appsBlockClipboardSharing", default=None,)
	appsBlockCopyPaste: Optional[bool] = Field(alias="appsBlockCopyPaste", default=None,)
	appsBlockYouTube: Optional[bool] = Field(alias="appsBlockYouTube", default=None,)
	appsHideList: Optional[list[AppListItem]] = Field(alias="appsHideList", default=None,)
	appsInstallAllowList: Optional[list[AppListItem]] = Field(alias="appsInstallAllowList", default=None,)
	appsLaunchBlockList: Optional[list[AppListItem]] = Field(alias="appsLaunchBlockList", default=None,)
	bluetoothBlocked: Optional[bool] = Field(alias="bluetoothBlocked", default=None,)
	cameraBlocked: Optional[bool] = Field(alias="cameraBlocked", default=None,)
	cellularBlockDataRoaming: Optional[bool] = Field(alias="cellularBlockDataRoaming", default=None,)
	cellularBlockMessaging: Optional[bool] = Field(alias="cellularBlockMessaging", default=None,)
	cellularBlockVoiceRoaming: Optional[bool] = Field(alias="cellularBlockVoiceRoaming", default=None,)
	cellularBlockWiFiTethering: Optional[bool] = Field(alias="cellularBlockWiFiTethering", default=None,)
	compliantAppListType: Optional[AppListType | str] = Field(alias="compliantAppListType", default=None,)
	compliantAppsList: Optional[list[AppListItem]] = Field(alias="compliantAppsList", default=None,)
	deviceSharingAllowed: Optional[bool] = Field(alias="deviceSharingAllowed", default=None,)
	diagnosticDataBlockSubmission: Optional[bool] = Field(alias="diagnosticDataBlockSubmission", default=None,)
	factoryResetBlocked: Optional[bool] = Field(alias="factoryResetBlocked", default=None,)
	googleAccountBlockAutoSync: Optional[bool] = Field(alias="googleAccountBlockAutoSync", default=None,)
	googlePlayStoreBlocked: Optional[bool] = Field(alias="googlePlayStoreBlocked", default=None,)
	kioskModeApps: Optional[list[AppListItem]] = Field(alias="kioskModeApps", default=None,)
	kioskModeBlockSleepButton: Optional[bool] = Field(alias="kioskModeBlockSleepButton", default=None,)
	kioskModeBlockVolumeButtons: Optional[bool] = Field(alias="kioskModeBlockVolumeButtons", default=None,)
	locationServicesBlocked: Optional[bool] = Field(alias="locationServicesBlocked", default=None,)
	nfcBlocked: Optional[bool] = Field(alias="nfcBlocked", default=None,)
	passwordBlockFingerprintUnlock: Optional[bool] = Field(alias="passwordBlockFingerprintUnlock", default=None,)
	passwordBlockTrustAgents: Optional[bool] = Field(alias="passwordBlockTrustAgents", default=None,)
	passwordExpirationDays: Optional[int] = Field(alias="passwordExpirationDays", default=None,)
	passwordMinimumLength: Optional[int] = Field(alias="passwordMinimumLength", default=None,)
	passwordMinutesOfInactivityBeforeScreenTimeout: Optional[int] = Field(alias="passwordMinutesOfInactivityBeforeScreenTimeout", default=None,)
	passwordPreviousPasswordBlockCount: Optional[int] = Field(alias="passwordPreviousPasswordBlockCount", default=None,)
	passwordRequired: Optional[bool] = Field(alias="passwordRequired", default=None,)
	passwordRequiredType: Optional[AndroidRequiredPasswordType | str] = Field(alias="passwordRequiredType", default=None,)
	passwordSignInFailureCountBeforeFactoryReset: Optional[int] = Field(alias="passwordSignInFailureCountBeforeFactoryReset", default=None,)
	powerOffBlocked: Optional[bool] = Field(alias="powerOffBlocked", default=None,)
	screenCaptureBlocked: Optional[bool] = Field(alias="screenCaptureBlocked", default=None,)
	securityRequireVerifyApps: Optional[bool] = Field(alias="securityRequireVerifyApps", default=None,)
	storageBlockGoogleBackup: Optional[bool] = Field(alias="storageBlockGoogleBackup", default=None,)
	storageBlockRemovableStorage: Optional[bool] = Field(alias="storageBlockRemovableStorage", default=None,)
	storageRequireDeviceEncryption: Optional[bool] = Field(alias="storageRequireDeviceEncryption", default=None,)
	storageRequireRemovableStorageEncryption: Optional[bool] = Field(alias="storageRequireRemovableStorageEncryption", default=None,)
	voiceAssistantBlocked: Optional[bool] = Field(alias="voiceAssistantBlocked", default=None,)
	voiceDialingBlocked: Optional[bool] = Field(alias="voiceDialingBlocked", default=None,)
	webBrowserBlockAutofill: Optional[bool] = Field(alias="webBrowserBlockAutofill", default=None,)
	webBrowserBlocked: Optional[bool] = Field(alias="webBrowserBlocked", default=None,)
	webBrowserBlockJavaScript: Optional[bool] = Field(alias="webBrowserBlockJavaScript", default=None,)
	webBrowserBlockPopups: Optional[bool] = Field(alias="webBrowserBlockPopups", default=None,)
	webBrowserCookieSettings: Optional[WebBrowserCookieSettings | str] = Field(alias="webBrowserCookieSettings", default=None,)
	wiFiBlocked: Optional[bool] = Field(alias="wiFiBlocked", default=None,)

from .device_configuration_assignment import DeviceConfigurationAssignment
from .setting_state_device_summary import SettingStateDeviceSummary
from .device_configuration_device_status import DeviceConfigurationDeviceStatus
from .device_configuration_device_overview import DeviceConfigurationDeviceOverview
from .device_configuration_user_status import DeviceConfigurationUserStatus
from .device_configuration_user_overview import DeviceConfigurationUserOverview
from .app_list_item import AppListItem
from .app_list_type import AppListType
from .android_required_password_type import AndroidRequiredPasswordType
from .web_browser_cookie_settings import WebBrowserCookieSettings
