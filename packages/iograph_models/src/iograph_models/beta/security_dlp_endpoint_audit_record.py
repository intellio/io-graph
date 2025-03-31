from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityDlpEndpointAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.dlpEndpointAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.dlpEndpointAuditRecord")

