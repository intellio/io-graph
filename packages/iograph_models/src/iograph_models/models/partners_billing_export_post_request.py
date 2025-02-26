from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Partners_billing_exportPostRequest(BaseModel):
	currencyCode: Optional[str] = Field(default=None,alias="currencyCode",)
	billingPeriod: Optional[PartnersBillingBillingPeriod] = Field(default=None,alias="billingPeriod",)
	attributeSet: Optional[PartnersBillingAttributeSet] = Field(default=None,alias="attributeSet",)

from .partners_billing_billing_period import PartnersBillingBillingPeriod
from .partners_billing_attribute_set import PartnersBillingAttributeSet

