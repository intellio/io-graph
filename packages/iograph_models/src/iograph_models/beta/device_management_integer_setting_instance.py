from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class DeviceManagementIntegerSettingInstance(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.deviceManagementIntegerSettingInstance"] = Field(alias="@odata.type", default="#microsoft.graph.deviceManagementIntegerSettingInstance")
	definitionId: Optional[str] = Field(alias="definitionId", default=None,)
	valueJson: Optional[str] = Field(alias="valueJson", default=None,)
	value: Optional[int] = Field(alias="value", default=None,)

