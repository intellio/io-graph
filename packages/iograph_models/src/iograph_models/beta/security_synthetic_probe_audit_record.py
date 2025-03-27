from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecuritySyntheticProbeAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.syntheticProbeAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.syntheticProbeAuditRecord")


