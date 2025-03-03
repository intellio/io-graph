from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class TrainingEventsContent(BaseModel):
	assignedTrainingsInfos: Optional[list[AssignedTrainingInfo]] = Field(default=None,alias="assignedTrainingsInfos",)
	trainingsAssignedUserCount: Optional[int] = Field(default=None,alias="trainingsAssignedUserCount",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .assigned_training_info import AssignedTrainingInfo

