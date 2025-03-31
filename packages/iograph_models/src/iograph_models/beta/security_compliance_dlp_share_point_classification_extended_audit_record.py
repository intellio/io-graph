from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityComplianceDlpSharePointClassificationExtendedAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.complianceDlpSharePointClassificationExtendedAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.complianceDlpSharePointClassificationExtendedAuditRecord")

