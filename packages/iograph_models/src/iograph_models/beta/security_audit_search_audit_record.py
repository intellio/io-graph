from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityAuditSearchAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.auditSearchAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.auditSearchAuditRecord")

