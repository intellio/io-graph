from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PlannerPlanContextDetails(BaseModel):
	customLinkText: Optional[str] = Field(alias="customLinkText",default=None,)
	displayLinkType: Optional[PlannerPlanContextType | str] = Field(alias="displayLinkType",default=None,)
	state: Optional[PlannerContextState | str] = Field(alias="state",default=None,)
	url: Optional[str] = Field(alias="url",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .planner_plan_context_type import PlannerPlanContextType
from .planner_context_state import PlannerContextState

