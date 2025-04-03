from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class ManagedTenantsCloudPcConnection(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.managedTenants.cloudPcConnection"] = Field(alias="@odata.type", default="#microsoft.graph.managedTenants.cloudPcConnection")
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	healthCheckStatus: Optional[str] = Field(alias="healthCheckStatus", default=None,)
	lastRefreshedDateTime: Optional[datetime] = Field(alias="lastRefreshedDateTime", default=None,)
	tenantDisplayName: Optional[str] = Field(alias="tenantDisplayName", default=None,)
	tenantId: Optional[str] = Field(alias="tenantId", default=None,)

