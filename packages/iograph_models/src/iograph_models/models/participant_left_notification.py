from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ParticipantLeftNotification(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	participantId: Optional[str] = Field(default=None,alias="participantId",)
	call: Optional[Call] = Field(default=None,alias="call",)

from .call import Call

