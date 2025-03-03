from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Check_granted_permissions_for_appPostResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[ResourceSpecificPermissionGrant]] = Field(default=None,alias="value",)

from .resource_specific_permission_grant import ResourceSpecificPermissionGrant

