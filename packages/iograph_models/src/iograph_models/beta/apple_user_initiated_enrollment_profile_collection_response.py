from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AppleUserInitiatedEnrollmentProfileCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[AppleUserInitiatedEnrollmentProfile]] = Field(alias="value", default=None,)

from .apple_user_initiated_enrollment_profile import AppleUserInitiatedEnrollmentProfile
