from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SettingSource(BaseModel):
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	id: Optional[str] = Field(default=None,alias="id",)
	sourceType: Optional[SettingSourceType] = Field(default=None,alias="sourceType",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .setting_source_type import SettingSourceType

