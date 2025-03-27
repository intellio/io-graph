from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PlannerTaskConfiguration(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	editPolicy: Optional[PlannerTaskPolicy] = Field(alias="editPolicy", default=None,)

from .planner_task_policy import PlannerTaskPolicy

