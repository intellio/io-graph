from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Planner(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	buckets: Optional[list[PlannerBucket]] = Field(default=None,alias="buckets",)
	plans: Optional[list[PlannerPlan]] = Field(default=None,alias="plans",)
	tasks: Optional[list[PlannerTask]] = Field(default=None,alias="tasks",)

from .planner_bucket import PlannerBucket
from .planner_plan import PlannerPlan
from .planner_task import PlannerTask

