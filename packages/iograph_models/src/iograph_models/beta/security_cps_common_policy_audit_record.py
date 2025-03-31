from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityCpsCommonPolicyAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.cpsCommonPolicyAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.cpsCommonPolicyAuditRecord")

