from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CrossTenantIdentitySyncPolicyPartner(BaseModel):
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	tenantId: Optional[str] = Field(alias="tenantId",default=None,)
	userSyncInbound: Optional[CrossTenantUserSyncInbound] = Field(alias="userSyncInbound",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .cross_tenant_user_sync_inbound import CrossTenantUserSyncInbound

