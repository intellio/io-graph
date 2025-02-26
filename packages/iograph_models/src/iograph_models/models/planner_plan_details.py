from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class PlannerPlanDetails(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	categoryDescriptions: Optional[PlannerCategoryDescriptions] = Field(default=None,alias="categoryDescriptions",)
	sharedWith: Optional[PlannerUserIds] = Field(default=None,alias="sharedWith",)

from .planner_category_descriptions import PlannerCategoryDescriptions
from .planner_user_ids import PlannerUserIds

