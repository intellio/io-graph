from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class UserTrainingEventInfo(BaseModel):
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	latestTrainingStatus: Optional[TrainingStatus] = Field(default=None,alias="latestTrainingStatus",)
	trainingAssignedProperties: Optional[UserTrainingContentEventInfo] = Field(default=None,alias="trainingAssignedProperties",)
	trainingCompletedProperties: Optional[UserTrainingContentEventInfo] = Field(default=None,alias="trainingCompletedProperties",)
	trainingUpdatedProperties: Optional[UserTrainingContentEventInfo] = Field(default=None,alias="trainingUpdatedProperties",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .training_status import TrainingStatus
from .user_training_content_event_info import UserTrainingContentEventInfo
from .user_training_content_event_info import UserTrainingContentEventInfo
from .user_training_content_event_info import UserTrainingContentEventInfo

