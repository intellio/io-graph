from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SynchronizationTaskExecution(BaseModel):
	activityIdentifier: Optional[str] = Field(default=None,alias="activityIdentifier",)
	countEntitled: Optional[int] = Field(default=None,alias="countEntitled",)
	countEntitledForProvisioning: Optional[int] = Field(default=None,alias="countEntitledForProvisioning",)
	countEscrowed: Optional[int] = Field(default=None,alias="countEscrowed",)
	countEscrowedRaw: Optional[int] = Field(default=None,alias="countEscrowedRaw",)
	countExported: Optional[int] = Field(default=None,alias="countExported",)
	countExports: Optional[int] = Field(default=None,alias="countExports",)
	countImported: Optional[int] = Field(default=None,alias="countImported",)
	countImportedDeltas: Optional[int] = Field(default=None,alias="countImportedDeltas",)
	countImportedReferenceDeltas: Optional[int] = Field(default=None,alias="countImportedReferenceDeltas",)
	error: Optional[SynchronizationError] = Field(default=None,alias="error",)
	state: Optional[SynchronizationTaskExecutionResult] = Field(default=None,alias="state",)
	timeBegan: Optional[datetime] = Field(default=None,alias="timeBegan",)
	timeEnded: Optional[datetime] = Field(default=None,alias="timeEnded",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .synchronization_error import SynchronizationError
from .synchronization_task_execution_result import SynchronizationTaskExecutionResult

