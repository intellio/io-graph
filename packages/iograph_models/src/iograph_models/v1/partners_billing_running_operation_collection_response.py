from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class PartnersBillingRunningOperationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[PartnersBillingRunningOperation]] = Field(alias="value", default=None,)

from .partners_billing_running_operation import PartnersBillingRunningOperation
