from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class WindowsPhone81GeneralConfiguration(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	version: Optional[int] = Field(default=None,alias="version",)
	assignments: list[DeviceConfigurationAssignment] = Field(alias="assignments",)
	deviceSettingStateSummaries: list[SettingStateDeviceSummary] = Field(alias="deviceSettingStateSummaries",)
	deviceStatuses: list[DeviceConfigurationDeviceStatus] = Field(alias="deviceStatuses",)
	deviceStatusOverview: Optional[DeviceConfigurationDeviceOverview] = Field(default=None,alias="deviceStatusOverview",)
	userStatuses: list[DeviceConfigurationUserStatus] = Field(alias="userStatuses",)
	userStatusOverview: Optional[DeviceConfigurationUserOverview] = Field(default=None,alias="userStatusOverview",)
	applyOnlyToWindowsPhone81: Optional[bool] = Field(default=None,alias="applyOnlyToWindowsPhone81",)
	appsBlockCopyPaste: Optional[bool] = Field(default=None,alias="appsBlockCopyPaste",)
	bluetoothBlocked: Optional[bool] = Field(default=None,alias="bluetoothBlocked",)
	cameraBlocked: Optional[bool] = Field(default=None,alias="cameraBlocked",)
	cellularBlockWifiTethering: Optional[bool] = Field(default=None,alias="cellularBlockWifiTethering",)
	compliantAppListType: Optional[AppListType] = Field(default=None,alias="compliantAppListType",)
	compliantAppsList: list[AppListItem] = Field(alias="compliantAppsList",)
	diagnosticDataBlockSubmission: Optional[bool] = Field(default=None,alias="diagnosticDataBlockSubmission",)
	emailBlockAddingAccounts: Optional[bool] = Field(default=None,alias="emailBlockAddingAccounts",)
	locationServicesBlocked: Optional[bool] = Field(default=None,alias="locationServicesBlocked",)
	microsoftAccountBlocked: Optional[bool] = Field(default=None,alias="microsoftAccountBlocked",)
	nfcBlocked: Optional[bool] = Field(default=None,alias="nfcBlocked",)
	passwordBlockSimple: Optional[bool] = Field(default=None,alias="passwordBlockSimple",)
	passwordExpirationDays: Optional[int] = Field(default=None,alias="passwordExpirationDays",)
	passwordMinimumCharacterSetCount: Optional[int] = Field(default=None,alias="passwordMinimumCharacterSetCount",)
	passwordMinimumLength: Optional[int] = Field(default=None,alias="passwordMinimumLength",)
	passwordMinutesOfInactivityBeforeScreenTimeout: Optional[int] = Field(default=None,alias="passwordMinutesOfInactivityBeforeScreenTimeout",)
	passwordPreviousPasswordBlockCount: Optional[int] = Field(default=None,alias="passwordPreviousPasswordBlockCount",)
	passwordRequired: Optional[bool] = Field(default=None,alias="passwordRequired",)
	passwordRequiredType: Optional[RequiredPasswordType] = Field(default=None,alias="passwordRequiredType",)
	passwordSignInFailureCountBeforeFactoryReset: Optional[int] = Field(default=None,alias="passwordSignInFailureCountBeforeFactoryReset",)
	screenCaptureBlocked: Optional[bool] = Field(default=None,alias="screenCaptureBlocked",)
	storageBlockRemovableStorage: Optional[bool] = Field(default=None,alias="storageBlockRemovableStorage",)
	storageRequireEncryption: Optional[bool] = Field(default=None,alias="storageRequireEncryption",)
	webBrowserBlocked: Optional[bool] = Field(default=None,alias="webBrowserBlocked",)
	wifiBlockAutomaticConnectHotspots: Optional[bool] = Field(default=None,alias="wifiBlockAutomaticConnectHotspots",)
	wifiBlocked: Optional[bool] = Field(default=None,alias="wifiBlocked",)
	wifiBlockHotspotReporting: Optional[bool] = Field(default=None,alias="wifiBlockHotspotReporting",)
	windowsStoreBlocked: Optional[bool] = Field(default=None,alias="windowsStoreBlocked",)

from .device_configuration_assignment import DeviceConfigurationAssignment
from .setting_state_device_summary import SettingStateDeviceSummary
from .device_configuration_device_status import DeviceConfigurationDeviceStatus
from .device_configuration_device_overview import DeviceConfigurationDeviceOverview
from .device_configuration_user_status import DeviceConfigurationUserStatus
from .device_configuration_user_overview import DeviceConfigurationUserOverview
from .app_list_type import AppListType
from .app_list_item import AppListItem
from .required_password_type import RequiredPasswordType

