from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Presence(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	activity: Optional[str] = Field(default=None,alias="activity",)
	availability: Optional[str] = Field(default=None,alias="availability",)
	statusMessage: Optional[PresenceStatusMessage] = Field(default=None,alias="statusMessage",)

from .presence_status_message import PresenceStatusMessage

