from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityUnifiedSimulationMatchedItemAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.unifiedSimulationMatchedItemAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.unifiedSimulationMatchedItemAuditRecord")

