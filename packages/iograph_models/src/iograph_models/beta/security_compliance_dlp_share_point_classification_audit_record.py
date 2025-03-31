from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityComplianceDlpSharePointClassificationAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.complianceDlpSharePointClassificationAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.complianceDlpSharePointClassificationAuditRecord")

