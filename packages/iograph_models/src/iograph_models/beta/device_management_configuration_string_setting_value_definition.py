from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class DeviceManagementConfigurationStringSettingValueDefinition(BaseModel):
	odata_type: Literal["#microsoft.graph.deviceManagementConfigurationStringSettingValueDefinition"] = Field(alias="@odata.type", default="#microsoft.graph.deviceManagementConfigurationStringSettingValueDefinition")
	fileTypes: Optional[list[str]] = Field(alias="fileTypes", default=None,)
	format: Optional[DeviceManagementConfigurationStringFormat | str] = Field(alias="format", default=None,)
	inputValidationSchema: Optional[str] = Field(alias="inputValidationSchema", default=None,)
	isSecret: Optional[bool] = Field(alias="isSecret", default=None,)
	maximumLength: Optional[int] = Field(alias="maximumLength", default=None,)
	minimumLength: Optional[int] = Field(alias="minimumLength", default=None,)

from .device_management_configuration_string_format import DeviceManagementConfigurationStringFormat
