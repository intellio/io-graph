from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityComplianceConnectorAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.complianceConnectorAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.complianceConnectorAuditRecord")


