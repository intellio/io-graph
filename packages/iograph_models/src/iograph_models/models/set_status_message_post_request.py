from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Set_status_messagePostRequest(BaseModel):
	statusMessage: Optional[PresenceStatusMessage] = Field(default=None,alias="statusMessage",)

from .presence_status_message import PresenceStatusMessage

