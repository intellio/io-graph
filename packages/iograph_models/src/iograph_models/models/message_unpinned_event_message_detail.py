from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class MessageUnpinnedEventMessageDetail(BaseModel):
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	eventDateTime: Optional[datetime] = Field(default=None,alias="eventDateTime",)
	initiator: Optional[IdentitySet] = Field(default=None,alias="initiator",)

from .identity_set import IdentitySet

