from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityTeamsUpdatesAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.teamsUpdatesAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.teamsUpdatesAuditRecord")

