from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CallEndedEventMessageDetail(BaseModel):
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	callDuration: Optional[str] = Field(default=None,alias="callDuration",)
	callEventType: Optional[TeamworkCallEventType] = Field(default=None,alias="callEventType",)
	callId: Optional[str] = Field(default=None,alias="callId",)
	callParticipants: Optional[list[CallParticipantInfo]] = Field(default=None,alias="callParticipants",)
	initiator: Optional[IdentitySet] = Field(default=None,alias="initiator",)

from .teamwork_call_event_type import TeamworkCallEventType
from .call_participant_info import CallParticipantInfo
from .identity_set import IdentitySet

