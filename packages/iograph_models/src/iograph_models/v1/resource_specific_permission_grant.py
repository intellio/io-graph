from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class ResourceSpecificPermissionGrant(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.resourceSpecificPermissionGrant"] = Field(alias="@odata.type", default="#microsoft.graph.resourceSpecificPermissionGrant")
	deletedDateTime: Optional[datetime] = Field(alias="deletedDateTime", default=None,)
	clientAppId: Optional[str] = Field(alias="clientAppId", default=None,)
	clientId: Optional[str] = Field(alias="clientId", default=None,)
	permission: Optional[str] = Field(alias="permission", default=None,)
	permissionType: Optional[str] = Field(alias="permissionType", default=None,)
	resourceAppId: Optional[str] = Field(alias="resourceAppId", default=None,)

