from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecuritySharePointSharingOperationAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.sharePointSharingOperationAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.sharePointSharingOperationAuditRecord")


