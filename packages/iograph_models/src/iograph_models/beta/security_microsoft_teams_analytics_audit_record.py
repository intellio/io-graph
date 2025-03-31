from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityMicrosoftTeamsAnalyticsAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.microsoftTeamsAnalyticsAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.microsoftTeamsAnalyticsAuditRecord")

