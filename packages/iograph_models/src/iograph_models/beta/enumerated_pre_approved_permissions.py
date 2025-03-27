from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class EnumeratedPreApprovedPermissions(BaseModel):
	permissionKind: Optional[PermissionKind | str] = Field(alias="permissionKind", default=None,)
	permissionType: Optional[PermissionType | str] = Field(alias="permissionType", default=None,)
	odata_type: Literal["#microsoft.graph.enumeratedPreApprovedPermissions"] = Field(alias="@odata.type", default="#microsoft.graph.enumeratedPreApprovedPermissions")
	permissionIds: Optional[list[str]] = Field(alias="permissionIds", default=None,)
	resourceApplicationId: Optional[str] = Field(alias="resourceApplicationId", default=None,)

from .permission_kind import PermissionKind
from .permission_type import PermissionType

