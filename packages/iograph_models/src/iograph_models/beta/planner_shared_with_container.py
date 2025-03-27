from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class PlannerSharedWithContainer(BaseModel):
	containerId: Optional[str] = Field(alias="containerId", default=None,)
	type: Optional[PlannerContainerType | str] = Field(alias="type", default=None,)
	url: Optional[str] = Field(alias="url", default=None,)
	odata_type: Literal["#microsoft.graph.plannerSharedWithContainer"] = Field(alias="@odata.type", default="#microsoft.graph.plannerSharedWithContainer")
	accessLevel: Optional[PlannerPlanAccessLevel | str] = Field(alias="accessLevel", default=None,)

from .planner_container_type import PlannerContainerType
from .planner_plan_access_level import PlannerPlanAccessLevel

