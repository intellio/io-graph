from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SynchronizationStatus(BaseModel):
	code: Optional[SynchronizationStatusCode | str] = Field(alias="code",default=None,)
	countSuccessiveCompleteFailures: Optional[int] = Field(alias="countSuccessiveCompleteFailures",default=None,)
	escrowsPruned: Optional[bool] = Field(alias="escrowsPruned",default=None,)
	lastExecution: Optional[SynchronizationTaskExecution] = Field(alias="lastExecution",default=None,)
	lastSuccessfulExecution: Optional[SynchronizationTaskExecution] = Field(alias="lastSuccessfulExecution",default=None,)
	lastSuccessfulExecutionWithExports: Optional[SynchronizationTaskExecution] = Field(alias="lastSuccessfulExecutionWithExports",default=None,)
	progress: Optional[list[SynchronizationProgress]] = Field(alias="progress",default=None,)
	quarantine: Optional[SynchronizationQuarantine] = Field(alias="quarantine",default=None,)
	steadyStateFirstAchievedTime: Optional[datetime] = Field(alias="steadyStateFirstAchievedTime",default=None,)
	steadyStateLastAchievedTime: Optional[datetime] = Field(alias="steadyStateLastAchievedTime",default=None,)
	synchronizedEntryCountByType: Optional[list[StringKeyLongValuePair]] = Field(alias="synchronizedEntryCountByType",default=None,)
	troubleshootingUrl: Optional[str] = Field(alias="troubleshootingUrl",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .synchronization_status_code import SynchronizationStatusCode
from .synchronization_task_execution import SynchronizationTaskExecution
from .synchronization_task_execution import SynchronizationTaskExecution
from .synchronization_task_execution import SynchronizationTaskExecution
from .synchronization_progress import SynchronizationProgress
from .synchronization_quarantine import SynchronizationQuarantine
from .string_key_long_value_pair import StringKeyLongValuePair

