from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityUnifiedGroupAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.unifiedGroupAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.unifiedGroupAuditRecord")


