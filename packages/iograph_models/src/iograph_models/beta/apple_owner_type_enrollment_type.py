from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AppleOwnerTypeEnrollmentType(BaseModel):
	enrollmentType: Optional[AppleUserInitiatedEnrollmentType | str] = Field(alias="enrollmentType", default=None,)
	ownerType: Optional[ManagedDeviceOwnerType | str] = Field(alias="ownerType", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .apple_user_initiated_enrollment_type import AppleUserInitiatedEnrollmentType
from .managed_device_owner_type import ManagedDeviceOwnerType

