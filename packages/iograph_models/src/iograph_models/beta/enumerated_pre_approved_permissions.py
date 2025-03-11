from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class EnumeratedPreApprovedPermissions(BaseModel):
	permissionKind: Optional[PermissionKind | str] = Field(alias="permissionKind",default=None,)
	permissionType: Optional[PermissionType | str] = Field(alias="permissionType",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	permissionIds: Optional[list[str]] = Field(alias="permissionIds",default=None,)
	resourceApplicationId: Optional[str] = Field(alias="resourceApplicationId",default=None,)

from .permission_kind import PermissionKind
from .permission_type import PermissionType

