from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class UserSimulationDetails(BaseModel):
	assignedTrainingsCount: Optional[int] = Field(alias="assignedTrainingsCount",default=None,)
	completedTrainingsCount: Optional[int] = Field(alias="completedTrainingsCount",default=None,)
	compromisedDateTime: Optional[datetime] = Field(alias="compromisedDateTime",default=None,)
	inProgressTrainingsCount: Optional[int] = Field(alias="inProgressTrainingsCount",default=None,)
	isCompromised: Optional[bool] = Field(alias="isCompromised",default=None,)
	latestSimulationActivity: Optional[str] = Field(alias="latestSimulationActivity",default=None,)
	reportedPhishDateTime: Optional[datetime] = Field(alias="reportedPhishDateTime",default=None,)
	simulationEvents: Optional[list[UserSimulationEventInfo]] = Field(alias="simulationEvents",default=None,)
	simulationUser: Optional[AttackSimulationUser] = Field(alias="simulationUser",default=None,)
	trainingEvents: Optional[list[UserTrainingEventInfo]] = Field(alias="trainingEvents",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .user_simulation_event_info import UserSimulationEventInfo
from .attack_simulation_user import AttackSimulationUser
from .user_training_event_info import UserTrainingEventInfo

