from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CloudCommunications(BaseModel):
	callRecords: Optional[list[CallRecordsCallRecord]] = Field(alias="callRecords", default=None,)
	calls: Optional[list[Call]] = Field(alias="calls", default=None,)
	onlineMeetings: Optional[list[OnlineMeeting]] = Field(alias="onlineMeetings", default=None,)
	presences: Optional[list[Presence]] = Field(alias="presences", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .call_records_call_record import CallRecordsCallRecord
from .call import Call
from .online_meeting import OnlineMeeting
from .presence import Presence
