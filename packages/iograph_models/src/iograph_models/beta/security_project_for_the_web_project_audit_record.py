from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityProjectForTheWebProjectAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.projectForTheWebProjectAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.projectForTheWebProjectAuditRecord")


