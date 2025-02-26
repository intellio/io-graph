from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class RoleAssignmentCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[RoleAssignment] = Field(alias="value",)

from .role_assignment import RoleAssignment

