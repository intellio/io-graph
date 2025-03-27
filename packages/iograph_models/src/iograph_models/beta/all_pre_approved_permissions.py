from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class AllPreApprovedPermissions(BaseModel):
	permissionKind: Optional[PermissionKind | str] = Field(alias="permissionKind", default=None,)
	permissionType: Optional[PermissionType | str] = Field(alias="permissionType", default=None,)
	odata_type: Literal["#microsoft.graph.allPreApprovedPermissions"] = Field(alias="@odata.type", default="#microsoft.graph.allPreApprovedPermissions")

from .permission_kind import PermissionKind
from .permission_type import PermissionType

