from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class UserTrainingStatusInfo(BaseModel):
	assignedDateTime: Optional[datetime] = Field(alias="assignedDateTime", default=None,)
	completionDateTime: Optional[datetime] = Field(alias="completionDateTime", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	trainingStatus: Optional[TrainingStatus | str] = Field(alias="trainingStatus", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .training_status import TrainingStatus
