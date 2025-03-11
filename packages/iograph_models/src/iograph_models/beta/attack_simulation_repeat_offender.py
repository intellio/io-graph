from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AttackSimulationRepeatOffender(BaseModel):
	attackSimulationUser: Optional[AttackSimulationUser] = Field(alias="attackSimulationUser",default=None,)
	repeatOffenceCount: Optional[int] = Field(alias="repeatOffenceCount",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .attack_simulation_user import AttackSimulationUser

