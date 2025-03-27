from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityExchangeMailboxAuditBaseRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.exchangeMailboxAuditBaseRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.exchangeMailboxAuditBaseRecord")


