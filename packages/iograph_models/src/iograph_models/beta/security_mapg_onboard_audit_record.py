from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityMapgOnboardAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.mapgOnboardAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.mapgOnboardAuditRecord")


