from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityDataCenterSecurityBaseAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.dataCenterSecurityBaseAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.dataCenterSecurityBaseAuditRecord")

