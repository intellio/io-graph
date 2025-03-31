from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class AzureActiveDirectoryTenant(BaseModel):
	odata_type: Literal["#microsoft.graph.azureActiveDirectoryTenant"] = Field(alias="@odata.type", default="#microsoft.graph.azureActiveDirectoryTenant")
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	tenantId: Optional[str] = Field(alias="tenantId", default=None,)

