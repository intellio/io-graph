from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class DeviceManagementSettingFileConstraint(BaseModel):
	odata_type: Literal["#microsoft.graph.deviceManagementSettingFileConstraint"] = Field(alias="@odata.type", default="#microsoft.graph.deviceManagementSettingFileConstraint")
	supportedExtensions: Optional[list[str]] = Field(alias="supportedExtensions", default=None,)

