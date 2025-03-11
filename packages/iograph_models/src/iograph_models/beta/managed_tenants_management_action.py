from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ManagedTenantsManagementAction(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	category: Optional[ManagedTenantsManagementCategory | str] = Field(alias="category",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	referenceTemplateId: Optional[str] = Field(alias="referenceTemplateId",default=None,)
	referenceTemplateVersion: Optional[int] = Field(alias="referenceTemplateVersion",default=None,)
	workloadActions: Optional[list[ManagedTenantsWorkloadAction]] = Field(alias="workloadActions",default=None,)

from .managed_tenants_management_category import ManagedTenantsManagementCategory
from .managed_tenants_workload_action import ManagedTenantsWorkloadAction

