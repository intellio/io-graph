from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityPowerPlatformAdminEnvironmentAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.powerPlatformAdminEnvironmentAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.powerPlatformAdminEnvironmentAuditRecord")

