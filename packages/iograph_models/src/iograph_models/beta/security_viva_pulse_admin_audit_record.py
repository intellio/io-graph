from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityVivaPulseAdminAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.vivaPulseAdminAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.vivaPulseAdminAuditRecord")


