from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AppliedConditionalAccessPolicyCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[AppliedConditionalAccessPolicy]] = Field(default=None,alias="value",)

from .applied_conditional_access_policy import AppliedConditionalAccessPolicy

