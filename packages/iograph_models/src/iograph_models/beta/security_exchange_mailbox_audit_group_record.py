from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityExchangeMailboxAuditGroupRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.exchangeMailboxAuditGroupRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.exchangeMailboxAuditGroupRecord")


