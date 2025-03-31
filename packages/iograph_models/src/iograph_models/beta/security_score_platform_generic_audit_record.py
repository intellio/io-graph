from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityScorePlatformGenericAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.scorePlatformGenericAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.scorePlatformGenericAuditRecord")

