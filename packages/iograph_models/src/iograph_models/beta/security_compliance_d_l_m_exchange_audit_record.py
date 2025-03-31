from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityComplianceDLMExchangeAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.complianceDLMExchangeAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.complianceDLMExchangeAuditRecord")

