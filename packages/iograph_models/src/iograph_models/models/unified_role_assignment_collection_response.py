from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class UnifiedRoleAssignmentCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[UnifiedRoleAssignment] = Field(alias="value",)

from .unified_role_assignment import UnifiedRoleAssignment

