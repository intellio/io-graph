from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AccessPackageResourceRoleCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[AccessPackageResourceRole] = Field(alias="value",)

from .access_package_resource_role import AccessPackageResourceRole

