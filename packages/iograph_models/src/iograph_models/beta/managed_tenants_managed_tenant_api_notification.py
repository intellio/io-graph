from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ManagedTenantsManagedTenantApiNotification(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	createdByUserId: Optional[str] = Field(alias="createdByUserId", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	isAcknowledged: Optional[bool] = Field(alias="isAcknowledged", default=None,)
	lastActionByUserId: Optional[str] = Field(alias="lastActionByUserId", default=None,)
	lastActionDateTime: Optional[datetime] = Field(alias="lastActionDateTime", default=None,)
	message: Optional[str] = Field(alias="message", default=None,)
	title: Optional[str] = Field(alias="title", default=None,)
	userId: Optional[str] = Field(alias="userId", default=None,)
	alert: Optional[ManagedTenantsManagedTenantAlert] = Field(alias="alert", default=None,)

from .managed_tenants_managed_tenant_alert import ManagedTenantsManagedTenantAlert

