from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementConfigurationStringSettingValueDefinition(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	fileTypes: Optional[list[str]] = Field(alias="fileTypes",default=None,)
	format: Optional[DeviceManagementConfigurationStringFormat | str] = Field(alias="format",default=None,)
	inputValidationSchema: Optional[str] = Field(alias="inputValidationSchema",default=None,)
	isSecret: Optional[bool] = Field(alias="isSecret",default=None,)
	maximumLength: Optional[int] = Field(alias="maximumLength",default=None,)
	minimumLength: Optional[int] = Field(alias="minimumLength",default=None,)

from .device_management_configuration_string_format import DeviceManagementConfigurationStringFormat

