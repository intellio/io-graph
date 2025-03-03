from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class IosMobileAppConfiguration(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	targetedMobileApps: Optional[list[str]] = Field(default=None,alias="targetedMobileApps",)
	version: Optional[int] = Field(default=None,alias="version",)
	assignments: Optional[list[ManagedDeviceMobileAppConfigurationAssignment]] = Field(default=None,alias="assignments",)
	deviceStatuses: Optional[list[ManagedDeviceMobileAppConfigurationDeviceStatus]] = Field(default=None,alias="deviceStatuses",)
	deviceStatusSummary: Optional[ManagedDeviceMobileAppConfigurationDeviceSummary] = Field(default=None,alias="deviceStatusSummary",)
	userStatuses: Optional[list[ManagedDeviceMobileAppConfigurationUserStatus]] = Field(default=None,alias="userStatuses",)
	userStatusSummary: Optional[ManagedDeviceMobileAppConfigurationUserSummary] = Field(default=None,alias="userStatusSummary",)
	encodedSettingXml: Optional[str] = Field(default=None,alias="encodedSettingXml",)
	settings: Optional[list[AppConfigurationSettingItem]] = Field(default=None,alias="settings",)

from .managed_device_mobile_app_configuration_assignment import ManagedDeviceMobileAppConfigurationAssignment
from .managed_device_mobile_app_configuration_device_status import ManagedDeviceMobileAppConfigurationDeviceStatus
from .managed_device_mobile_app_configuration_device_summary import ManagedDeviceMobileAppConfigurationDeviceSummary
from .managed_device_mobile_app_configuration_user_status import ManagedDeviceMobileAppConfigurationUserStatus
from .managed_device_mobile_app_configuration_user_summary import ManagedDeviceMobileAppConfigurationUserSummary
from .app_configuration_setting_item import AppConfigurationSettingItem

