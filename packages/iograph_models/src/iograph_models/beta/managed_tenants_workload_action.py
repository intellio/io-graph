from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ManagedTenantsWorkloadAction(BaseModel):
	actionId: Optional[str] = Field(alias="actionId", default=None,)
	category: Optional[ManagedTenantsWorkloadActionCategory | str] = Field(alias="category", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	licenses: Optional[list[str]] = Field(alias="licenses", default=None,)
	service: Optional[str] = Field(alias="service", default=None,)
	settings: Optional[list[ManagedTenantsSetting]] = Field(alias="settings", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .managed_tenants_workload_action_category import ManagedTenantsWorkloadActionCategory
from .managed_tenants_setting import ManagedTenantsSetting

