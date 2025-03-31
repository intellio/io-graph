from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class DeviceManagementConfigurationApplicationSettingApplicability(BaseModel):
	description: Optional[str] = Field(alias="description", default=None,)
	deviceMode: Optional[DeviceManagementConfigurationDeviceMode | str] = Field(alias="deviceMode", default=None,)
	platform: Optional[DeviceManagementConfigurationPlatforms | str] = Field(alias="platform", default=None,)
	technologies: Optional[DeviceManagementConfigurationTechnologies | str] = Field(alias="technologies", default=None,)
	odata_type: Literal["#microsoft.graph.deviceManagementConfigurationApplicationSettingApplicability"] = Field(alias="@odata.type", default="#microsoft.graph.deviceManagementConfigurationApplicationSettingApplicability")

from .device_management_configuration_device_mode import DeviceManagementConfigurationDeviceMode
from .device_management_configuration_platforms import DeviceManagementConfigurationPlatforms
from .device_management_configuration_technologies import DeviceManagementConfigurationTechnologies
