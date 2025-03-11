from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class BusinessScenarioGroupTarget(BaseModel):
	taskTargetKind: Optional[PlannerTaskTargetKind | str] = Field(alias="taskTargetKind",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	groupId: Optional[str] = Field(alias="groupId",default=None,)

from .planner_task_target_kind import PlannerTaskTargetKind

