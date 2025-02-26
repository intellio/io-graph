from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class Windows10TeamGeneralConfiguration(BaseModel):
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
	azureOperationalInsightsBlockTelemetry: Optional[bool] = Field(default=None,alias="azureOperationalInsightsBlockTelemetry",)
	azureOperationalInsightsWorkspaceId: Optional[str] = Field(default=None,alias="azureOperationalInsightsWorkspaceId",)
	azureOperationalInsightsWorkspaceKey: Optional[str] = Field(default=None,alias="azureOperationalInsightsWorkspaceKey",)
	connectAppBlockAutoLaunch: Optional[bool] = Field(default=None,alias="connectAppBlockAutoLaunch",)
	maintenanceWindowBlocked: Optional[bool] = Field(default=None,alias="maintenanceWindowBlocked",)
	maintenanceWindowDurationInHours: Optional[int] = Field(default=None,alias="maintenanceWindowDurationInHours",)
	maintenanceWindowStartTime: Optional[str] = Field(default=None,alias="maintenanceWindowStartTime",)
	miracastBlocked: Optional[bool] = Field(default=None,alias="miracastBlocked",)
	miracastChannel: Optional[MiracastChannel] = Field(default=None,alias="miracastChannel",)
	miracastRequirePin: Optional[bool] = Field(default=None,alias="miracastRequirePin",)
	settingsBlockMyMeetingsAndFiles: Optional[bool] = Field(default=None,alias="settingsBlockMyMeetingsAndFiles",)
	settingsBlockSessionResume: Optional[bool] = Field(default=None,alias="settingsBlockSessionResume",)
	settingsBlockSigninSuggestions: Optional[bool] = Field(default=None,alias="settingsBlockSigninSuggestions",)
	settingsDefaultVolume: Optional[int] = Field(default=None,alias="settingsDefaultVolume",)
	settingsScreenTimeoutInMinutes: Optional[int] = Field(default=None,alias="settingsScreenTimeoutInMinutes",)
	settingsSessionTimeoutInMinutes: Optional[int] = Field(default=None,alias="settingsSessionTimeoutInMinutes",)
	settingsSleepTimeoutInMinutes: Optional[int] = Field(default=None,alias="settingsSleepTimeoutInMinutes",)
	welcomeScreenBackgroundImageUrl: Optional[str] = Field(default=None,alias="welcomeScreenBackgroundImageUrl",)
	welcomeScreenBlockAutomaticWakeUp: Optional[bool] = Field(default=None,alias="welcomeScreenBlockAutomaticWakeUp",)
	welcomeScreenMeetingInformation: Optional[WelcomeScreenMeetingInformation] = Field(default=None,alias="welcomeScreenMeetingInformation",)

from .device_configuration_assignment import DeviceConfigurationAssignment
from .setting_state_device_summary import SettingStateDeviceSummary
from .device_configuration_device_status import DeviceConfigurationDeviceStatus
from .device_configuration_device_overview import DeviceConfigurationDeviceOverview
from .device_configuration_user_status import DeviceConfigurationUserStatus
from .device_configuration_user_overview import DeviceConfigurationUserOverview
from .miracast_channel import MiracastChannel
from .welcome_screen_meeting_information import WelcomeScreenMeetingInformation

