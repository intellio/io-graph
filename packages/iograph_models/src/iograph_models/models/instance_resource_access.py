from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class InstanceResourceAccess(BaseModel):
	permissions: Optional[list[ResourcePermission]] = Field(default=None,alias="permissions",)
	resourceAppId: Optional[str] = Field(default=None,alias="resourceAppId",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .resource_permission import ResourcePermission

