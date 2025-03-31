from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class TimeCardEntry(BaseModel):
	breaks: Optional[list[TimeCardBreak]] = Field(alias="breaks", default=None,)
	clockInEvent: Optional[TimeCardEvent] = Field(alias="clockInEvent", default=None,)
	clockOutEvent: Optional[TimeCardEvent] = Field(alias="clockOutEvent", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .time_card_break import TimeCardBreak
from .time_card_event import TimeCardEvent
