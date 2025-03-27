from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ParticipantLeftNotification(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	participantId: Optional[str] = Field(alias="participantId", default=None,)
	call: Optional[Call] = Field(alias="call", default=None,)

from .call import Call

