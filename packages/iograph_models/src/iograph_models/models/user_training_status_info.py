from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class UserTrainingStatusInfo(BaseModel):
	assignedDateTime: Optional[datetime] = Field(default=None,alias="assignedDateTime",)
	completionDateTime: Optional[datetime] = Field(default=None,alias="completionDateTime",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	trainingStatus: Optional[TrainingStatus] = Field(default=None,alias="trainingStatus",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .training_status import TrainingStatus

