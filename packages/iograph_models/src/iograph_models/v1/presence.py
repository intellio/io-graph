from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Presence(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	activity: Optional[str] = Field(alias="activity", default=None,)
	availability: Optional[str] = Field(alias="availability", default=None,)
	statusMessage: Optional[PresenceStatusMessage] = Field(alias="statusMessage", default=None,)

from .presence_status_message import PresenceStatusMessage

