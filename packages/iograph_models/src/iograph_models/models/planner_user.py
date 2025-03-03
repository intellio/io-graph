from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class PlannerUser(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	plans: Optional[list[PlannerPlan]] = Field(default=None,alias="plans",)
	tasks: Optional[list[PlannerTask]] = Field(default=None,alias="tasks",)

from .planner_plan import PlannerPlan
from .planner_task import PlannerTask

