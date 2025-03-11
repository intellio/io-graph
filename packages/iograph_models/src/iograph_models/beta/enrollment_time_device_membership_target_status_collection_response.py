from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class EnrollmentTimeDeviceMembershipTargetStatusCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[EnrollmentTimeDeviceMembershipTargetStatus]] = Field(alias="value",default=None,)

from .enrollment_time_device_membership_target_status import EnrollmentTimeDeviceMembershipTargetStatus

