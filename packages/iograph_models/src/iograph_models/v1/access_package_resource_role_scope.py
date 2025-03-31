from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class AccessPackageResourceRoleScope(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.accessPackageResourceRoleScope"] = Field(alias="@odata.type",)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	role: Optional[AccessPackageResourceRole] = Field(alias="role", default=None,)
	scope: Optional[AccessPackageResourceScope] = Field(alias="scope", default=None,)

from .access_package_resource_role import AccessPackageResourceRole
from .access_package_resource_scope import AccessPackageResourceScope
