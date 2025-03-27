from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementSettingProfileConstraint(BaseModel):
	odata_type: Literal["#microsoft.graph.deviceManagementSettingProfileConstraint"] = Field(alias="@odata.type", default="#microsoft.graph.deviceManagementSettingProfileConstraint")
	source: Optional[str] = Field(alias="source", default=None,)
	types: Optional[list[str]] = Field(alias="types", default=None,)


