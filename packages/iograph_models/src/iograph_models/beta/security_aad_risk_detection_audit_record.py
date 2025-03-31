from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityAadRiskDetectionAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.aadRiskDetectionAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.aadRiskDetectionAuditRecord")

