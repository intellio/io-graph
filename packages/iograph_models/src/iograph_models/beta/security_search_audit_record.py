from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecuritySearchAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.searchAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.searchAuditRecord")

