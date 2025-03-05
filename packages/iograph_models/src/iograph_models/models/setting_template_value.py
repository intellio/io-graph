from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SettingTemplateValue(BaseModel):
	defaultValue: Optional[str] = Field(default=None,alias="defaultValue",)
	description: Optional[str] = Field(default=None,alias="description",)
	name: Optional[str] = Field(default=None,alias="name",)
	type: Optional[str] = Field(default=None,alias="type",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


