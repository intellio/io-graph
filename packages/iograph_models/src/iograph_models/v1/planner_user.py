from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class PlannerUser(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.plannerUser"] = Field(alias="@odata.type",)
	plans: Optional[list[PlannerPlan]] = Field(alias="plans", default=None,)
	tasks: Optional[list[PlannerTask]] = Field(alias="tasks", default=None,)

from .planner_plan import PlannerPlan
from .planner_task import PlannerTask
