from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AccessPackageResourceRoleScopeCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[AccessPackageResourceRoleScope]] = Field(default=None,alias="value",)

from .access_package_resource_role_scope import AccessPackageResourceRoleScope

