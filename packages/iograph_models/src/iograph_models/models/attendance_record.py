from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AttendanceRecord(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	attendanceIntervals: Optional[list[AttendanceInterval]] = Field(default=None,alias="attendanceIntervals",)
	emailAddress: Optional[str] = Field(default=None,alias="emailAddress",)
	identity: Optional[Identity] = Field(default=None,alias="identity",)
	role: Optional[str] = Field(default=None,alias="role",)
	totalAttendanceInSeconds: Optional[int] = Field(default=None,alias="totalAttendanceInSeconds",)

from .attendance_interval import AttendanceInterval
from .identity import Identity

