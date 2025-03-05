from __future__ import annotations
from uuid import UUID
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CalendarGroup(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	changeKey: Optional[str] = Field(alias="changeKey",default=None,)
	classId: Optional[UUID] = Field(alias="classId",default=None,)
	name: Optional[str] = Field(alias="name",default=None,)
	calendars: Optional[list[Calendar]] = Field(alias="calendars",default=None,)

from .calendar import Calendar

