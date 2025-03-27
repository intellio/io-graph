from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityUrbacRoleAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.urbacRoleAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.urbacRoleAuditRecord")


