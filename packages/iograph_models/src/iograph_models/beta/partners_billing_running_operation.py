from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class PartnersBillingRunningOperation(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.partners.billing.runningOperation"] = Field(alias="@odata.type", default="#microsoft.graph.partners.billing.runningOperation")
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	lastActionDateTime: Optional[datetime] = Field(alias="lastActionDateTime", default=None,)
	status: Optional[LongRunningOperationStatus | str] = Field(alias="status", default=None,)

from .long_running_operation_status import LongRunningOperationStatus
