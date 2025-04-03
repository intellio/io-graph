from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class TeamsAsyncOperation(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.teamsAsyncOperation"] = Field(alias="@odata.type", default="#microsoft.graph.teamsAsyncOperation")
	attemptsCount: Optional[int] = Field(alias="attemptsCount", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	error: Optional[OperationError] = Field(alias="error", default=None,)
	lastActionDateTime: Optional[datetime] = Field(alias="lastActionDateTime", default=None,)
	operationType: Optional[TeamsAsyncOperationType | str] = Field(alias="operationType", default=None,)
	status: Optional[TeamsAsyncOperationStatus | str] = Field(alias="status", default=None,)
	targetResourceId: Optional[str] = Field(alias="targetResourceId", default=None,)
	targetResourceLocation: Optional[str] = Field(alias="targetResourceLocation", default=None,)

from .operation_error import OperationError
from .teams_async_operation_type import TeamsAsyncOperationType
from .teams_async_operation_status import TeamsAsyncOperationStatus
