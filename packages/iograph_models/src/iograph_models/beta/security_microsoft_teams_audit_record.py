from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityMicrosoftTeamsAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.microsoftTeamsAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.microsoftTeamsAuditRecord")

