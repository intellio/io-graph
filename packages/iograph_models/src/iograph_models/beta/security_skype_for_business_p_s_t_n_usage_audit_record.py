from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecuritySkypeForBusinessPSTNUsageAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.skypeForBusinessPSTNUsageAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.skypeForBusinessPSTNUsageAuditRecord")

