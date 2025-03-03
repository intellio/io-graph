from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class Windows10SecureAssessmentConfiguration(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	version: Optional[int] = Field(default=None,alias="version",)
	assignments: Optional[list[DeviceConfigurationAssignment]] = Field(default=None,alias="assignments",)
	deviceSettingStateSummaries: Optional[list[SettingStateDeviceSummary]] = Field(default=None,alias="deviceSettingStateSummaries",)
	deviceStatuses: Optional[list[DeviceConfigurationDeviceStatus]] = Field(default=None,alias="deviceStatuses",)
	deviceStatusOverview: Optional[DeviceConfigurationDeviceOverview] = Field(default=None,alias="deviceStatusOverview",)
	userStatuses: Optional[list[DeviceConfigurationUserStatus]] = Field(default=None,alias="userStatuses",)
	userStatusOverview: Optional[DeviceConfigurationUserOverview] = Field(default=None,alias="userStatusOverview",)
	allowPrinting: Optional[bool] = Field(default=None,alias="allowPrinting",)
	allowScreenCapture: Optional[bool] = Field(default=None,alias="allowScreenCapture",)
	allowTextSuggestion: Optional[bool] = Field(default=None,alias="allowTextSuggestion",)
	configurationAccount: Optional[str] = Field(default=None,alias="configurationAccount",)
	launchUri: Optional[str] = Field(default=None,alias="launchUri",)

from .device_configuration_assignment import DeviceConfigurationAssignment
from .setting_state_device_summary import SettingStateDeviceSummary
from .device_configuration_device_status import DeviceConfigurationDeviceStatus
from .device_configuration_device_overview import DeviceConfigurationDeviceOverview
from .device_configuration_user_status import DeviceConfigurationUserStatus
from .device_configuration_user_overview import DeviceConfigurationUserOverview

