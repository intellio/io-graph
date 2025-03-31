from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityThreatFinderAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.threatFinderAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.threatFinderAuditRecord")

