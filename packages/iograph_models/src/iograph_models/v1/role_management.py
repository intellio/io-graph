from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class RoleManagement(BaseModel):
	directory: Optional[RbacApplication] = Field(alias="directory", default=None,)
	entitlementManagement: Optional[RbacApplication] = Field(alias="entitlementManagement", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .rbac_application import RbacApplication
from .rbac_application import RbacApplication

