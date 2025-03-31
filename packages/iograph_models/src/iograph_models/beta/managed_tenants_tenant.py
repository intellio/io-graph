from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class ManagedTenantsTenant(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.managedTenants.tenant"] = Field(alias="@odata.type",)
	contract: Optional[ManagedTenantsTenantContract] = Field(alias="contract", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	lastUpdatedDateTime: Optional[datetime] = Field(alias="lastUpdatedDateTime", default=None,)
	tenantId: Optional[str] = Field(alias="tenantId", default=None,)
	tenantStatusInformation: Optional[ManagedTenantsTenantStatusInformation] = Field(alias="tenantStatusInformation", default=None,)

from .managed_tenants_tenant_contract import ManagedTenantsTenantContract
from .managed_tenants_tenant_status_information import ManagedTenantsTenantStatusInformation
