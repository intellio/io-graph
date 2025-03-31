from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityDataLakeExportOperationAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.dataLakeExportOperationAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.dataLakeExportOperationAuditRecord")

