from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementConfigurationCategory(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	categoryDescription: Optional[str] = Field(alias="categoryDescription",default=None,)
	childCategoryIds: Optional[list[str]] = Field(alias="childCategoryIds",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	helpText: Optional[str] = Field(alias="helpText",default=None,)
	name: Optional[str] = Field(alias="name",default=None,)
	parentCategoryId: Optional[str] = Field(alias="parentCategoryId",default=None,)
	platforms: Optional[DeviceManagementConfigurationPlatforms | str] = Field(alias="platforms",default=None,)
	rootCategoryId: Optional[str] = Field(alias="rootCategoryId",default=None,)
	settingUsage: Optional[DeviceManagementConfigurationSettingUsage | str] = Field(alias="settingUsage",default=None,)
	technologies: Optional[DeviceManagementConfigurationTechnologies | str] = Field(alias="technologies",default=None,)

from .device_management_configuration_platforms import DeviceManagementConfigurationPlatforms
from .device_management_configuration_setting_usage import DeviceManagementConfigurationSettingUsage
from .device_management_configuration_technologies import DeviceManagementConfigurationTechnologies

