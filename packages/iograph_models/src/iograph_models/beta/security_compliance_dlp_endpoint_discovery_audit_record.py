from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityComplianceDlpEndpointDiscoveryAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.complianceDlpEndpointDiscoveryAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.complianceDlpEndpointDiscoveryAuditRecord")

