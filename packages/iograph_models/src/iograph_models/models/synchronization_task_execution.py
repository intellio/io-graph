from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SynchronizationTaskExecution(BaseModel):
	activityIdentifier: Optional[str] = Field(alias="activityIdentifier",default=None,)
	countEntitled: Optional[int] = Field(alias="countEntitled",default=None,)
	countEntitledForProvisioning: Optional[int] = Field(alias="countEntitledForProvisioning",default=None,)
	countEscrowed: Optional[int] = Field(alias="countEscrowed",default=None,)
	countEscrowedRaw: Optional[int] = Field(alias="countEscrowedRaw",default=None,)
	countExported: Optional[int] = Field(alias="countExported",default=None,)
	countExports: Optional[int] = Field(alias="countExports",default=None,)
	countImported: Optional[int] = Field(alias="countImported",default=None,)
	countImportedDeltas: Optional[int] = Field(alias="countImportedDeltas",default=None,)
	countImportedReferenceDeltas: Optional[int] = Field(alias="countImportedReferenceDeltas",default=None,)
	error: Optional[SynchronizationError] = Field(alias="error",default=None,)
	state: Optional[str | SynchronizationTaskExecutionResult] = Field(alias="state",default=None,)
	timeBegan: Optional[datetime] = Field(alias="timeBegan",default=None,)
	timeEnded: Optional[datetime] = Field(alias="timeEnded",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .synchronization_error import SynchronizationError
from .synchronization_task_execution_result import SynchronizationTaskExecutionResult

