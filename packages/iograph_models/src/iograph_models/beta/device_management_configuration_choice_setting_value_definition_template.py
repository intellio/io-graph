from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class DeviceManagementConfigurationChoiceSettingValueDefinitionTemplate(BaseModel):
	allowedOptions: Optional[list[DeviceManagementConfigurationOptionDefinitionTemplate]] = Field(alias="allowedOptions", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .device_management_configuration_option_definition_template import DeviceManagementConfigurationOptionDefinitionTemplate
