from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ConditionalAccessPolicyCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[ConditionalAccessPolicy] = Field(alias="value",)

from .conditional_access_policy import ConditionalAccessPolicy

