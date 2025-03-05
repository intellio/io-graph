from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DatePostRequest(BaseModel):
	year: Optional[str] = Field(default=None,alias="year",)
	month: Optional[str] = Field(default=None,alias="month",)
	day: Optional[str] = Field(default=None,alias="day",)


