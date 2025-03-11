from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class MultiTenantOrganizationIdentitySyncPolicyTemplate(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	templateApplicationLevel: Optional[TemplateApplicationLevel | str] = Field(alias="templateApplicationLevel",default=None,)
	userSyncInbound: Optional[CrossTenantUserSyncInbound] = Field(alias="userSyncInbound",default=None,)

from .template_application_level import TemplateApplicationLevel
from .cross_tenant_user_sync_inbound import CrossTenantUserSyncInbound

