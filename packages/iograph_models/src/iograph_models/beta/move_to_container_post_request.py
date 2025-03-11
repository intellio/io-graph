from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Move_to_containerPostRequest(BaseModel):
	container: SerializeAsAny[Optional[PlannerPlanContainer]] = Field(alias="container",default=None,)

from .planner_plan_container import PlannerPlanContainer

