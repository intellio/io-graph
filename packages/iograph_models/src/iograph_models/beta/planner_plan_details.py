from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PlannerPlanDetails(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	categoryDescriptions: Optional[PlannerCategoryDescriptions] = Field(alias="categoryDescriptions", default=None,)
	contextDetails: Optional[PlannerPlanContextDetailsCollection] = Field(alias="contextDetails", default=None,)
	sharedWith: Optional[PlannerUserIds] = Field(alias="sharedWith", default=None,)

from .planner_category_descriptions import PlannerCategoryDescriptions
from .planner_plan_context_details_collection import PlannerPlanContextDetailsCollection
from .planner_user_ids import PlannerUserIds

