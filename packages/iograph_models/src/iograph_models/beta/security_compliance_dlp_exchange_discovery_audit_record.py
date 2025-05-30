from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityComplianceDlpExchangeDiscoveryAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.complianceDlpExchangeDiscoveryAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.complianceDlpExchangeDiscoveryAuditRecord")

