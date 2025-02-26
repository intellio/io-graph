from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class DateTimeTimeZone(BaseModel):
	dateTime: Optional[str] = Field(default=None,alias="dateTime",)
	timeZone: Optional[str] = Field(default=None,alias="timeZone",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


