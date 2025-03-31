from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityDataInsightsRestApiAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.dataInsightsRestApiAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.dataInsightsRestApiAuditRecord")

