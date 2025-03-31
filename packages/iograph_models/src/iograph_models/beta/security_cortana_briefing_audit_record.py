from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityCortanaBriefingAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.cortanaBriefingAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.cortanaBriefingAuditRecord")

