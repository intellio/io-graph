from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class AccessPackageResource(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	attributes: Optional[list[AccessPackageResourceAttribute]] = Field(alias="attributes",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	modifiedDateTime: Optional[datetime] = Field(alias="modifiedDateTime",default=None,)
	originId: Optional[str] = Field(alias="originId",default=None,)
	originSystem: Optional[str] = Field(alias="originSystem",default=None,)
	environment: Optional[AccessPackageResourceEnvironment] = Field(alias="environment",default=None,)
	roles: Optional[list[AccessPackageResourceRole]] = Field(alias="roles",default=None,)
	scopes: Optional[list[AccessPackageResourceScope]] = Field(alias="scopes",default=None,)

from .access_package_resource_attribute import AccessPackageResourceAttribute
from .access_package_resource_environment import AccessPackageResourceEnvironment
from .access_package_resource_role import AccessPackageResourceRole
from .access_package_resource_scope import AccessPackageResourceScope

