from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class DateTimeColumn(BaseModel):
	displayAs: Optional[str] = Field(default=None,alias="displayAs",)
	format: Optional[str] = Field(default=None,alias="format",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


