from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityWindows365CustomerLockboxAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.windows365CustomerLockboxAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.windows365CustomerLockboxAuditRecord")

