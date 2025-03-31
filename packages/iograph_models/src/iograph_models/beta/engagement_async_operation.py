from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class EngagementAsyncOperation(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.engagementAsyncOperation"] = Field(alias="@odata.type",)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	lastActionDateTime: Optional[datetime] = Field(alias="lastActionDateTime", default=None,)
	resourceLocation: Optional[str] = Field(alias="resourceLocation", default=None,)
	status: Optional[LongRunningOperationStatus | str] = Field(alias="status", default=None,)
	statusDetail: Optional[str] = Field(alias="statusDetail", default=None,)
	operationType: Optional[EngagementAsyncOperationType | str] = Field(alias="operationType", default=None,)
	resourceId: Optional[str] = Field(alias="resourceId", default=None,)

from .long_running_operation_status import LongRunningOperationStatus
from .engagement_async_operation_type import EngagementAsyncOperationType
