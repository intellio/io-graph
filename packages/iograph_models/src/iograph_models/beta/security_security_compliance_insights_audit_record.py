from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecuritySecurityComplianceInsightsAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.securityComplianceInsightsAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.securityComplianceInsightsAuditRecord")

