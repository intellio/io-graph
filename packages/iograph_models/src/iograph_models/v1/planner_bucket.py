from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class PlannerBucket(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.plannerBucket"] = Field(alias="@odata.type",)
	name: Optional[str] = Field(alias="name", default=None,)
	orderHint: Optional[str] = Field(alias="orderHint", default=None,)
	planId: Optional[str] = Field(alias="planId", default=None,)
	tasks: Optional[list[PlannerTask]] = Field(alias="tasks", default=None,)

from .planner_task import PlannerTask
