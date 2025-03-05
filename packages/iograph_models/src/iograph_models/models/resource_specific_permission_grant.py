from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ResourceSpecificPermissionGrant(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	deletedDateTime: Optional[datetime] = Field(default=None,alias="deletedDateTime",)
	clientAppId: Optional[str] = Field(default=None,alias="clientAppId",)
	clientId: Optional[str] = Field(default=None,alias="clientId",)
	permission: Optional[str] = Field(default=None,alias="permission",)
	permissionType: Optional[str] = Field(default=None,alias="permissionType",)
	resourceAppId: Optional[str] = Field(default=None,alias="resourceAppId",)


