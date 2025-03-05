from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PlannerPlanContainer(BaseModel):
	containerId: Optional[str] = Field(alias="containerId",default=None,)
	type: Optional[str | PlannerContainerType] = Field(alias="type",default=None,)
	url: Optional[str] = Field(alias="url",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .planner_container_type import PlannerContainerType

