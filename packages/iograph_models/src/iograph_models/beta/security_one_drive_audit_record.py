from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityOneDriveAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.oneDriveAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.oneDriveAuditRecord")

