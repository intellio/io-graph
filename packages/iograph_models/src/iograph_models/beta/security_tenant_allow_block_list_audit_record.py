from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityTenantAllowBlockListAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.tenantAllowBlockListAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.tenantAllowBlockListAuditRecord")

