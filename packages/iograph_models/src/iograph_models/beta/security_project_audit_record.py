from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityProjectAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.projectAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.projectAuditRecord")

