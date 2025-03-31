from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecuritySharePointFileOperationAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.sharePointFileOperationAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.sharePointFileOperationAuditRecord")

