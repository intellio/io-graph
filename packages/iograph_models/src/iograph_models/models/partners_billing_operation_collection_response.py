from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PartnersBillingOperationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: SerializeAsAny[Optional[list[PartnersBillingOperation]]] = Field(default=None,alias="value",)

from .partners_billing_operation import PartnersBillingOperation

