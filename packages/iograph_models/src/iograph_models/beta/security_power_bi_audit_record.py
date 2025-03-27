from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityPowerBiAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.powerBiAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.powerBiAuditRecord")


