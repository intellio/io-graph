from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class DeviceManagementConfigurationWindowsSettingApplicability(BaseModel):
	description: Optional[str] = Field(alias="description", default=None,)
	deviceMode: Optional[DeviceManagementConfigurationDeviceMode | str] = Field(alias="deviceMode", default=None,)
	platform: Optional[DeviceManagementConfigurationPlatforms | str] = Field(alias="platform", default=None,)
	technologies: Optional[DeviceManagementConfigurationTechnologies | str] = Field(alias="technologies", default=None,)
	odata_type: Literal["#microsoft.graph.deviceManagementConfigurationWindowsSettingApplicability"] = Field(alias="@odata.type", default="#microsoft.graph.deviceManagementConfigurationWindowsSettingApplicability")
	configurationServiceProviderVersion: Optional[str] = Field(alias="configurationServiceProviderVersion", default=None,)
	maximumSupportedVersion: Optional[str] = Field(alias="maximumSupportedVersion", default=None,)
	minimumSupportedVersion: Optional[str] = Field(alias="minimumSupportedVersion", default=None,)
	requiredAzureAdTrustType: Optional[DeviceManagementConfigurationAzureAdTrustType | str] = Field(alias="requiredAzureAdTrustType", default=None,)
	requiresAzureAd: Optional[bool] = Field(alias="requiresAzureAd", default=None,)
	windowsSkus: Optional[list[DeviceManagementConfigurationWindowsSkus | str]] = Field(alias="windowsSkus", default=None,)

from .device_management_configuration_device_mode import DeviceManagementConfigurationDeviceMode
from .device_management_configuration_platforms import DeviceManagementConfigurationPlatforms
from .device_management_configuration_technologies import DeviceManagementConfigurationTechnologies
from .device_management_configuration_azure_ad_trust_type import DeviceManagementConfigurationAzureAdTrustType
from .device_management_configuration_windows_skus import DeviceManagementConfigurationWindowsSkus
