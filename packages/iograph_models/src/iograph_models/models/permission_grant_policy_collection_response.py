from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class PermissionGrantPolicyCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[PermissionGrantPolicy] = Field(alias="value",)

from .permission_grant_policy import PermissionGrantPolicy

