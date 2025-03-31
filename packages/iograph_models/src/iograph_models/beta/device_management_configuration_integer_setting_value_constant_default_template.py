from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class DeviceManagementConfigurationIntegerSettingValueConstantDefaultTemplate(BaseModel):
	odata_type: Literal["#microsoft.graph.deviceManagementConfigurationIntegerSettingValueConstantDefaultTemplate"] = Field(alias="@odata.type", default="#microsoft.graph.deviceManagementConfigurationIntegerSettingValueConstantDefaultTemplate")
	constantValue: Optional[int] = Field(alias="constantValue", default=None,)

