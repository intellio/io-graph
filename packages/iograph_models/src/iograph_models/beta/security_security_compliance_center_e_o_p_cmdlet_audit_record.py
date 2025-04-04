from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecuritySecurityComplianceCenterEOPCmdletAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.securityComplianceCenterEOPCmdletAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.securityComplianceCenterEOPCmdletAuditRecord")

