from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CallStartedEventMessageDetail(BaseModel):
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	callEventType: Optional[TeamworkCallEventType] = Field(default=None,alias="callEventType",)
	callId: Optional[str] = Field(default=None,alias="callId",)
	initiator: Optional[IdentitySet] = Field(default=None,alias="initiator",)

from .teamwork_call_event_type import TeamworkCallEventType
from .identity_set import IdentitySet

