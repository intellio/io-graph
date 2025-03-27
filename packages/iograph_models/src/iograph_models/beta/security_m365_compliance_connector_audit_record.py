from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityM365ComplianceConnectorAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.m365ComplianceConnectorAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.m365ComplianceConnectorAuditRecord")


