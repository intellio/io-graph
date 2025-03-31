from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityVivaGoalsAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.vivaGoalsAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.vivaGoalsAuditRecord")

