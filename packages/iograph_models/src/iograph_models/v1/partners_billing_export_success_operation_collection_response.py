from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PartnersBillingExportSuccessOperationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[PartnersBillingExportSuccessOperation]] = Field(alias="value",default=None,)

from .partners_billing_export_success_operation import PartnersBillingExportSuccessOperation

