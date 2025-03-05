from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeltaParticipants(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	sequenceNumber: Optional[int] = Field(default=None,alias="sequenceNumber",)
	participants: Optional[list[Participant]] = Field(default=None,alias="participants",)

from .participant import Participant

