from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityAttackSimAdminAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.attackSimAdminAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.attackSimAdminAuditRecord")

