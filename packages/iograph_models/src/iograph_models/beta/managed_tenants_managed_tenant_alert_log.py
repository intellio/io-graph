from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ManagedTenantsManagedTenantAlertLog(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	content: Optional[ManagedTenantsAlertLogContent] = Field(alias="content",default=None,)
	createdByUserId: Optional[str] = Field(alias="createdByUserId",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	lastActionByUserId: Optional[str] = Field(alias="lastActionByUserId",default=None,)
	lastActionDateTime: Optional[datetime] = Field(alias="lastActionDateTime",default=None,)
	alert: Optional[ManagedTenantsManagedTenantAlert] = Field(alias="alert",default=None,)

from .managed_tenants_alert_log_content import ManagedTenantsAlertLogContent
from .managed_tenants_managed_tenant_alert import ManagedTenantsManagedTenantAlert

