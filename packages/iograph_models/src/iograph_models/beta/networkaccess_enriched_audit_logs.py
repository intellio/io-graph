from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class NetworkaccessEnrichedAuditLogs(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	exchange: Optional[NetworkaccessEnrichedAuditLogsSettings] = Field(alias="exchange",default=None,)
	sharepoint: Optional[NetworkaccessEnrichedAuditLogsSettings] = Field(alias="sharepoint",default=None,)
	teams: Optional[NetworkaccessEnrichedAuditLogsSettings] = Field(alias="teams",default=None,)

from .networkaccess_enriched_audit_logs_settings import NetworkaccessEnrichedAuditLogsSettings
from .networkaccess_enriched_audit_logs_settings import NetworkaccessEnrichedAuditLogsSettings
from .networkaccess_enriched_audit_logs_settings import NetworkaccessEnrichedAuditLogsSettings

