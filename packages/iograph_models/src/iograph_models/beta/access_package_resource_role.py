from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class AccessPackageResourceRole(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.accessPackageResourceRole"] = Field(alias="@odata.type", default="#microsoft.graph.accessPackageResourceRole")
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	originId: Optional[str] = Field(alias="originId", default=None,)
	originSystem: Optional[str] = Field(alias="originSystem", default=None,)
	accessPackageResource: Optional[AccessPackageResource] = Field(alias="accessPackageResource", default=None,)

from .access_package_resource import AccessPackageResource
