from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityComplianceDlpEndpointAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.complianceDlpEndpointAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.complianceDlpEndpointAuditRecord")


