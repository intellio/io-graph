from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityPowerBiDlpAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.powerBiDlpAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.powerBiDlpAuditRecord")

