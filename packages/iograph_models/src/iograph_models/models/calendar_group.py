from __future__ import annotations
from uuid import UUID
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CalendarGroup(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	changeKey: Optional[str] = Field(default=None,alias="changeKey",)
	classId: Optional[UUID] = Field(default=None,alias="classId",)
	name: Optional[str] = Field(default=None,alias="name",)
	calendars: Optional[list[Calendar]] = Field(default=None,alias="calendars",)

from .calendar import Calendar

