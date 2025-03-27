from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityComplianceDlpExchangeAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.complianceDlpExchangeAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.complianceDlpExchangeAuditRecord")


