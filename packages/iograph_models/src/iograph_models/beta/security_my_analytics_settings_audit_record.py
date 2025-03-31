from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityMyAnalyticsSettingsAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.myAnalyticsSettingsAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.myAnalyticsSettingsAuditRecord")

