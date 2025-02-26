from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class OmaSettingDateTime(BaseModel):
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	omaUri: Optional[str] = Field(default=None,alias="omaUri",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	value: Optional[datetime] = Field(default=None,alias="value",)


