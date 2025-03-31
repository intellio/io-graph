from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class AttackSimulationSimulationUserCoverage(BaseModel):
	attackSimulationUser: Optional[AttackSimulationUser] = Field(alias="attackSimulationUser", default=None,)
	clickCount: Optional[int] = Field(alias="clickCount", default=None,)
	compromisedCount: Optional[int] = Field(alias="compromisedCount", default=None,)
	latestSimulationDateTime: Optional[datetime] = Field(alias="latestSimulationDateTime", default=None,)
	simulationCount: Optional[int] = Field(alias="simulationCount", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .attack_simulation_user import AttackSimulationUser
