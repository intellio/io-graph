from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class InternetMessageHeader(BaseModel):
	name: Optional[str] = Field(default=None,alias="name",)
	value: Optional[str] = Field(default=None,alias="value",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


