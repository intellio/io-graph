from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecuritySharePointAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.sharePointAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.sharePointAuditRecord")


