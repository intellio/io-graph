from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class RoleManagement(BaseModel):
	directory: Optional[RbacApplication] = Field(default=None,alias="directory",)
	entitlementManagement: Optional[RbacApplication] = Field(default=None,alias="entitlementManagement",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .rbac_application import RbacApplication
from .rbac_application import RbacApplication

