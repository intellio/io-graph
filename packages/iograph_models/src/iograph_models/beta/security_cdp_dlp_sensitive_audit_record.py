from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityCdpDlpSensitiveAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.cdpDlpSensitiveAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.cdpDlpSensitiveAuditRecord")


