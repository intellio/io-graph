from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityOmePortalAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.omePortalAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.omePortalAuditRecord")


