from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AttackSimulationRepeatOffender(BaseModel):
	attackSimulationUser: Optional[AttackSimulationUser] = Field(default=None,alias="attackSimulationUser",)
	repeatOffenceCount: Optional[int] = Field(default=None,alias="repeatOffenceCount",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .attack_simulation_user import AttackSimulationUser

