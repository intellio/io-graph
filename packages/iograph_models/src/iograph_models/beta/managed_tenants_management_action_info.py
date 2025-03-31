from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ManagedTenantsManagementActionInfo(BaseModel):
	managementActionId: Optional[str] = Field(alias="managementActionId", default=None,)
	managementTemplateId: Optional[str] = Field(alias="managementTemplateId", default=None,)
	managementTemplateVersion: Optional[int] = Field(alias="managementTemplateVersion", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

