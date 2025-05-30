from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class AccessPackageResourceRoleScope(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.accessPackageResourceRoleScope"] = Field(alias="@odata.type", default="#microsoft.graph.accessPackageResourceRoleScope")
	createdBy: Optional[str] = Field(alias="createdBy", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	modifiedBy: Optional[str] = Field(alias="modifiedBy", default=None,)
	modifiedDateTime: Optional[datetime] = Field(alias="modifiedDateTime", default=None,)
	accessPackageResourceRole: Optional[AccessPackageResourceRole] = Field(alias="accessPackageResourceRole", default=None,)
	accessPackageResourceScope: Optional[AccessPackageResourceScope] = Field(alias="accessPackageResourceScope", default=None,)

from .access_package_resource_role import AccessPackageResourceRole
from .access_package_resource_scope import AccessPackageResourceScope
