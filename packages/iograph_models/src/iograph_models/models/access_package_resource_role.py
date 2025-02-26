from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AccessPackageResourceRole(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	originId: Optional[str] = Field(default=None,alias="originId",)
	originSystem: Optional[str] = Field(default=None,alias="originSystem",)
	resource: Optional[AccessPackageResource] = Field(default=None,alias="resource",)

from .access_package_resource import AccessPackageResource

