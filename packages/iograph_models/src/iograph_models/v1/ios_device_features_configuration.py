from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from datetime import datetime
from pydantic import BaseModel, Field


class IosDeviceFeaturesConfiguration(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.iosDeviceFeaturesConfiguration"] = Field(alias="@odata.type", default="#microsoft.graph.iosDeviceFeaturesConfiguration")
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
	assetTagTemplate: Optional[str] = Field(alias="assetTagTemplate", default=None,)
	homeScreenDockIcons: Optional[list[Annotated[Union[IosHomeScreenApp, IosHomeScreenFolder],Field(discriminator="odata_type")]]] = Field(alias="homeScreenDockIcons", default=None,)
	homeScreenPages: Optional[list[IosHomeScreenPage]] = Field(alias="homeScreenPages", default=None,)
	lockScreenFootnote: Optional[str] = Field(alias="lockScreenFootnote", default=None,)
	notificationSettings: Optional[list[IosNotificationSettings]] = Field(alias="notificationSettings", default=None,)

from .device_configuration_assignment import DeviceConfigurationAssignment
from .setting_state_device_summary import SettingStateDeviceSummary
from .device_configuration_device_status import DeviceConfigurationDeviceStatus
from .device_configuration_device_overview import DeviceConfigurationDeviceOverview
from .device_configuration_user_status import DeviceConfigurationUserStatus
from .device_configuration_user_overview import DeviceConfigurationUserOverview
from .ios_home_screen_app import IosHomeScreenApp
from .ios_home_screen_folder import IosHomeScreenFolder
from .ios_home_screen_page import IosHomeScreenPage
from .ios_notification_settings import IosNotificationSettings
