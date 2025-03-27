from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityRetentionPolicyAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.retentionPolicyAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.retentionPolicyAuditRecord")


