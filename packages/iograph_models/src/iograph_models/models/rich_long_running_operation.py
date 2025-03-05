from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class RichLongRunningOperation(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	lastActionDateTime: Optional[datetime] = Field(default=None,alias="lastActionDateTime",)
	resourceLocation: Optional[str] = Field(default=None,alias="resourceLocation",)
	status: Optional[LongRunningOperationStatus] = Field(default=None,alias="status",)
	statusDetail: Optional[str] = Field(default=None,alias="statusDetail",)
	error: Optional[PublicError] = Field(default=None,alias="error",)
	percentageComplete: Optional[int] = Field(default=None,alias="percentageComplete",)
	resourceId: Optional[str] = Field(default=None,alias="resourceId",)
	type: Optional[str] = Field(default=None,alias="type",)

from .long_running_operation_status import LongRunningOperationStatus
from .public_error import PublicError

