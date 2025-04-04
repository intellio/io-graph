from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityPhysicalBadgingSignalAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.physicalBadgingSignalAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.physicalBadgingSignalAuditRecord")

