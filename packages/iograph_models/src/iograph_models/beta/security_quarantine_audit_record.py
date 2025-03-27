from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityQuarantineAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.quarantineAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.quarantineAuditRecord")


