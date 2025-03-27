from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityMapgPolicyAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.mapgPolicyAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.mapgPolicyAuditRecord")


