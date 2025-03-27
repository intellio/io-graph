from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityDiscoveryAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.discoveryAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.discoveryAuditRecord")


