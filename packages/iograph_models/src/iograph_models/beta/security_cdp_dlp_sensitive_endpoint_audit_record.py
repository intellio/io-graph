from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityCdpDlpSensitiveEndpointAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.cdpDlpSensitiveEndpointAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.cdpDlpSensitiveEndpointAuditRecord")


