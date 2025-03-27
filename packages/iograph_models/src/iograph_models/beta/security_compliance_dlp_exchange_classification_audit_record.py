from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityComplianceDlpExchangeClassificationAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.complianceDlpExchangeClassificationAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.complianceDlpExchangeClassificationAuditRecord")


