from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityPlannerPlanAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.plannerPlanAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.plannerPlanAuditRecord")

