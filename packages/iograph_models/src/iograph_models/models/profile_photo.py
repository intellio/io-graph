from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ProfilePhoto(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	height: Optional[int] = Field(default=None,alias="height",)
	width: Optional[int] = Field(default=None,alias="width",)


