from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AttendanceRecord(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	attendanceIntervals: Optional[list[AttendanceInterval]] = Field(alias="attendanceIntervals",default=None,)
	emailAddress: Optional[str] = Field(alias="emailAddress",default=None,)
	externalRegistrationInformation: Optional[VirtualEventExternalRegistrationInformation] = Field(alias="externalRegistrationInformation",default=None,)
	identity: SerializeAsAny[Optional[Identity]] = Field(alias="identity",default=None,)
	registrantId: Optional[str] = Field(alias="registrantId",default=None,)
	registrationId: Optional[str] = Field(alias="registrationId",default=None,)
	role: Optional[str] = Field(alias="role",default=None,)
	totalAttendanceInSeconds: Optional[int] = Field(alias="totalAttendanceInSeconds",default=None,)

from .attendance_interval import AttendanceInterval
from .virtual_event_external_registration_information import VirtualEventExternalRegistrationInformation
from .identity import Identity

