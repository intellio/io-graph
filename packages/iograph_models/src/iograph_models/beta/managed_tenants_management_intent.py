from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ManagedTenantsManagementIntent(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	isGlobal: Optional[bool] = Field(alias="isGlobal", default=None,)
	managementTemplates: Optional[list[ManagedTenantsManagementTemplateDetailedInfo]] = Field(alias="managementTemplates", default=None,)

from .managed_tenants_management_template_detailed_info import ManagedTenantsManagementTemplateDetailedInfo

