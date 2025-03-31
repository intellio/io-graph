from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class PartnersBillingBillingReconciliation(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.partners.billing.billingReconciliation"] = Field(alias="@odata.type",)
	billed: Optional[PartnersBillingBilledReconciliation] = Field(alias="billed", default=None,)

from .partners_billing_billed_reconciliation import PartnersBillingBilledReconciliation
