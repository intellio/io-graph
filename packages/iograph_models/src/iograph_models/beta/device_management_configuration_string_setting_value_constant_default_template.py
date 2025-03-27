from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementConfigurationStringSettingValueConstantDefaultTemplate(BaseModel):
	odata_type: Literal["#microsoft.graph.deviceManagementConfigurationStringSettingValueConstantDefaultTemplate"] = Field(alias="@odata.type", default="#microsoft.graph.deviceManagementConfigurationStringSettingValueConstantDefaultTemplate")
	constantValue: Optional[str] = Field(alias="constantValue", default=None,)


