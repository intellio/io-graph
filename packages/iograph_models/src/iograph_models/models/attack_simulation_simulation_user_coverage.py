from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class AttackSimulationSimulationUserCoverage(BaseModel):
	attackSimulationUser: Optional[AttackSimulationUser] = Field(default=None,alias="attackSimulationUser",)
	clickCount: Optional[int] = Field(default=None,alias="clickCount",)
	compromisedCount: Optional[int] = Field(default=None,alias="compromisedCount",)
	latestSimulationDateTime: Optional[datetime] = Field(default=None,alias="latestSimulationDateTime",)
	simulationCount: Optional[int] = Field(default=None,alias="simulationCount",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .attack_simulation_user import AttackSimulationUser

