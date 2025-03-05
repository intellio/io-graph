from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class PartnersBillingFailedOperation(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	lastActionDateTime: Optional[datetime] = Field(default=None,alias="lastActionDateTime",)
	status: Optional[LongRunningOperationStatus] = Field(default=None,alias="status",)
	error: Optional[PublicError] = Field(default=None,alias="error",)

from .long_running_operation_status import LongRunningOperationStatus
from .public_error import PublicError

