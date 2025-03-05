from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AttendanceRecord(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	attendanceIntervals: Optional[list[AttendanceInterval]] = Field(alias="attendanceIntervals",default=None,)
	emailAddress: Optional[str] = Field(alias="emailAddress",default=None,)
	identity: SerializeAsAny[Optional[Identity]] = Field(alias="identity",default=None,)
	role: Optional[str] = Field(alias="role",default=None,)
	totalAttendanceInSeconds: Optional[int] = Field(alias="totalAttendanceInSeconds",default=None,)

from .attendance_interval import AttendanceInterval
from .identity import Identity

