from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class GroupSetting(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.groupSetting"] = Field(alias="@odata.type", default="#microsoft.graph.groupSetting")
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	templateId: Optional[str] = Field(alias="templateId", default=None,)
	values: Optional[list[SettingValue]] = Field(alias="values", default=None,)

from .setting_value import SettingValue
