from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AndroidForWorkEnrollmentProfileCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[AndroidForWorkEnrollmentProfile]] = Field(alias="value",default=None,)

from .android_for_work_enrollment_profile import AndroidForWorkEnrollmentProfile

