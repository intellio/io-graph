from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class TeamsAsyncOperation(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	attemptsCount: Optional[int] = Field(default=None,alias="attemptsCount",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	error: Optional[OperationError] = Field(default=None,alias="error",)
	lastActionDateTime: Optional[datetime] = Field(default=None,alias="lastActionDateTime",)
	operationType: Optional[TeamsAsyncOperationType] = Field(default=None,alias="operationType",)
	status: Optional[TeamsAsyncOperationStatus] = Field(default=None,alias="status",)
	targetResourceId: Optional[str] = Field(default=None,alias="targetResourceId",)
	targetResourceLocation: Optional[str] = Field(default=None,alias="targetResourceLocation",)

from .operation_error import OperationError
from .teams_async_operation_type import TeamsAsyncOperationType
from .teams_async_operation_status import TeamsAsyncOperationStatus

