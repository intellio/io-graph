from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityExchangeAdminAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.exchangeAdminAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.exchangeAdminAuditRecord")


