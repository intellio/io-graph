from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SortProperty(BaseModel):
	isDescending: Optional[bool] = Field(default=None,alias="isDescending",)
	name: Optional[str] = Field(default=None,alias="name",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


