from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class ManagedTenantsManagedTenantGenericError(BaseModel):
	error: Optional[str] = Field(alias="error", default=None,)
	tenantId: Optional[str] = Field(alias="tenantId", default=None,)
	odata_type: Literal["#microsoft.graph.managedTenants.managedTenantGenericError"] = Field(alias="@odata.type", default="#microsoft.graph.managedTenants.managedTenantGenericError")

