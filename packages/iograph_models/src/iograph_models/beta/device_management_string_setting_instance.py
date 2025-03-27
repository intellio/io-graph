from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementStringSettingInstance(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.deviceManagementStringSettingInstance"] = Field(alias="@odata.type", default="#microsoft.graph.deviceManagementStringSettingInstance")
	definitionId: Optional[str] = Field(alias="definitionId", default=None,)
	valueJson: Optional[str] = Field(alias="valueJson", default=None,)
	value: Optional[str] = Field(alias="value", default=None,)


