from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityMapgAlertsAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.mapgAlertsAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.mapgAlertsAuditRecord")

