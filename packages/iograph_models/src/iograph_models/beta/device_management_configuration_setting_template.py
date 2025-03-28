from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementConfigurationSettingTemplate(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	settingInstanceTemplate: Optional[Union[DeviceManagementConfigurationChoiceSettingCollectionInstanceTemplate, DeviceManagementConfigurationChoiceSettingInstanceTemplate, DeviceManagementConfigurationGroupSettingCollectionInstanceTemplate, DeviceManagementConfigurationGroupSettingInstanceTemplate, DeviceManagementConfigurationSimpleSettingCollectionInstanceTemplate, DeviceManagementConfigurationSimpleSettingInstanceTemplate]] = Field(alias="settingInstanceTemplate", default=None,discriminator="odata_type", )
	settingDefinitions: Optional[list[Annotated[Union[DeviceManagementConfigurationChoiceSettingDefinition, DeviceManagementConfigurationChoiceSettingCollectionDefinition, DeviceManagementConfigurationRedirectSettingDefinition, DeviceManagementConfigurationSettingGroupDefinition, DeviceManagementConfigurationSettingGroupCollectionDefinition, DeviceManagementConfigurationSimpleSettingDefinition, DeviceManagementConfigurationSimpleSettingCollectionDefinition],Field(discriminator="odata_type")]]] = Field(alias="settingDefinitions", default=None,)

from .device_management_configuration_choice_setting_collection_instance_template import DeviceManagementConfigurationChoiceSettingCollectionInstanceTemplate
from .device_management_configuration_choice_setting_instance_template import DeviceManagementConfigurationChoiceSettingInstanceTemplate
from .device_management_configuration_group_setting_collection_instance_template import DeviceManagementConfigurationGroupSettingCollectionInstanceTemplate
from .device_management_configuration_group_setting_instance_template import DeviceManagementConfigurationGroupSettingInstanceTemplate
from .device_management_configuration_simple_setting_collection_instance_template import DeviceManagementConfigurationSimpleSettingCollectionInstanceTemplate
from .device_management_configuration_simple_setting_instance_template import DeviceManagementConfigurationSimpleSettingInstanceTemplate
from .device_management_configuration_choice_setting_definition import DeviceManagementConfigurationChoiceSettingDefinition
from .device_management_configuration_choice_setting_collection_definition import DeviceManagementConfigurationChoiceSettingCollectionDefinition
from .device_management_configuration_redirect_setting_definition import DeviceManagementConfigurationRedirectSettingDefinition
from .device_management_configuration_setting_group_definition import DeviceManagementConfigurationSettingGroupDefinition
from .device_management_configuration_setting_group_collection_definition import DeviceManagementConfigurationSettingGroupCollectionDefinition
from .device_management_configuration_simple_setting_definition import DeviceManagementConfigurationSimpleSettingDefinition
from .device_management_configuration_simple_setting_collection_definition import DeviceManagementConfigurationSimpleSettingCollectionDefinition

