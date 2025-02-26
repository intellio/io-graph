from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class PlannerUser(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	plans: list[PlannerPlan] = Field(alias="plans",)
	tasks: list[PlannerTask] = Field(alias="tasks",)

from .planner_plan import PlannerPlan
from .planner_task import PlannerTask

