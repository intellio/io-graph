from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class DefaultUserRoleOverride(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.defaultUserRoleOverride"] = Field(alias="@odata.type", default="#microsoft.graph.defaultUserRoleOverride")
	isDefault: Optional[bool] = Field(alias="isDefault", default=None,)
	rolePermissions: Optional[list[UnifiedRolePermission]] = Field(alias="rolePermissions", default=None,)

from .unified_role_permission import UnifiedRolePermission
