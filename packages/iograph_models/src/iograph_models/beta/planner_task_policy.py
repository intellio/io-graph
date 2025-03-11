from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PlannerTaskPolicy(BaseModel):
	rules: Optional[list[PlannerTaskRoleBasedRule]] = Field(alias="rules",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .planner_task_role_based_rule import PlannerTaskRoleBasedRule

