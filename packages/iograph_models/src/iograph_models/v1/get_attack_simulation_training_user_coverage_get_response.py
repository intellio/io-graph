from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Get_attack_simulation_training_user_coverageGetResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[AttackSimulationTrainingUserCoverage]] = Field(alias="value", default=None,)

from .attack_simulation_training_user_coverage import AttackSimulationTrainingUserCoverage
