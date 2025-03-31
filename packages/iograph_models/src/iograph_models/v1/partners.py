from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class Partners(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.partners"] = Field(alias="@odata.type",)
	billing: Optional[PartnersBillingBilling] = Field(alias="billing", default=None,)

from .partners_billing_billing import PartnersBillingBilling
