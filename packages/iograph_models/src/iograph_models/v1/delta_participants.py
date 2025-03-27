from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeltaParticipants(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	sequenceNumber: Optional[int] = Field(alias="sequenceNumber", default=None,)
	participants: Optional[list[Participant]] = Field(alias="participants", default=None,)

from .participant import Participant

