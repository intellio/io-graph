from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AppleEnrollmentProfileAssignmentCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[AppleEnrollmentProfileAssignment]] = Field(alias="value", default=None,)

from .apple_enrollment_profile_assignment import AppleEnrollmentProfileAssignment
