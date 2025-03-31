from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class Windows10SecureAssessmentConfiguration(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.windows10SecureAssessmentConfiguration"] = Field(alias="@odata.type", default="#microsoft.graph.windows10SecureAssessmentConfiguration")
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
	allowPrinting: Optional[bool] = Field(alias="allowPrinting", default=None,)
	allowScreenCapture: Optional[bool] = Field(alias="allowScreenCapture", default=None,)
	allowTextSuggestion: Optional[bool] = Field(alias="allowTextSuggestion", default=None,)
	configurationAccount: Optional[str] = Field(alias="configurationAccount", default=None,)
	launchUri: Optional[str] = Field(alias="launchUri", default=None,)

from .device_configuration_assignment import DeviceConfigurationAssignment
from .setting_state_device_summary import SettingStateDeviceSummary
from .device_configuration_device_status import DeviceConfigurationDeviceStatus
from .device_configuration_device_overview import DeviceConfigurationDeviceOverview
from .device_configuration_user_status import DeviceConfigurationUserStatus
from .device_configuration_user_overview import DeviceConfigurationUserOverview
