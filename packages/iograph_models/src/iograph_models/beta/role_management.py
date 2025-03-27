from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class RoleManagement(BaseModel):
	cloudPC: Optional[RbacApplicationMultiple] = Field(alias="cloudPC", default=None,)
	defender: Optional[RbacApplicationMultiple] = Field(alias="defender", default=None,)
	deviceManagement: Optional[RbacApplicationMultiple] = Field(alias="deviceManagement", default=None,)
	directory: Optional[RbacApplication] = Field(alias="directory", default=None,)
	enterpriseApps: Optional[list[RbacApplication]] = Field(alias="enterpriseApps", default=None,)
	entitlementManagement: Optional[RbacApplication] = Field(alias="entitlementManagement", default=None,)
	exchange: Optional[UnifiedRbacApplication] = Field(alias="exchange", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .rbac_application_multiple import RbacApplicationMultiple
from .rbac_application_multiple import RbacApplicationMultiple
from .rbac_application_multiple import RbacApplicationMultiple
from .rbac_application import RbacApplication
from .rbac_application import RbacApplication
from .rbac_application import RbacApplication
from .unified_rbac_application import UnifiedRbacApplication

