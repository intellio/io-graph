from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecuritySupervisoryReviewDayXInsightsAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.supervisoryReviewDayXInsightsAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.supervisoryReviewDayXInsightsAuditRecord")

