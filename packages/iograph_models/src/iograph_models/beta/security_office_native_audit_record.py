from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityOfficeNativeAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.officeNativeAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.officeNativeAuditRecord")

