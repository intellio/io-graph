from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityComplianceSupervisionExchangeAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.complianceSupervisionExchangeAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.complianceSupervisionExchangeAuditRecord")

