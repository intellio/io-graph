from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class PartnersBillingFailedOperationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[PartnersBillingFailedOperation]] = Field(alias="value", default=None,)

from .partners_billing_failed_operation import PartnersBillingFailedOperation
