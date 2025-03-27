from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class AppleUserInitiatedEnrollmentProfile(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	availableEnrollmentTypeOptions: Optional[list[AppleOwnerTypeEnrollmentType]] = Field(alias="availableEnrollmentTypeOptions", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	defaultEnrollmentType: Optional[AppleUserInitiatedEnrollmentType | str] = Field(alias="defaultEnrollmentType", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	platform: Optional[DevicePlatformType | str] = Field(alias="platform", default=None,)
	priority: Optional[int] = Field(alias="priority", default=None,)
	assignments: Optional[list[AppleEnrollmentProfileAssignment]] = Field(alias="assignments", default=None,)

from .apple_owner_type_enrollment_type import AppleOwnerTypeEnrollmentType
from .apple_user_initiated_enrollment_type import AppleUserInitiatedEnrollmentType
from .device_platform_type import DevicePlatformType
from .apple_enrollment_profile_assignment import AppleEnrollmentProfileAssignment

