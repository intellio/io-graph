from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityPlannerTaskAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.plannerTaskAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.plannerTaskAuditRecord")


