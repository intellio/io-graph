from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class OmaSettingInteger(BaseModel):
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	omaUri: Optional[str] = Field(default=None,alias="omaUri",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	value: Optional[int] = Field(default=None,alias="value",)


