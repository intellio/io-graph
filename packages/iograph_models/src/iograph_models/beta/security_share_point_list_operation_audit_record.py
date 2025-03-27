from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecuritySharePointListOperationAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.sharePointListOperationAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.sharePointListOperationAuditRecord")


