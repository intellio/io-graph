from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class TimeCardEntry(BaseModel):
	breaks: list[TimeCardBreak] = Field(alias="breaks",)
	clockInEvent: Optional[TimeCardEvent] = Field(default=None,alias="clockInEvent",)
	clockOutEvent: Optional[TimeCardEvent] = Field(default=None,alias="clockOutEvent",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .time_card_break import TimeCardBreak
from .time_card_event import TimeCardEvent
from .time_card_event import TimeCardEvent

