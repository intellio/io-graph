from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CloudCommunications(BaseModel):
	callRecords: Optional[list[CallRecordsCallRecord]] = Field(default=None,alias="callRecords",)
	calls: Optional[list[Call]] = Field(default=None,alias="calls",)
	onlineMeetings: Optional[list[OnlineMeeting]] = Field(default=None,alias="onlineMeetings",)
	presences: Optional[list[Presence]] = Field(default=None,alias="presences",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .call_records_call_record import CallRecordsCallRecord
from .call import Call
from .online_meeting import OnlineMeeting
from .presence import Presence

