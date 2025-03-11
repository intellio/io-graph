from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PartnersBillingBillingReconciliation(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	billed: Optional[PartnersBillingBilledReconciliation] = Field(alias="billed",default=None,)

from .partners_billing_billed_reconciliation import PartnersBillingBilledReconciliation

