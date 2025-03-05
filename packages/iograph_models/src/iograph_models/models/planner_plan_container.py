from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PlannerPlanContainer(BaseModel):
	containerId: Optional[str] = Field(default=None,alias="containerId",)
	type: Optional[PlannerContainerType] = Field(default=None,alias="type",)
	url: Optional[str] = Field(default=None,alias="url",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .planner_container_type import PlannerContainerType

