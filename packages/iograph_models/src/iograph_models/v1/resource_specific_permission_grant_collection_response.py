from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ResourceSpecificPermissionGrantCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[ResourceSpecificPermissionGrant]] = Field(alias="value", default=None,)

from .resource_specific_permission_grant import ResourceSpecificPermissionGrant

