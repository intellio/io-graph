from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityCrmEntityOperationAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.crmEntityOperationAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.crmEntityOperationAuditRecord")

