from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PartnersBillingAzureUsage(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	billed: Optional[PartnersBillingBilledUsage] = Field(default=None,alias="billed",)
	unbilled: Optional[PartnersBillingUnbilledUsage] = Field(default=None,alias="unbilled",)

from .partners_billing_billed_usage import PartnersBillingBilledUsage
from .partners_billing_unbilled_usage import PartnersBillingUnbilledUsage

