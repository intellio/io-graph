from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementSettingAppConstraint(BaseModel):
	odata_type: Literal["#microsoft.graph.deviceManagementSettingAppConstraint"] = Field(alias="@odata.type", default="#microsoft.graph.deviceManagementSettingAppConstraint")
	supportedTypes: Optional[list[str]] = Field(alias="supportedTypes", default=None,)


