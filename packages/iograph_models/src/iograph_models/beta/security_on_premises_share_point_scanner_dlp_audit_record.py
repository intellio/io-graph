from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityOnPremisesSharePointScannerDlpAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.onPremisesSharePointScannerDlpAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.onPremisesSharePointScannerDlpAuditRecord")

