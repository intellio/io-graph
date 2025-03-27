from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Partners(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	billing: Optional[PartnersBillingBilling] = Field(alias="billing", default=None,)

from .partners_billing_billing import PartnersBillingBilling

