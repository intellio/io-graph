from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class DeltaParticipants(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	sequenceNumber: Optional[int] = Field(default=None,alias="sequenceNumber",)
	participants: list[Participant] = Field(alias="participants",)

from .participant import Participant

