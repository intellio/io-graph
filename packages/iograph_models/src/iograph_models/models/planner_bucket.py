from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PlannerBucket(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	name: Optional[str] = Field(default=None,alias="name",)
	orderHint: Optional[str] = Field(default=None,alias="orderHint",)
	planId: Optional[str] = Field(default=None,alias="planId",)
	tasks: Optional[list[PlannerTask]] = Field(default=None,alias="tasks",)

from .planner_task import PlannerTask

