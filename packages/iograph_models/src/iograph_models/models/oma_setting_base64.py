from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class OmaSettingBase64(BaseModel):
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	omaUri: Optional[str] = Field(default=None,alias="omaUri",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	fileName: Optional[str] = Field(default=None,alias="fileName",)
	value: Optional[str] = Field(default=None,alias="value",)


