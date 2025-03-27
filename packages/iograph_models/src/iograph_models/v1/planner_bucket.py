from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PlannerBucket(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	name: Optional[str] = Field(alias="name", default=None,)
	orderHint: Optional[str] = Field(alias="orderHint", default=None,)
	planId: Optional[str] = Field(alias="planId", default=None,)
	tasks: Optional[list[PlannerTask]] = Field(alias="tasks", default=None,)

from .planner_task import PlannerTask

