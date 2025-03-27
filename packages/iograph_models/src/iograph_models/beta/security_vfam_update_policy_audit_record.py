from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityVfamUpdatePolicyAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.vfamUpdatePolicyAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.vfamUpdatePolicyAuditRecord")


