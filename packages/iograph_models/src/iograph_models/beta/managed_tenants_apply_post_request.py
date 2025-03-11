from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Managed_tenants_applyPostRequest(BaseModel):
	tenantId: Optional[str] = Field(alias="tenantId",default=None,)
	tenantGroupId: Optional[str] = Field(alias="tenantGroupId",default=None,)
	managementTemplateId: Optional[str] = Field(alias="managementTemplateId",default=None,)
	includeAllUsers: Optional[bool] = Field(alias="includeAllUsers",default=None,)
	includeGroups: Optional[list[str]] = Field(alias="includeGroups",default=None,)
	excludeGroups: Optional[list[str]] = Field(alias="excludeGroups",default=None,)


