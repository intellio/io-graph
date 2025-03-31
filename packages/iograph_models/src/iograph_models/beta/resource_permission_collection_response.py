from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ResourcePermissionCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[ResourcePermission]] = Field(alias="value", default=None,)

from .resource_permission import ResourcePermission
