from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityMdiAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.mdiAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.mdiAuditRecord")


