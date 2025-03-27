from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityOnPremisesFileShareScannerDlpAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.onPremisesFileShareScannerDlpAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.onPremisesFileShareScannerDlpAuditRecord")


