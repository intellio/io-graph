from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class MultiTenantOrganizationIdentitySyncPolicyTemplate(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	templateApplicationLevel: Optional[TemplateApplicationLevel] = Field(default=None,alias="templateApplicationLevel",)
	userSyncInbound: Optional[CrossTenantUserSyncInbound] = Field(default=None,alias="userSyncInbound",)

from .template_application_level import TemplateApplicationLevel
from .cross_tenant_user_sync_inbound import CrossTenantUserSyncInbound

