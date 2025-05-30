from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field


class DeviceManagementConfigurationSettingDefinitionCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[DeviceManagementConfigurationChoiceSettingCollectionDefinition, DeviceManagementConfigurationRedirectSettingDefinition, DeviceManagementConfigurationSettingGroupCollectionDefinition, DeviceManagementConfigurationSimpleSettingCollectionDefinition],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .device_management_configuration_choice_setting_collection_definition import DeviceManagementConfigurationChoiceSettingCollectionDefinition
from .device_management_configuration_redirect_setting_definition import DeviceManagementConfigurationRedirectSettingDefinition
from .device_management_configuration_setting_group_collection_definition import DeviceManagementConfigurationSettingGroupCollectionDefinition
from .device_management_configuration_simple_setting_collection_definition import DeviceManagementConfigurationSimpleSettingCollectionDefinition
