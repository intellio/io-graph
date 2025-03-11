from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class EnrollmentTimeDeviceMembershipTargetStatus(BaseModel):
	targetId: Optional[str] = Field(alias="targetId",default=None,)
	targetValidationErrorCode: Optional[EnrollmentTimeDeviceMembershipTargetValidationErrorCode | str] = Field(alias="targetValidationErrorCode",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .enrollment_time_device_membership_target_validation_error_code import EnrollmentTimeDeviceMembershipTargetValidationErrorCode

