from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecuritySkypeForBusinessCmdletsAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.skypeForBusinessCmdletsAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.skypeForBusinessCmdletsAuditRecord")


