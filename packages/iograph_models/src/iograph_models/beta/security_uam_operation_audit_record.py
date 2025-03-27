from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityUamOperationAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.uamOperationAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.uamOperationAuditRecord")


