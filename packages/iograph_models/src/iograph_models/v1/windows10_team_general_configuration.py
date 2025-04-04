from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class Windows10TeamGeneralConfiguration(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.windows10TeamGeneralConfiguration"] = Field(alias="@odata.type", default="#microsoft.graph.windows10TeamGeneralConfiguration")
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
	azureOperationalInsightsBlockTelemetry: Optional[bool] = Field(alias="azureOperationalInsightsBlockTelemetry", default=None,)
	azureOperationalInsightsWorkspaceId: Optional[str] = Field(alias="azureOperationalInsightsWorkspaceId", default=None,)
	azureOperationalInsightsWorkspaceKey: Optional[str] = Field(alias="azureOperationalInsightsWorkspaceKey", default=None,)
	connectAppBlockAutoLaunch: Optional[bool] = Field(alias="connectAppBlockAutoLaunch", default=None,)
	maintenanceWindowBlocked: Optional[bool] = Field(alias="maintenanceWindowBlocked", default=None,)
	maintenanceWindowDurationInHours: Optional[int] = Field(alias="maintenanceWindowDurationInHours", default=None,)
	maintenanceWindowStartTime: Optional[str] = Field(alias="maintenanceWindowStartTime", default=None,)
	miracastBlocked: Optional[bool] = Field(alias="miracastBlocked", default=None,)
	miracastChannel: Optional[MiracastChannel | str] = Field(alias="miracastChannel", default=None,)
	miracastRequirePin: Optional[bool] = Field(alias="miracastRequirePin", default=None,)
	settingsBlockMyMeetingsAndFiles: Optional[bool] = Field(alias="settingsBlockMyMeetingsAndFiles", default=None,)
	settingsBlockSessionResume: Optional[bool] = Field(alias="settingsBlockSessionResume", default=None,)
	settingsBlockSigninSuggestions: Optional[bool] = Field(alias="settingsBlockSigninSuggestions", default=None,)
	settingsDefaultVolume: Optional[int] = Field(alias="settingsDefaultVolume", default=None,)
	settingsScreenTimeoutInMinutes: Optional[int] = Field(alias="settingsScreenTimeoutInMinutes", default=None,)
	settingsSessionTimeoutInMinutes: Optional[int] = Field(alias="settingsSessionTimeoutInMinutes", default=None,)
	settingsSleepTimeoutInMinutes: Optional[int] = Field(alias="settingsSleepTimeoutInMinutes", default=None,)
	welcomeScreenBackgroundImageUrl: Optional[str] = Field(alias="welcomeScreenBackgroundImageUrl", default=None,)
	welcomeScreenBlockAutomaticWakeUp: Optional[bool] = Field(alias="welcomeScreenBlockAutomaticWakeUp", default=None,)
	welcomeScreenMeetingInformation: Optional[WelcomeScreenMeetingInformation | str] = Field(alias="welcomeScreenMeetingInformation", default=None,)

from .device_configuration_assignment import DeviceConfigurationAssignment
from .setting_state_device_summary import SettingStateDeviceSummary
from .device_configuration_device_status import DeviceConfigurationDeviceStatus
from .device_configuration_device_overview import DeviceConfigurationDeviceOverview
from .device_configuration_user_status import DeviceConfigurationUserStatus
from .device_configuration_user_overview import DeviceConfigurationUserOverview
from .miracast_channel import MiracastChannel
from .welcome_screen_meeting_information import WelcomeScreenMeetingInformation
