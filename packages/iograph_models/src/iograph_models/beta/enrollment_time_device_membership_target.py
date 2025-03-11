from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class EnrollmentTimeDeviceMembershipTarget(BaseModel):
	targetId: Optional[str] = Field(alias="targetId",default=None,)
	targetType: Optional[EnrollmentTimeDeviceMembershipTargetType | str] = Field(alias="targetType",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .enrollment_time_device_membership_target_type import EnrollmentTimeDeviceMembershipTargetType

