from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecuritySecurityComplianceUserChangeAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.securityComplianceUserChangeAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.securityComplianceUserChangeAuditRecord")


