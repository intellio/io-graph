from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CallStartedEventMessageDetail(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	callEventType: Optional[str | TeamworkCallEventType] = Field(alias="callEventType",default=None,)
	callId: Optional[str] = Field(alias="callId",default=None,)
	initiator: SerializeAsAny[Optional[IdentitySet]] = Field(alias="initiator",default=None,)

from .teamwork_call_event_type import TeamworkCallEventType
from .identity_set import IdentitySet

