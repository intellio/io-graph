from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class OmaSettingString(BaseModel):
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	omaUri: Optional[str] = Field(default=None,alias="omaUri",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	value: Optional[str] = Field(default=None,alias="value",)


