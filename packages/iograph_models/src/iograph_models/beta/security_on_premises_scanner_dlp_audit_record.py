from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityOnPremisesScannerDlpAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.onPremisesScannerDlpAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.onPremisesScannerDlpAuditRecord")

