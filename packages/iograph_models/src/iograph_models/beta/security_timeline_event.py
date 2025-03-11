from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityTimelineEvent(BaseModel):
	eventDateTime: Optional[datetime] = Field(alias="eventDateTime",default=None,)
	eventDetails: Optional[str] = Field(alias="eventDetails",default=None,)
	eventResult: Optional[str] = Field(alias="eventResult",default=None,)
	eventSource: Optional[SecurityEventSource | str] = Field(alias="eventSource",default=None,)
	eventThreats: Optional[list[str]] = Field(alias="eventThreats",default=None,)
	eventType: Optional[SecurityTimelineEventType | str] = Field(alias="eventType",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .security_event_source import SecurityEventSource
from .security_timeline_event_type import SecurityTimelineEventType

