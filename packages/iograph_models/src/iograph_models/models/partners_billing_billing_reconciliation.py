from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PartnersBillingBillingReconciliation(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	billed: Optional[PartnersBillingBilledReconciliation] = Field(default=None,alias="billed",)

from .partners_billing_billed_reconciliation import PartnersBillingBilledReconciliation

