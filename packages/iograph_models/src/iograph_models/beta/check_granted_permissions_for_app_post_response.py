from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Check_granted_permissions_for_appPostResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[ResourceSpecificPermissionGrant]] = Field(alias="value",default=None,)

from .resource_specific_permission_grant import ResourceSpecificPermissionGrant

