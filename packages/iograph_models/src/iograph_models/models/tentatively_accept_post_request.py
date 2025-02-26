from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Tentatively_acceptPostRequest(BaseModel):
	ProposedNewTime: Optional[TimeSlot] = Field(default=None,alias="ProposedNewTime",)
	SendResponse: Optional[bool] = Field(default=None,alias="SendResponse",)
	Comment: Optional[str] = Field(default=None,alias="Comment",)

from .time_slot import TimeSlot

