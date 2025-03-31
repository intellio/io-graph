from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Set_enrollment_time_device_membership_targetPostRequest(BaseModel):
	enrollmentTimeDeviceMembershipTargets: Optional[list[EnrollmentTimeDeviceMembershipTarget]] = Field(alias="enrollmentTimeDeviceMembershipTargets", default=None,)

from .enrollment_time_device_membership_target import EnrollmentTimeDeviceMembershipTarget
