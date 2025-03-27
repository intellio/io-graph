from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecuritySharePointFieldOperationAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.sharePointFieldOperationAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.sharePointFieldOperationAuditRecord")


