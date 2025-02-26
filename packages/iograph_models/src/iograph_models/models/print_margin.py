from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class PrintMargin(BaseModel):
	bottom: Optional[int] = Field(default=None,alias="bottom",)
	left: Optional[int] = Field(default=None,alias="left",)
	right: Optional[int] = Field(default=None,alias="right",)
	top: Optional[int] = Field(default=None,alias="top",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


