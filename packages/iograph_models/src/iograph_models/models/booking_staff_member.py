from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class BookingStaffMember(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	availabilityIsAffectedByPersonalCalendar: Optional[bool] = Field(default=None,alias="availabilityIsAffectedByPersonalCalendar",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	emailAddress: Optional[str] = Field(default=None,alias="emailAddress",)
	isEmailNotificationEnabled: Optional[bool] = Field(default=None,alias="isEmailNotificationEnabled",)
	lastUpdatedDateTime: Optional[datetime] = Field(default=None,alias="lastUpdatedDateTime",)
	membershipStatus: Optional[BookingStaffMembershipStatus] = Field(default=None,alias="membershipStatus",)
	role: Optional[BookingStaffRole] = Field(default=None,alias="role",)
	timeZone: Optional[str] = Field(default=None,alias="timeZone",)
	useBusinessHours: Optional[bool] = Field(default=None,alias="useBusinessHours",)
	workingHours: list[BookingWorkHours] = Field(alias="workingHours",)

from .booking_staff_membership_status import BookingStaffMembershipStatus
from .booking_staff_role import BookingStaffRole
from .booking_work_hours import BookingWorkHours

