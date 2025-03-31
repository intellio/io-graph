from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityComplianceDlpBaseAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.complianceDlpBaseAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.complianceDlpBaseAuditRecord")

