from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class UserAttributeValuesItem(BaseModel):
	isDefault: Optional[bool] = Field(default=None,alias="isDefault",)
	name: Optional[str] = Field(default=None,alias="name",)
	value: Optional[str] = Field(default=None,alias="value",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


