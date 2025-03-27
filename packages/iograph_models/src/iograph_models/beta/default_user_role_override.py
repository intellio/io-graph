from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DefaultUserRoleOverride(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	isDefault: Optional[bool] = Field(alias="isDefault", default=None,)
	rolePermissions: Optional[list[UnifiedRolePermission]] = Field(alias="rolePermissions", default=None,)

from .unified_role_permission import UnifiedRolePermission

