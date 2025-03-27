from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityCdpOcrBillingRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.cdpOcrBillingRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.cdpOcrBillingRecord")


