from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class OperationApprovalRequestEntityStatus(BaseModel):
	entityLocked: Optional[bool] = Field(alias="entityLocked",default=None,)
	requestExpirationDateTime: Optional[datetime] = Field(alias="requestExpirationDateTime",default=None,)
	requestId: Optional[str] = Field(alias="requestId",default=None,)
	requestStatus: Optional[OperationApprovalRequestStatus | str] = Field(alias="requestStatus",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .operation_approval_request_status import OperationApprovalRequestStatus

