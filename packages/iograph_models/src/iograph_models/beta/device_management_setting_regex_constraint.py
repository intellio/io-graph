from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class DeviceManagementSettingRegexConstraint(BaseModel):
	odata_type: Literal["#microsoft.graph.deviceManagementSettingRegexConstraint"] = Field(alias="@odata.type", default="#microsoft.graph.deviceManagementSettingRegexConstraint")
	regex: Optional[str] = Field(alias="regex", default=None,)

