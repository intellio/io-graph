from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityDataCenterSecurityCmdletAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.dataCenterSecurityCmdletAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.dataCenterSecurityCmdletAuditRecord")


