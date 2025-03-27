from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeclinePostRequest(BaseModel):
	ProposedNewTime: Optional[TimeSlot] = Field(alias="ProposedNewTime", default=None,)
	SendResponse: Optional[bool] = Field(alias="SendResponse", default=None,)
	Comment: Optional[str] = Field(alias="Comment", default=None,)

from .time_slot import TimeSlot

