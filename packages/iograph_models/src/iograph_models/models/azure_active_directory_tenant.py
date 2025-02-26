from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AzureActiveDirectoryTenant(BaseModel):
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	tenantId: Optional[str] = Field(default=None,alias="tenantId",)


