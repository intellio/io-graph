from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityComplianceSupervisionBaseAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.complianceSupervisionBaseAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.complianceSupervisionBaseAuditRecord")

