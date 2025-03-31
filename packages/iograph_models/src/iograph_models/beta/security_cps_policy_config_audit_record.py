from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityCpsPolicyConfigAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.cpsPolicyConfigAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.cpsPolicyConfigAuditRecord")

