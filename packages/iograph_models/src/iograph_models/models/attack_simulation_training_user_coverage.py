from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AttackSimulationTrainingUserCoverage(BaseModel):
	attackSimulationUser: Optional[AttackSimulationUser] = Field(default=None,alias="attackSimulationUser",)
	userTrainings: list[UserTrainingStatusInfo] = Field(alias="userTrainings",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .attack_simulation_user import AttackSimulationUser
from .user_training_status_info import UserTrainingStatusInfo

