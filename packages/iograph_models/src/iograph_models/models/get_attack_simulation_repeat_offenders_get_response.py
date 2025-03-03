from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Get_attack_simulation_repeat_offendersGetResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[AttackSimulationRepeatOffender]] = Field(default=None,alias="value",)

from .attack_simulation_repeat_offender import AttackSimulationRepeatOffender

