from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityAedAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.aedAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.aedAuditRecord")


