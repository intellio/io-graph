from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class TimeCardBreak(BaseModel):
	breakId: Optional[str] = Field(alias="breakId", default=None,)
	end: Optional[TimeCardEvent] = Field(alias="end", default=None,)
	notes: Optional[ItemBody] = Field(alias="notes", default=None,)
	start: Optional[TimeCardEvent] = Field(alias="start", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .time_card_event import TimeCardEvent
from .item_body import ItemBody
from .time_card_event import TimeCardEvent

