from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class ManagedTenantsManagedTenantAlertLog(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.managedTenants.managedTenantAlertLog"] = Field(alias="@odata.type",)
	content: Optional[ManagedTenantsAlertLogContent] = Field(alias="content", default=None,)
	createdByUserId: Optional[str] = Field(alias="createdByUserId", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	lastActionByUserId: Optional[str] = Field(alias="lastActionByUserId", default=None,)
	lastActionDateTime: Optional[datetime] = Field(alias="lastActionDateTime", default=None,)
	alert: Optional[ManagedTenantsManagedTenantAlert] = Field(alias="alert", default=None,)

from .managed_tenants_alert_log_content import ManagedTenantsAlertLogContent
from .managed_tenants_managed_tenant_alert import ManagedTenantsManagedTenantAlert
