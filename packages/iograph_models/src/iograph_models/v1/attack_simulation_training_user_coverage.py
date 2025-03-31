from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AttackSimulationTrainingUserCoverage(BaseModel):
	attackSimulationUser: Optional[AttackSimulationUser] = Field(alias="attackSimulationUser", default=None,)
	userTrainings: Optional[list[UserTrainingStatusInfo]] = Field(alias="userTrainings", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .attack_simulation_user import AttackSimulationUser
from .user_training_status_info import UserTrainingStatusInfo
