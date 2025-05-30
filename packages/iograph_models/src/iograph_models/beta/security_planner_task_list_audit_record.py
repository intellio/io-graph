from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityPlannerTaskListAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.plannerTaskListAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.plannerTaskListAuditRecord")

