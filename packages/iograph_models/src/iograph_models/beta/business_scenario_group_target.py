from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class BusinessScenarioGroupTarget(BaseModel):
	taskTargetKind: Optional[PlannerTaskTargetKind | str] = Field(alias="taskTargetKind", default=None,)
	odata_type: Literal["#microsoft.graph.businessScenarioGroupTarget"] = Field(alias="@odata.type", default="#microsoft.graph.businessScenarioGroupTarget")
	groupId: Optional[str] = Field(alias="groupId", default=None,)

from .planner_task_target_kind import PlannerTaskTargetKind

