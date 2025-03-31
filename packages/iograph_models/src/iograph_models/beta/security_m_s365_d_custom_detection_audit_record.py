from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityMS365DCustomDetectionAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.mS365DCustomDetectionAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.mS365DCustomDetectionAuditRecord")

