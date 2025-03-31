from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityPowerPlatformAdminDlpAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.powerPlatformAdminDlpAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.powerPlatformAdminDlpAuditRecord")

