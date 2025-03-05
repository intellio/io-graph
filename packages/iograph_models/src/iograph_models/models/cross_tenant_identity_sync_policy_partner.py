from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CrossTenantIdentitySyncPolicyPartner(BaseModel):
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	tenantId: Optional[str] = Field(default=None,alias="tenantId",)
	userSyncInbound: Optional[CrossTenantUserSyncInbound] = Field(default=None,alias="userSyncInbound",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .cross_tenant_user_sync_inbound import CrossTenantUserSyncInbound

