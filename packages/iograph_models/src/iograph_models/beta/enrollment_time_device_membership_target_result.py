from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class EnrollmentTimeDeviceMembershipTargetResult(BaseModel):
	enrollmentTimeDeviceMembershipTargetValidationStatuses: Optional[list[EnrollmentTimeDeviceMembershipTargetStatus]] = Field(alias="enrollmentTimeDeviceMembershipTargetValidationStatuses",default=None,)
	validationSucceeded: Optional[bool] = Field(alias="validationSucceeded",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .enrollment_time_device_membership_target_status import EnrollmentTimeDeviceMembershipTargetStatus

