from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class UserTrainingEventInfo(BaseModel):
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	latestTrainingStatus: Optional[str | TrainingStatus] = Field(alias="latestTrainingStatus",default=None,)
	trainingAssignedProperties: Optional[UserTrainingContentEventInfo] = Field(alias="trainingAssignedProperties",default=None,)
	trainingCompletedProperties: Optional[UserTrainingContentEventInfo] = Field(alias="trainingCompletedProperties",default=None,)
	trainingUpdatedProperties: Optional[UserTrainingContentEventInfo] = Field(alias="trainingUpdatedProperties",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .training_status import TrainingStatus
from .user_training_content_event_info import UserTrainingContentEventInfo
from .user_training_content_event_info import UserTrainingContentEventInfo
from .user_training_content_event_info import UserTrainingContentEventInfo

