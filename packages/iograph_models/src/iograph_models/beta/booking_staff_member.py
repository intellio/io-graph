from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class BookingStaffMember(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.bookingStaffMember"] = Field(alias="@odata.type", default="#microsoft.graph.bookingStaffMember")
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	emailAddress: Optional[str] = Field(alias="emailAddress", default=None,)
	availabilityIsAffectedByPersonalCalendar: Optional[bool] = Field(alias="availabilityIsAffectedByPersonalCalendar", default=None,)
	colorIndex: Optional[int] = Field(alias="colorIndex", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	isEmailNotificationEnabled: Optional[bool] = Field(alias="isEmailNotificationEnabled", default=None,)
	lastUpdatedDateTime: Optional[datetime] = Field(alias="lastUpdatedDateTime", default=None,)
	membershipStatus: Optional[BookingStaffMembershipStatus | str] = Field(alias="membershipStatus", default=None,)
	role: Optional[BookingStaffRole | str] = Field(alias="role", default=None,)
	timeZone: Optional[str] = Field(alias="timeZone", default=None,)
	useBusinessHours: Optional[bool] = Field(alias="useBusinessHours", default=None,)
	workingHours: Optional[list[BookingWorkHours]] = Field(alias="workingHours", default=None,)

from .booking_staff_membership_status import BookingStaffMembershipStatus
from .booking_staff_role import BookingStaffRole
from .booking_work_hours import BookingWorkHours
