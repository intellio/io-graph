from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class PartnersBillingBilledUsage(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.partners.billing.billedUsage"] = Field(alias="@odata.type",)

