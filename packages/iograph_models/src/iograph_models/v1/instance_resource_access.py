from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class InstanceResourceAccess(BaseModel):
	permissions: Optional[list[ResourcePermission]] = Field(alias="permissions",default=None,)
	resourceAppId: Optional[str] = Field(alias="resourceAppId",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .resource_permission import ResourcePermission

