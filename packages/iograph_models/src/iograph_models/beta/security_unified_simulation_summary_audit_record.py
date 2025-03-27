from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityUnifiedSimulationSummaryAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.unifiedSimulationSummaryAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.unifiedSimulationSummaryAuditRecord")


