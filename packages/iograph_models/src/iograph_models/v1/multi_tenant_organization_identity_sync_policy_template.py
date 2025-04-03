from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class MultiTenantOrganizationIdentitySyncPolicyTemplate(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.multiTenantOrganizationIdentitySyncPolicyTemplate"] = Field(alias="@odata.type", default="#microsoft.graph.multiTenantOrganizationIdentitySyncPolicyTemplate")
	templateApplicationLevel: Optional[TemplateApplicationLevel | str] = Field(alias="templateApplicationLevel", default=None,)
	userSyncInbound: Optional[CrossTenantUserSyncInbound] = Field(alias="userSyncInbound", default=None,)

from .template_application_level import TemplateApplicationLevel
from .cross_tenant_user_sync_inbound import CrossTenantUserSyncInbound
