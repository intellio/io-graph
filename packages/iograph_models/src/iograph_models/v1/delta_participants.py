from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class DeltaParticipants(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.deltaParticipants"] = Field(alias="@odata.type", default="#microsoft.graph.deltaParticipants")
	sequenceNumber: Optional[int] = Field(alias="sequenceNumber", default=None,)
	participants: Optional[list[Participant]] = Field(alias="participants", default=None,)

from .participant import Participant
