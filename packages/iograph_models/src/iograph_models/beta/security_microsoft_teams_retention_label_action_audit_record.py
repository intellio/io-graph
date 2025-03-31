from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityMicrosoftTeamsRetentionLabelActionAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.microsoftTeamsRetentionLabelActionAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.microsoftTeamsRetentionLabelActionAuditRecord")

