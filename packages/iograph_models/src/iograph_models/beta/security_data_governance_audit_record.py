from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityDataGovernanceAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.dataGovernanceAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.dataGovernanceAuditRecord")

