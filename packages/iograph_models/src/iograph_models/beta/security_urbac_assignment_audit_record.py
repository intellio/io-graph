from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityUrbacAssignmentAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.urbacAssignmentAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.urbacAssignmentAuditRecord")

