from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityVfamDeletePolicyAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.vfamDeletePolicyAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.vfamDeletePolicyAuditRecord")


