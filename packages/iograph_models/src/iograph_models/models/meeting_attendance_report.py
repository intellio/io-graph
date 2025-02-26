from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class MeetingAttendanceReport(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	meetingEndDateTime: Optional[datetime] = Field(default=None,alias="meetingEndDateTime",)
	meetingStartDateTime: Optional[datetime] = Field(default=None,alias="meetingStartDateTime",)
	totalParticipantCount: Optional[int] = Field(default=None,alias="totalParticipantCount",)
	attendanceRecords: list[AttendanceRecord] = Field(alias="attendanceRecords",)

from .attendance_record import AttendanceRecord

