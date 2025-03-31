from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityCaseAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.caseAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.caseAuditRecord")

