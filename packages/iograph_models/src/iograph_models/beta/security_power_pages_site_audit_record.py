from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityPowerPagesSiteAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.powerPagesSiteAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.powerPagesSiteAuditRecord")


