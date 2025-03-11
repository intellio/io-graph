from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AppliedConditionalAccessPolicyCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[AppliedConditionalAccessPolicy]] = Field(alias="value",default=None,)

from .applied_conditional_access_policy import AppliedConditionalAccessPolicy

