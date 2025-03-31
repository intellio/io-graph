from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class ApprovalOperation(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.approvalOperation"] = Field(alias="@odata.type",)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	error: Optional[PublicError] = Field(alias="error", default=None,)
	lastActionDateTime: Optional[datetime] = Field(alias="lastActionDateTime", default=None,)
	resourceLocation: Optional[str] = Field(alias="resourceLocation", default=None,)
	status: Optional[ApprovalOperationStatus | str] = Field(alias="status", default=None,)

from .public_error import PublicError
from .approval_operation_status import ApprovalOperationStatus
