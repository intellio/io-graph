from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class SynchronizationStatus(BaseModel):
	code: Optional[SynchronizationStatusCode] = Field(default=None,alias="code",)
	countSuccessiveCompleteFailures: Optional[int] = Field(default=None,alias="countSuccessiveCompleteFailures",)
	escrowsPruned: Optional[bool] = Field(default=None,alias="escrowsPruned",)
	lastExecution: Optional[SynchronizationTaskExecution] = Field(default=None,alias="lastExecution",)
	lastSuccessfulExecution: Optional[SynchronizationTaskExecution] = Field(default=None,alias="lastSuccessfulExecution",)
	lastSuccessfulExecutionWithExports: Optional[SynchronizationTaskExecution] = Field(default=None,alias="lastSuccessfulExecutionWithExports",)
	progress: Optional[list[SynchronizationProgress]] = Field(default=None,alias="progress",)
	quarantine: Optional[SynchronizationQuarantine] = Field(default=None,alias="quarantine",)
	steadyStateFirstAchievedTime: Optional[datetime] = Field(default=None,alias="steadyStateFirstAchievedTime",)
	steadyStateLastAchievedTime: Optional[datetime] = Field(default=None,alias="steadyStateLastAchievedTime",)
	synchronizedEntryCountByType: Optional[list[StringKeyLongValuePair]] = Field(default=None,alias="synchronizedEntryCountByType",)
	troubleshootingUrl: Optional[str] = Field(default=None,alias="troubleshootingUrl",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .synchronization_status_code import SynchronizationStatusCode
from .synchronization_task_execution import SynchronizationTaskExecution
from .synchronization_task_execution import SynchronizationTaskExecution
from .synchronization_task_execution import SynchronizationTaskExecution
from .synchronization_progress import SynchronizationProgress
from .synchronization_quarantine import SynchronizationQuarantine
from .string_key_long_value_pair import StringKeyLongValuePair

