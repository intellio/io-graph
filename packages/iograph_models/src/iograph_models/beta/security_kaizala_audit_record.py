from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityKaizalaAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.kaizalaAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.kaizalaAuditRecord")


