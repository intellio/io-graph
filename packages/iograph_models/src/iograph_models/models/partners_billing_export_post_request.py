from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Partners_billing_exportPostRequest(BaseModel):
	currencyCode: Optional[str] = Field(alias="currencyCode",default=None,)
	billingPeriod: Optional[str | PartnersBillingBillingPeriod] = Field(alias="billingPeriod",default=None,)
	attributeSet: Optional[str | PartnersBillingAttributeSet] = Field(alias="attributeSet",default=None,)

from .partners_billing_billing_period import PartnersBillingBillingPeriod
from .partners_billing_attribute_set import PartnersBillingAttributeSet

