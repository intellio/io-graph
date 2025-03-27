from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class MeetingAttendanceReport(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	externalEventInformation: Optional[list[VirtualEventExternalInformation]] = Field(alias="externalEventInformation", default=None,)
	meetingEndDateTime: Optional[datetime] = Field(alias="meetingEndDateTime", default=None,)
	meetingStartDateTime: Optional[datetime] = Field(alias="meetingStartDateTime", default=None,)
	totalParticipantCount: Optional[int] = Field(alias="totalParticipantCount", default=None,)
	attendanceRecords: Optional[list[AttendanceRecord]] = Field(alias="attendanceRecords", default=None,)

from .virtual_event_external_information import VirtualEventExternalInformation
from .attendance_record import AttendanceRecord

