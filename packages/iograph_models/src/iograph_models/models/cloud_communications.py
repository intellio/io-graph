from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CloudCommunications(BaseModel):
	callRecords: list[CallRecordsCallRecord] = Field(alias="callRecords",)
	calls: list[Call] = Field(alias="calls",)
	onlineMeetings: list[OnlineMeeting] = Field(alias="onlineMeetings",)
	presences: list[Presence] = Field(alias="presences",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .call_records_call_record import CallRecordsCallRecord
from .call import Call
from .online_meeting import OnlineMeeting
from .presence import Presence

