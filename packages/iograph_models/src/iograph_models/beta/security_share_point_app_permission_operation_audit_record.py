from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecuritySharePointAppPermissionOperationAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.sharePointAppPermissionOperationAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.sharePointAppPermissionOperationAuditRecord")


