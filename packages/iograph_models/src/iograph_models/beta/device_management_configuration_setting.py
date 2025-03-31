from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from pydantic import BaseModel, Field


class DeviceManagementConfigurationSetting(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.deviceManagementConfigurationSetting"] = Field(alias="@odata.type",)
	settingInstance: Optional[Union[DeviceManagementConfigurationChoiceSettingCollectionInstance, DeviceManagementConfigurationChoiceSettingInstance, DeviceManagementConfigurationGroupSettingCollectionInstance, DeviceManagementConfigurationGroupSettingInstance, DeviceManagementConfigurationSettingGroupCollectionInstance, DeviceManagementConfigurationSettingGroupInstance, DeviceManagementConfigurationSimpleSettingCollectionInstance, DeviceManagementConfigurationSimpleSettingInstance]] = Field(alias="settingInstance", default=None,discriminator="odata_type", )
	settingDefinitions: Optional[list[Annotated[Union[DeviceManagementConfigurationChoiceSettingCollectionDefinition, DeviceManagementConfigurationRedirectSettingDefinition, DeviceManagementConfigurationSettingGroupCollectionDefinition, DeviceManagementConfigurationSimpleSettingCollectionDefinition],Field(discriminator="odata_type")]]] = Field(alias="settingDefinitions", default=None,)

from .device_management_configuration_choice_setting_collection_instance import DeviceManagementConfigurationChoiceSettingCollectionInstance
from .device_management_configuration_choice_setting_instance import DeviceManagementConfigurationChoiceSettingInstance
from .device_management_configuration_group_setting_collection_instance import DeviceManagementConfigurationGroupSettingCollectionInstance
from .device_management_configuration_group_setting_instance import DeviceManagementConfigurationGroupSettingInstance
from .device_management_configuration_setting_group_collection_instance import DeviceManagementConfigurationSettingGroupCollectionInstance
from .device_management_configuration_setting_group_instance import DeviceManagementConfigurationSettingGroupInstance
from .device_management_configuration_simple_setting_collection_instance import DeviceManagementConfigurationSimpleSettingCollectionInstance
from .device_management_configuration_simple_setting_instance import DeviceManagementConfigurationSimpleSettingInstance
from .device_management_configuration_choice_setting_collection_definition import DeviceManagementConfigurationChoiceSettingCollectionDefinition
from .device_management_configuration_redirect_setting_definition import DeviceManagementConfigurationRedirectSettingDefinition
from .device_management_configuration_setting_group_collection_definition import DeviceManagementConfigurationSettingGroupCollectionDefinition
from .device_management_configuration_simple_setting_collection_definition import DeviceManagementConfigurationSimpleSettingCollectionDefinition
