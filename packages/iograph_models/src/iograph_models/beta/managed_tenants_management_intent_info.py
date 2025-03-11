from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ManagedTenantsManagementIntentInfo(BaseModel):
	managementIntentDisplayName: Optional[str] = Field(alias="managementIntentDisplayName",default=None,)
	managementIntentId: Optional[str] = Field(alias="managementIntentId",default=None,)
	managementTemplates: Optional[list[ManagedTenantsManagementTemplateDetailedInfo]] = Field(alias="managementTemplates",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .managed_tenants_management_template_detailed_info import ManagedTenantsManagementTemplateDetailedInfo

