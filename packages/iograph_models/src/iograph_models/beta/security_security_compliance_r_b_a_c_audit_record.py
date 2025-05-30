from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecuritySecurityComplianceRBACAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.securityComplianceRBACAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.securityComplianceRBACAuditRecord")

