from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class PlannerPlan(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	container: Optional[PlannerPlanContainer] = Field(default=None,alias="container",)
	createdBy: Optional[IdentitySet] = Field(default=None,alias="createdBy",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	owner: Optional[str] = Field(default=None,alias="owner",)
	title: Optional[str] = Field(default=None,alias="title",)
	buckets: list[PlannerBucket] = Field(alias="buckets",)
	details: Optional[PlannerPlanDetails] = Field(default=None,alias="details",)
	tasks: list[PlannerTask] = Field(alias="tasks",)

from .planner_plan_container import PlannerPlanContainer
from .identity_set import IdentitySet
from .planner_bucket import PlannerBucket
from .planner_plan_details import PlannerPlanDetails
from .planner_task import PlannerTask

