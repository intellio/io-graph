from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ResourceSpecificPermissionGrantCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[ResourceSpecificPermissionGrant] = Field(alias="value",)

from .resource_specific_permission_grant import ResourceSpecificPermissionGrant

