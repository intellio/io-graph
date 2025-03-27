from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ManagedTenantsManagedTenantEmailNotification(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
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

