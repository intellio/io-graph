from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class EngagementAsyncOperation(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	lastActionDateTime: Optional[datetime] = Field(default=None,alias="lastActionDateTime",)
	resourceLocation: Optional[str] = Field(default=None,alias="resourceLocation",)
	status: Optional[LongRunningOperationStatus] = Field(default=None,alias="status",)
	statusDetail: Optional[str] = Field(default=None,alias="statusDetail",)
	operationType: Optional[EngagementAsyncOperationType] = Field(default=None,alias="operationType",)
	resourceId: Optional[str] = Field(default=None,alias="resourceId",)

from .long_running_operation_status import LongRunningOperationStatus
from .engagement_async_operation_type import EngagementAsyncOperationType

