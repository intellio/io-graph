from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityMcasAlertsAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.mcasAlertsAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.mcasAlertsAuditRecord")


