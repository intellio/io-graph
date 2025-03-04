from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Get_effective_permissionsGetResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[RolePermission]] = Field(default=None,alias="value",)

from .role_permission import RolePermission

