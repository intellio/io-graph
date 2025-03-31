from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityComplianceDlpSharePointAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.complianceDlpSharePointAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.complianceDlpSharePointAuditRecord")

