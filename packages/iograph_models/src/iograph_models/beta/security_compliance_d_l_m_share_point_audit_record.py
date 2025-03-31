from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityComplianceDLMSharePointAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.complianceDLMSharePointAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.complianceDLMSharePointAuditRecord")

