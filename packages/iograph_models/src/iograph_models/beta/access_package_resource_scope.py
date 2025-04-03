from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class AccessPackageResourceScope(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.accessPackageResourceScope"] = Field(alias="@odata.type", default="#microsoft.graph.accessPackageResourceScope")
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	isRootScope: Optional[bool] = Field(alias="isRootScope", default=None,)
	originId: Optional[str] = Field(alias="originId", default=None,)
	originSystem: Optional[str] = Field(alias="originSystem", default=None,)
	roleOriginId: Optional[str] = Field(alias="roleOriginId", default=None,)
	url: Optional[str] = Field(alias="url", default=None,)
	accessPackageResource: Optional[AccessPackageResource] = Field(alias="accessPackageResource", default=None,)

from .access_package_resource import AccessPackageResource
