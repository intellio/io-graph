from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class OpenShiftItem(BaseModel):
	endDateTime: Optional[datetime] = Field(alias="endDateTime", default=None,)
	startDateTime: Optional[datetime] = Field(alias="startDateTime", default=None,)
	theme: Optional[ScheduleEntityTheme | str] = Field(alias="theme", default=None,)
	odata_type: Literal["#microsoft.graph.openShiftItem"] = Field(alias="@odata.type", default="#microsoft.graph.openShiftItem")
	activities: Optional[list[ShiftActivity]] = Field(alias="activities", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	notes: Optional[str] = Field(alias="notes", default=None,)
	openSlotCount: Optional[int] = Field(alias="openSlotCount", default=None,)

from .schedule_entity_theme import ScheduleEntityTheme
from .shift_activity import ShiftActivity

