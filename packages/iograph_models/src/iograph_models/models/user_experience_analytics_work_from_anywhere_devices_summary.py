from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class UserExperienceAnalyticsWorkFromAnywhereDevicesSummary(BaseModel):
	autopilotDevicesSummary: Optional[UserExperienceAnalyticsAutopilotDevicesSummary] = Field(alias="autopilotDevicesSummary",default=None,)
	cloudIdentityDevicesSummary: Optional[UserExperienceAnalyticsCloudIdentityDevicesSummary] = Field(alias="cloudIdentityDevicesSummary",default=None,)
	cloudManagementDevicesSummary: Optional[UserExperienceAnalyticsCloudManagementDevicesSummary] = Field(alias="cloudManagementDevicesSummary",default=None,)
	coManagedDevices: Optional[int] = Field(alias="coManagedDevices",default=None,)
	devicesNotAutopilotRegistered: Optional[int] = Field(alias="devicesNotAutopilotRegistered",default=None,)
	devicesWithoutAutopilotProfileAssigned: Optional[int] = Field(alias="devicesWithoutAutopilotProfileAssigned",default=None,)
	devicesWithoutCloudIdentity: Optional[int] = Field(alias="devicesWithoutCloudIdentity",default=None,)
	intuneDevices: Optional[int] = Field(alias="intuneDevices",default=None,)
	tenantAttachDevices: Optional[int] = Field(alias="tenantAttachDevices",default=None,)
	totalDevices: Optional[int] = Field(alias="totalDevices",default=None,)
	unsupportedOSversionDevices: Optional[int] = Field(alias="unsupportedOSversionDevices",default=None,)
	windows10Devices: Optional[int] = Field(alias="windows10Devices",default=None,)
	windows10DevicesSummary: Optional[UserExperienceAnalyticsWindows10DevicesSummary] = Field(alias="windows10DevicesSummary",default=None,)
	windows10DevicesWithoutTenantAttach: Optional[int] = Field(alias="windows10DevicesWithoutTenantAttach",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .user_experience_analytics_autopilot_devices_summary import UserExperienceAnalyticsAutopilotDevicesSummary
from .user_experience_analytics_cloud_identity_devices_summary import UserExperienceAnalyticsCloudIdentityDevicesSummary
from .user_experience_analytics_cloud_management_devices_summary import UserExperienceAnalyticsCloudManagementDevicesSummary
from .user_experience_analytics_windows10_devices_summary import UserExperienceAnalyticsWindows10DevicesSummary

