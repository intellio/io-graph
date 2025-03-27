from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityUrbacEnableStateAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.urbacEnableStateAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.urbacEnableStateAuditRecord")


