from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class IosDeviceFeaturesConfiguration(BaseModel):
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
	assetTagTemplate: Optional[str] = Field(default=None,alias="assetTagTemplate",)
	homeScreenDockIcons: list[IosHomeScreenItem] = Field(alias="homeScreenDockIcons",)
	homeScreenPages: list[IosHomeScreenPage] = Field(alias="homeScreenPages",)
	lockScreenFootnote: Optional[str] = Field(default=None,alias="lockScreenFootnote",)
	notificationSettings: list[IosNotificationSettings] = Field(alias="notificationSettings",)

from .device_configuration_assignment import DeviceConfigurationAssignment
from .setting_state_device_summary import SettingStateDeviceSummary
from .device_configuration_device_status import DeviceConfigurationDeviceStatus
from .device_configuration_device_overview import DeviceConfigurationDeviceOverview
from .device_configuration_user_status import DeviceConfigurationUserStatus
from .device_configuration_user_overview import DeviceConfigurationUserOverview
from .ios_home_screen_item import IosHomeScreenItem
from .ios_home_screen_page import IosHomeScreenPage
from .ios_notification_settings import IosNotificationSettings

