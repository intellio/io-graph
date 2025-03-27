from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DepMacOSEnrollmentProfileCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[DepMacOSEnrollmentProfile]] = Field(alias="value", default=None,)

from .dep_mac_o_s_enrollment_profile import DepMacOSEnrollmentProfile

