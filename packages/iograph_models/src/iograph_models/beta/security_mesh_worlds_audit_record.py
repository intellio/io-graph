from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityMeshWorldsAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.meshWorldsAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.meshWorldsAuditRecord")

