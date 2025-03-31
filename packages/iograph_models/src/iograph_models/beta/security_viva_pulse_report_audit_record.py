from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityVivaPulseReportAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.vivaPulseReportAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.vivaPulseReportAuditRecord")

