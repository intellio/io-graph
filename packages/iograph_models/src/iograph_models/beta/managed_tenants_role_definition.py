from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ManagedTenantsRoleDefinition(BaseModel):
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	templateId: Optional[str] = Field(alias="templateId", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

