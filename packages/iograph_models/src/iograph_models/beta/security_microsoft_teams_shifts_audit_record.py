from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityMicrosoftTeamsShiftsAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.microsoftTeamsShiftsAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.microsoftTeamsShiftsAuditRecord")

