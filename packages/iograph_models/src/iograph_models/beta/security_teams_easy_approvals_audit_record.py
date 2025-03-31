from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityTeamsEasyApprovalsAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.teamsEasyApprovalsAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.teamsEasyApprovalsAuditRecord")

