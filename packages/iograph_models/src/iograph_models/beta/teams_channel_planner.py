from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class TeamsChannelPlanner(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	plans: Optional[list[PlannerPlan]] = Field(alias="plans", default=None,)

from .planner_plan import PlannerPlan

