from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityMipAutoLabelExchangeItemAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.mipAutoLabelExchangeItemAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.mipAutoLabelExchangeItemAuditRecord")

