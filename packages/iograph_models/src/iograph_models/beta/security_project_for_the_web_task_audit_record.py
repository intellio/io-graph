from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityProjectForTheWebTaskAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.projectForTheWebTaskAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.projectForTheWebTaskAuditRecord")

