from __future__ import annotations
from uuid import UUID
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class CalendarGroup(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.calendarGroup"] = Field(alias="@odata.type",)
	changeKey: Optional[str] = Field(alias="changeKey", default=None,)
	classId: Optional[UUID] = Field(alias="classId", default=None,)
	name: Optional[str] = Field(alias="name", default=None,)
	calendars: Optional[list[Calendar]] = Field(alias="calendars", default=None,)

from .calendar import Calendar
