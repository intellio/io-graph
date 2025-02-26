from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AppRoleAssignmentCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[AppRoleAssignment] = Field(alias="value",)

from .app_role_assignment import AppRoleAssignment

