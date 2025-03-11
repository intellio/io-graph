from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class PartnersBillingFailedOperation(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	lastActionDateTime: Optional[datetime] = Field(alias="lastActionDateTime",default=None,)
	status: Optional[LongRunningOperationStatus | str] = Field(alias="status",default=None,)
	error: Optional[PublicError] = Field(alias="error",default=None,)

from .long_running_operation_status import LongRunningOperationStatus
from .public_error import PublicError

