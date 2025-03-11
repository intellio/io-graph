from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class NetworkaccessSettings(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	conditionalAccess: Optional[NetworkaccessConditionalAccessSettings] = Field(alias="conditionalAccess",default=None,)
	crossTenantAccess: Optional[NetworkaccessCrossTenantAccessSettings] = Field(alias="crossTenantAccess",default=None,)
	enrichedAuditLogs: Optional[NetworkaccessEnrichedAuditLogs] = Field(alias="enrichedAuditLogs",default=None,)
	forwardingOptions: Optional[NetworkaccessForwardingOptions] = Field(alias="forwardingOptions",default=None,)

from .networkaccess_conditional_access_settings import NetworkaccessConditionalAccessSettings
from .networkaccess_cross_tenant_access_settings import NetworkaccessCrossTenantAccessSettings
from .networkaccess_enriched_audit_logs import NetworkaccessEnrichedAuditLogs
from .networkaccess_forwarding_options import NetworkaccessForwardingOptions

