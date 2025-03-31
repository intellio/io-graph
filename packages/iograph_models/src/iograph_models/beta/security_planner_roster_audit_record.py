from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityPlannerRosterAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.plannerRosterAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.plannerRosterAuditRecord")

