from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityRecordsManagementAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.recordsManagementAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.recordsManagementAuditRecord")


