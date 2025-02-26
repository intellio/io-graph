from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class AccessPackageResourceRoleScope(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	role: Optional[AccessPackageResourceRole] = Field(default=None,alias="role",)
	scope: Optional[AccessPackageResourceScope] = Field(default=None,alias="scope",)

from .access_package_resource_role import AccessPackageResourceRole
from .access_package_resource_scope import AccessPackageResourceScope

