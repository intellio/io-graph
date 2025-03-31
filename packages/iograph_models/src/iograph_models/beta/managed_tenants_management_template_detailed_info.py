from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ManagedTenantsManagementTemplateDetailedInfo(BaseModel):
	category: Optional[ManagedTenantsManagementCategory | str] = Field(alias="category", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	managementTemplateId: Optional[str] = Field(alias="managementTemplateId", default=None,)
	version: Optional[int] = Field(alias="version", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .managed_tenants_management_category import ManagedTenantsManagementCategory
