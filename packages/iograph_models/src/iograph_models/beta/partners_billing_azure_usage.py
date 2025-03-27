from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PartnersBillingAzureUsage(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	billed: Optional[PartnersBillingBilledUsage] = Field(alias="billed", default=None,)
	unbilled: Optional[PartnersBillingUnbilledUsage] = Field(alias="unbilled", default=None,)

from .partners_billing_billed_usage import PartnersBillingBilledUsage
from .partners_billing_unbilled_usage import PartnersBillingUnbilledUsage

