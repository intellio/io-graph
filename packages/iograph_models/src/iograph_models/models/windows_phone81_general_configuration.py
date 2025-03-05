from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsPhone81GeneralConfiguration(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	version: Optional[int] = Field(alias="version",default=None,)
	assignments: Optional[list[DeviceConfigurationAssignment]] = Field(alias="assignments",default=None,)
	deviceSettingStateSummaries: Optional[list[SettingStateDeviceSummary]] = Field(alias="deviceSettingStateSummaries",default=None,)
	deviceStatuses: Optional[list[DeviceConfigurationDeviceStatus]] = Field(alias="deviceStatuses",default=None,)
	deviceStatusOverview: Optional[DeviceConfigurationDeviceOverview] = Field(alias="deviceStatusOverview",default=None,)
	userStatuses: Optional[list[DeviceConfigurationUserStatus]] = Field(alias="userStatuses",default=None,)
	userStatusOverview: Optional[DeviceConfigurationUserOverview] = Field(alias="userStatusOverview",default=None,)
	applyOnlyToWindowsPhone81: Optional[bool] = Field(alias="applyOnlyToWindowsPhone81",default=None,)
	appsBlockCopyPaste: Optional[bool] = Field(alias="appsBlockCopyPaste",default=None,)
	bluetoothBlocked: Optional[bool] = Field(alias="bluetoothBlocked",default=None,)
	cameraBlocked: Optional[bool] = Field(alias="cameraBlocked",default=None,)
	cellularBlockWifiTethering: Optional[bool] = Field(alias="cellularBlockWifiTethering",default=None,)
	compliantAppListType: Optional[str | AppListType] = Field(alias="compliantAppListType",default=None,)
	compliantAppsList: Optional[list[AppListItem]] = Field(alias="compliantAppsList",default=None,)
	diagnosticDataBlockSubmission: Optional[bool] = Field(alias="diagnosticDataBlockSubmission",default=None,)
	emailBlockAddingAccounts: Optional[bool] = Field(alias="emailBlockAddingAccounts",default=None,)
	locationServicesBlocked: Optional[bool] = Field(alias="locationServicesBlocked",default=None,)
	microsoftAccountBlocked: Optional[bool] = Field(alias="microsoftAccountBlocked",default=None,)
	nfcBlocked: Optional[bool] = Field(alias="nfcBlocked",default=None,)
	passwordBlockSimple: Optional[bool] = Field(alias="passwordBlockSimple",default=None,)
	passwordExpirationDays: Optional[int] = Field(alias="passwordExpirationDays",default=None,)
	passwordMinimumCharacterSetCount: Optional[int] = Field(alias="passwordMinimumCharacterSetCount",default=None,)
	passwordMinimumLength: Optional[int] = Field(alias="passwordMinimumLength",default=None,)
	passwordMinutesOfInactivityBeforeScreenTimeout: Optional[int] = Field(alias="passwordMinutesOfInactivityBeforeScreenTimeout",default=None,)
	passwordPreviousPasswordBlockCount: Optional[int] = Field(alias="passwordPreviousPasswordBlockCount",default=None,)
	passwordRequired: Optional[bool] = Field(alias="passwordRequired",default=None,)
	passwordRequiredType: Optional[str | RequiredPasswordType] = Field(alias="passwordRequiredType",default=None,)
	passwordSignInFailureCountBeforeFactoryReset: Optional[int] = Field(alias="passwordSignInFailureCountBeforeFactoryReset",default=None,)
	screenCaptureBlocked: Optional[bool] = Field(alias="screenCaptureBlocked",default=None,)
	storageBlockRemovableStorage: Optional[bool] = Field(alias="storageBlockRemovableStorage",default=None,)
	storageRequireEncryption: Optional[bool] = Field(alias="storageRequireEncryption",default=None,)
	webBrowserBlocked: Optional[bool] = Field(alias="webBrowserBlocked",default=None,)
	wifiBlockAutomaticConnectHotspots: Optional[bool] = Field(alias="wifiBlockAutomaticConnectHotspots",default=None,)
	wifiBlocked: Optional[bool] = Field(alias="wifiBlocked",default=None,)
	wifiBlockHotspotReporting: Optional[bool] = Field(alias="wifiBlockHotspotReporting",default=None,)
	windowsStoreBlocked: Optional[bool] = Field(alias="windowsStoreBlocked",default=None,)

from .device_configuration_assignment import DeviceConfigurationAssignment
from .setting_state_device_summary import SettingStateDeviceSummary
from .device_configuration_device_status import DeviceConfigurationDeviceStatus
from .device_configuration_device_overview import DeviceConfigurationDeviceOverview
from .device_configuration_user_status import DeviceConfigurationUserStatus
from .device_configuration_user_overview import DeviceConfigurationUserOverview
from .app_list_type import AppListType
from .app_list_item import AppListItem
from .required_password_type import RequiredPasswordType

