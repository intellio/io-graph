from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityTeamsHealthcareAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.teamsHealthcareAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.teamsHealthcareAuditRecord")

