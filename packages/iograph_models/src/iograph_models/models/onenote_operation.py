from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class OnenoteOperation(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	lastActionDateTime: Optional[datetime] = Field(default=None,alias="lastActionDateTime",)
	status: Optional[OperationStatus] = Field(default=None,alias="status",)
	error: Optional[OnenoteOperationError] = Field(default=None,alias="error",)
	percentComplete: Optional[str] = Field(default=None,alias="percentComplete",)
	resourceId: Optional[str] = Field(default=None,alias="resourceId",)
	resourceLocation: Optional[str] = Field(default=None,alias="resourceLocation",)

from .operation_status import OperationStatus
from .onenote_operation_error import OnenoteOperationError

