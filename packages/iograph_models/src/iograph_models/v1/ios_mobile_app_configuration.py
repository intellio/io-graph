from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class IosMobileAppConfiguration(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	targetedMobileApps: Optional[list[str]] = Field(alias="targetedMobileApps",default=None,)
	version: Optional[int] = Field(alias="version",default=None,)
	assignments: Optional[list[ManagedDeviceMobileAppConfigurationAssignment]] = Field(alias="assignments",default=None,)
	deviceStatuses: Optional[list[ManagedDeviceMobileAppConfigurationDeviceStatus]] = Field(alias="deviceStatuses",default=None,)
	deviceStatusSummary: Optional[ManagedDeviceMobileAppConfigurationDeviceSummary] = Field(alias="deviceStatusSummary",default=None,)
	userStatuses: Optional[list[ManagedDeviceMobileAppConfigurationUserStatus]] = Field(alias="userStatuses",default=None,)
	userStatusSummary: Optional[ManagedDeviceMobileAppConfigurationUserSummary] = Field(alias="userStatusSummary",default=None,)
	encodedSettingXml: Optional[str] = Field(alias="encodedSettingXml",default=None,)
	settings: Optional[list[AppConfigurationSettingItem]] = Field(alias="settings",default=None,)

from .managed_device_mobile_app_configuration_assignment import ManagedDeviceMobileAppConfigurationAssignment
from .managed_device_mobile_app_configuration_device_status import ManagedDeviceMobileAppConfigurationDeviceStatus
from .managed_device_mobile_app_configuration_device_summary import ManagedDeviceMobileAppConfigurationDeviceSummary
from .managed_device_mobile_app_configuration_user_status import ManagedDeviceMobileAppConfigurationUserStatus
from .managed_device_mobile_app_configuration_user_summary import ManagedDeviceMobileAppConfigurationUserSummary
from .app_configuration_setting_item import AppConfigurationSettingItem

