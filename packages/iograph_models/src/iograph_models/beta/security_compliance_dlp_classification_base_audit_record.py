from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityComplianceDlpClassificationBaseAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.complianceDlpClassificationBaseAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.complianceDlpClassificationBaseAuditRecord")

