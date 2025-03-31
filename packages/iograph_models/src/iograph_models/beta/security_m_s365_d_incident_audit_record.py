from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityMS365DIncidentAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.mS365DIncidentAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.mS365DIncidentAuditRecord")

