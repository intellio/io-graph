from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class PlannerPlanDetails(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.plannerPlanDetails"] = Field(alias="@odata.type", default="#microsoft.graph.plannerPlanDetails")
	categoryDescriptions: Optional[PlannerCategoryDescriptions] = Field(alias="categoryDescriptions", default=None,)
	sharedWith: Optional[PlannerUserIds] = Field(alias="sharedWith", default=None,)

from .planner_category_descriptions import PlannerCategoryDescriptions
from .planner_user_ids import PlannerUserIds
