from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CalendarGroupCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[CalendarGroup]] = Field(alias="value", default=None,)

from .calendar_group import CalendarGroup
