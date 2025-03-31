from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityExchangeMailboxAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.exchangeMailboxAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.exchangeMailboxAuditRecord")

