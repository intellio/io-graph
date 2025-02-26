from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class UserExperienceAnalyticsWorkFromAnywhereDevicesSummary(BaseModel):
	autopilotDevicesSummary: Optional[UserExperienceAnalyticsAutopilotDevicesSummary] = Field(default=None,alias="autopilotDevicesSummary",)
	cloudIdentityDevicesSummary: Optional[UserExperienceAnalyticsCloudIdentityDevicesSummary] = Field(default=None,alias="cloudIdentityDevicesSummary",)
	cloudManagementDevicesSummary: Optional[UserExperienceAnalyticsCloudManagementDevicesSummary] = Field(default=None,alias="cloudManagementDevicesSummary",)
	coManagedDevices: Optional[int] = Field(default=None,alias="coManagedDevices",)
	devicesNotAutopilotRegistered: Optional[int] = Field(default=None,alias="devicesNotAutopilotRegistered",)
	devicesWithoutAutopilotProfileAssigned: Optional[int] = Field(default=None,alias="devicesWithoutAutopilotProfileAssigned",)
	devicesWithoutCloudIdentity: Optional[int] = Field(default=None,alias="devicesWithoutCloudIdentity",)
	intuneDevices: Optional[int] = Field(default=None,alias="intuneDevices",)
	tenantAttachDevices: Optional[int] = Field(default=None,alias="tenantAttachDevices",)
	totalDevices: Optional[int] = Field(default=None,alias="totalDevices",)
	unsupportedOSversionDevices: Optional[int] = Field(default=None,alias="unsupportedOSversionDevices",)
	windows10Devices: Optional[int] = Field(default=None,alias="windows10Devices",)
	windows10DevicesSummary: Optional[UserExperienceAnalyticsWindows10DevicesSummary] = Field(default=None,alias="windows10DevicesSummary",)
	windows10DevicesWithoutTenantAttach: Optional[int] = Field(default=None,alias="windows10DevicesWithoutTenantAttach",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .user_experience_analytics_autopilot_devices_summary import UserExperienceAnalyticsAutopilotDevicesSummary
from .user_experience_analytics_cloud_identity_devices_summary import UserExperienceAnalyticsCloudIdentityDevicesSummary
from .user_experience_analytics_cloud_management_devices_summary import UserExperienceAnalyticsCloudManagementDevicesSummary
from .user_experience_analytics_windows10_devices_summary import UserExperienceAnalyticsWindows10DevicesSummary

