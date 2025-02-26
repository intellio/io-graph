from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class AccessPackageResource(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	attributes: list[AccessPackageResourceAttribute] = Field(alias="attributes",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	modifiedDateTime: Optional[datetime] = Field(default=None,alias="modifiedDateTime",)
	originId: Optional[str] = Field(default=None,alias="originId",)
	originSystem: Optional[str] = Field(default=None,alias="originSystem",)
	environment: Optional[AccessPackageResourceEnvironment] = Field(default=None,alias="environment",)
	roles: list[AccessPackageResourceRole] = Field(alias="roles",)
	scopes: list[AccessPackageResourceScope] = Field(alias="scopes",)

from .access_package_resource_attribute import AccessPackageResourceAttribute
from .access_package_resource_environment import AccessPackageResourceEnvironment
from .access_package_resource_role import AccessPackageResourceRole
from .access_package_resource_scope import AccessPackageResourceScope

