from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class UserSimulationDetails(BaseModel):
	assignedTrainingsCount: Optional[int] = Field(default=None,alias="assignedTrainingsCount",)
	completedTrainingsCount: Optional[int] = Field(default=None,alias="completedTrainingsCount",)
	compromisedDateTime: Optional[datetime] = Field(default=None,alias="compromisedDateTime",)
	inProgressTrainingsCount: Optional[int] = Field(default=None,alias="inProgressTrainingsCount",)
	isCompromised: Optional[bool] = Field(default=None,alias="isCompromised",)
	reportedPhishDateTime: Optional[datetime] = Field(default=None,alias="reportedPhishDateTime",)
	simulationEvents: Optional[list[UserSimulationEventInfo]] = Field(default=None,alias="simulationEvents",)
	simulationUser: Optional[AttackSimulationUser] = Field(default=None,alias="simulationUser",)
	trainingEvents: Optional[list[UserTrainingEventInfo]] = Field(default=None,alias="trainingEvents",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .user_simulation_event_info import UserSimulationEventInfo
from .attack_simulation_user import AttackSimulationUser
from .user_training_event_info import UserTrainingEventInfo

