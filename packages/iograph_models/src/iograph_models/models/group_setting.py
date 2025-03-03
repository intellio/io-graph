from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class GroupSetting(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	templateId: Optional[str] = Field(default=None,alias="templateId",)
	values: Optional[list[SettingValue]] = Field(default=None,alias="values",)

from .setting_value import SettingValue

