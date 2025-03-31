from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class NetworkaccessSettings(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.networkaccess.settings"] = Field(alias="@odata.type",)
	conditionalAccess: Optional[NetworkaccessConditionalAccessSettings] = Field(alias="conditionalAccess", default=None,)
	crossTenantAccess: Optional[NetworkaccessCrossTenantAccessSettings] = Field(alias="crossTenantAccess", default=None,)
	enrichedAuditLogs: Optional[NetworkaccessEnrichedAuditLogs] = Field(alias="enrichedAuditLogs", default=None,)
	forwardingOptions: Optional[NetworkaccessForwardingOptions] = Field(alias="forwardingOptions", default=None,)

from .networkaccess_conditional_access_settings import NetworkaccessConditionalAccessSettings
from .networkaccess_cross_tenant_access_settings import NetworkaccessCrossTenantAccessSettings
from .networkaccess_enriched_audit_logs import NetworkaccessEnrichedAuditLogs
from .networkaccess_forwarding_options import NetworkaccessForwardingOptions
