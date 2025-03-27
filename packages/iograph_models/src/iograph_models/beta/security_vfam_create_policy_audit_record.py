from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityVfamCreatePolicyAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.vfamCreatePolicyAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.vfamCreatePolicyAuditRecord")


