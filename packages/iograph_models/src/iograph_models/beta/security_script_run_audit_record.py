from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityScriptRunAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.scriptRunAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.scriptRunAuditRecord")

