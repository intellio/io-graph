from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ManagedTenantsTenantGroup(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	allTenantsIncluded: Optional[bool] = Field(alias="allTenantsIncluded", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	managementActions: Optional[list[ManagedTenantsManagementActionInfo]] = Field(alias="managementActions", default=None,)
	managementIntents: Optional[list[ManagedTenantsManagementIntentInfo]] = Field(alias="managementIntents", default=None,)
	tenantIds: Optional[list[str]] = Field(alias="tenantIds", default=None,)

from .managed_tenants_management_action_info import ManagedTenantsManagementActionInfo
from .managed_tenants_management_intent_info import ManagedTenantsManagementIntentInfo

