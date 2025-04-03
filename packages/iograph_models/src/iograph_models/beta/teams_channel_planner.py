from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class TeamsChannelPlanner(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.teamsChannelPlanner"] = Field(alias="@odata.type", default="#microsoft.graph.teamsChannelPlanner")
	plans: Optional[list[PlannerPlan]] = Field(alias="plans", default=None,)

from .planner_plan import PlannerPlan
