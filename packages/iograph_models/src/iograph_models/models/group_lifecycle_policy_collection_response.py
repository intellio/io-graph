from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class GroupLifecyclePolicyCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[GroupLifecyclePolicy] = Field(alias="value",)

from .group_lifecycle_policy import GroupLifecyclePolicy

