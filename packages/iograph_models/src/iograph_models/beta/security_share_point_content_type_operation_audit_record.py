from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecuritySharePointContentTypeOperationAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.sharePointContentTypeOperationAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.sharePointContentTypeOperationAuditRecord")


