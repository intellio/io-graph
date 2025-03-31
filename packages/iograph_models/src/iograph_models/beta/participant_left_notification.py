from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class ParticipantLeftNotification(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.participantLeftNotification"] = Field(alias="@odata.type",)
	participantId: Optional[str] = Field(alias="participantId", default=None,)
	call: Optional[Call] = Field(alias="call", default=None,)

from .call import Call
