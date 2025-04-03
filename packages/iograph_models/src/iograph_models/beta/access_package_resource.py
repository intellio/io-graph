from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class AccessPackageResource(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.accessPackageResource"] = Field(alias="@odata.type", default="#microsoft.graph.accessPackageResource")
	addedBy: Optional[str] = Field(alias="addedBy", default=None,)
	addedOn: Optional[datetime] = Field(alias="addedOn", default=None,)
	attributes: Optional[list[AccessPackageResourceAttribute]] = Field(alias="attributes", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	isPendingOnboarding: Optional[bool] = Field(alias="isPendingOnboarding", default=None,)
	originId: Optional[str] = Field(alias="originId", default=None,)
	originSystem: Optional[str] = Field(alias="originSystem", default=None,)
	resourceType: Optional[str] = Field(alias="resourceType", default=None,)
	url: Optional[str] = Field(alias="url", default=None,)
	accessPackageResourceEnvironment: Optional[AccessPackageResourceEnvironment] = Field(alias="accessPackageResourceEnvironment", default=None,)
	accessPackageResourceRoles: Optional[list[AccessPackageResourceRole]] = Field(alias="accessPackageResourceRoles", default=None,)
	accessPackageResourceScopes: Optional[list[AccessPackageResourceScope]] = Field(alias="accessPackageResourceScopes", default=None,)

from .access_package_resource_attribute import AccessPackageResourceAttribute
from .access_package_resource_environment import AccessPackageResourceEnvironment
from .access_package_resource_role import AccessPackageResourceRole
from .access_package_resource_scope import AccessPackageResourceScope
