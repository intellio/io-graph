from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DatePostRequest(BaseModel):
	year: Optional[str] = Field(alias="year", default=None,)
	month: Optional[str] = Field(alias="month", default=None,)
	day: Optional[str] = Field(alias="day", default=None,)


