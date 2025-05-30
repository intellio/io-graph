from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class MeetingAttendanceReport(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.meetingAttendanceReport"] = Field(alias="@odata.type", default="#microsoft.graph.meetingAttendanceReport")
	meetingEndDateTime: Optional[datetime] = Field(alias="meetingEndDateTime", default=None,)
	meetingStartDateTime: Optional[datetime] = Field(alias="meetingStartDateTime", default=None,)
	totalParticipantCount: Optional[int] = Field(alias="totalParticipantCount", default=None,)
	attendanceRecords: Optional[list[AttendanceRecord]] = Field(alias="attendanceRecords", default=None,)

from .attendance_record import AttendanceRecord
