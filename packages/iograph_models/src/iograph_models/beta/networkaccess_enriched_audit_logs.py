from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class NetworkaccessEnrichedAuditLogs(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.networkaccess.enrichedAuditLogs"] = Field(alias="@odata.type",)
	exchange: Optional[NetworkaccessEnrichedAuditLogsSettings] = Field(alias="exchange", default=None,)
	sharepoint: Optional[NetworkaccessEnrichedAuditLogsSettings] = Field(alias="sharepoint", default=None,)
	teams: Optional[NetworkaccessEnrichedAuditLogsSettings] = Field(alias="teams", default=None,)

from .networkaccess_enriched_audit_logs_settings import NetworkaccessEnrichedAuditLogsSettings
