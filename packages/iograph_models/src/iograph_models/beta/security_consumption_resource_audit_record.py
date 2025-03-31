from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityConsumptionResourceAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.consumptionResourceAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.consumptionResourceAuditRecord")

