from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from pydantic import BaseModel, Field


class DeviceManagementConfigurationSimpleSettingInstance(BaseModel):
	settingDefinitionId: Optional[str] = Field(alias="settingDefinitionId", default=None,)
	settingInstanceTemplateReference: Optional[DeviceManagementConfigurationSettingInstanceTemplateReference] = Field(alias="settingInstanceTemplateReference", default=None,)
	odata_type: Literal["#microsoft.graph.deviceManagementConfigurationSimpleSettingInstance"] = Field(alias="@odata.type", default="#microsoft.graph.deviceManagementConfigurationSimpleSettingInstance")
	simpleSettingValue: Optional[Union[DeviceManagementConfigurationIntegerSettingValue, DeviceManagementConfigurationSecretSettingValue, DeviceManagementConfigurationReferenceSettingValue]] = Field(alias="simpleSettingValue", default=None,discriminator="odata_type", )

from .device_management_configuration_setting_instance_template_reference import DeviceManagementConfigurationSettingInstanceTemplateReference
from .device_management_configuration_integer_setting_value import DeviceManagementConfigurationIntegerSettingValue
from .device_management_configuration_secret_setting_value import DeviceManagementConfigurationSecretSettingValue
from .device_management_configuration_reference_setting_value import DeviceManagementConfigurationReferenceSettingValue
