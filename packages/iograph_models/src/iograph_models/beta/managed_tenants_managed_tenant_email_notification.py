from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class ManagedTenantsManagedTenantEmailNotification(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.managedTenants.managedTenantEmailNotification"] = Field(alias="@odata.type", default="#microsoft.graph.managedTenants.managedTenantEmailNotification")
	createdByUserId: Optional[str] = Field(alias="createdByUserId", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	emailAddresses: Optional[list[ManagedTenantsEmail]] = Field(alias="emailAddresses", default=None,)
	emailBody: Optional[str] = Field(alias="emailBody", default=None,)
	lastActionByUserId: Optional[str] = Field(alias="lastActionByUserId", default=None,)
	lastActionDateTime: Optional[datetime] = Field(alias="lastActionDateTime", default=None,)
	subject: Optional[str] = Field(alias="subject", default=None,)
	alert: Optional[ManagedTenantsManagedTenantAlert] = Field(alias="alert", default=None,)

from .managed_tenants_email import ManagedTenantsEmail
from .managed_tenants_managed_tenant_alert import ManagedTenantsManagedTenantAlert
