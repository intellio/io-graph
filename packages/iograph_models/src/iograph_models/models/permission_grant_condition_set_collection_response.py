from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class PermissionGrantConditionSetCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[PermissionGrantConditionSet] = Field(alias="value",)

from .permission_grant_condition_set import PermissionGrantConditionSet

