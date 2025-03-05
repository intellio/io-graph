from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class TrainingEventsContent(BaseModel):
	assignedTrainingsInfos: Optional[list[AssignedTrainingInfo]] = Field(alias="assignedTrainingsInfos",default=None,)
	trainingsAssignedUserCount: Optional[int] = Field(alias="trainingsAssignedUserCount",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .assigned_training_info import AssignedTrainingInfo

