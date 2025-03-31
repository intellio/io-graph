from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class PlannerTaskConfiguration(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.plannerTaskConfiguration"] = Field(alias="@odata.type",)
	editPolicy: Optional[PlannerTaskPolicy] = Field(alias="editPolicy", default=None,)

from .planner_task_policy import PlannerTaskPolicy
