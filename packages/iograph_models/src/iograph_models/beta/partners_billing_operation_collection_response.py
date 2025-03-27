from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class PartnersBillingOperationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[PartnersBillingExportSuccessOperation, PartnersBillingFailedOperation, PartnersBillingRunningOperation]],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .partners_billing_export_success_operation import PartnersBillingExportSuccessOperation
from .partners_billing_failed_operation import PartnersBillingFailedOperation
from .partners_billing_running_operation import PartnersBillingRunningOperation

