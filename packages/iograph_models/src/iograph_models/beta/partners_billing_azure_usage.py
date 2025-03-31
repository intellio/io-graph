from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class PartnersBillingAzureUsage(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.partners.billing.azureUsage"] = Field(alias="@odata.type",)
	billed: Optional[PartnersBillingBilledUsage] = Field(alias="billed", default=None,)
	unbilled: Optional[PartnersBillingUnbilledUsage] = Field(alias="unbilled", default=None,)

from .partners_billing_billed_usage import PartnersBillingBilledUsage
from .partners_billing_unbilled_usage import PartnersBillingUnbilledUsage
