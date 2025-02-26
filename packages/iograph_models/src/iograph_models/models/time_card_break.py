from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class TimeCardBreak(BaseModel):
	breakId: Optional[str] = Field(default=None,alias="breakId",)
	end: Optional[TimeCardEvent] = Field(default=None,alias="end",)
	notes: Optional[ItemBody] = Field(default=None,alias="notes",)
	start: Optional[TimeCardEvent] = Field(default=None,alias="start",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .time_card_event import TimeCardEvent
from .item_body import ItemBody
from .time_card_event import TimeCardEvent

