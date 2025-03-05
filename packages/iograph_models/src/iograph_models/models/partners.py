from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Partners(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	billing: Optional[PartnersBillingBilling] = Field(default=None,alias="billing",)

from .partners_billing_billing import PartnersBillingBilling

