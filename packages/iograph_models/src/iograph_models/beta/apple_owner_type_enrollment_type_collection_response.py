from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AppleOwnerTypeEnrollmentTypeCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[AppleOwnerTypeEnrollmentType]] = Field(alias="value", default=None,)

from .apple_owner_type_enrollment_type import AppleOwnerTypeEnrollmentType

