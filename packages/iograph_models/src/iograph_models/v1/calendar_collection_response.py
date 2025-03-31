from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CalendarCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Calendar]] = Field(alias="value", default=None,)

from .calendar import Calendar
