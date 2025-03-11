from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PlannerUser(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	favoritePlanReferences: Optional[PlannerFavoritePlanReferenceCollection] = Field(alias="favoritePlanReferences",default=None,)
	recentPlanReferences: Optional[PlannerRecentPlanReferenceCollection] = Field(alias="recentPlanReferences",default=None,)
	all: SerializeAsAny[Optional[list[PlannerDelta]]] = Field(alias="all",default=None,)
	favoritePlans: Optional[list[PlannerPlan]] = Field(alias="favoritePlans",default=None,)
	myDayTasks: SerializeAsAny[Optional[list[PlannerTask]]] = Field(alias="myDayTasks",default=None,)
	plans: Optional[list[PlannerPlan]] = Field(alias="plans",default=None,)
	recentPlans: Optional[list[PlannerPlan]] = Field(alias="recentPlans",default=None,)
	rosterPlans: Optional[list[PlannerPlan]] = Field(alias="rosterPlans",default=None,)
	tasks: SerializeAsAny[Optional[list[PlannerTask]]] = Field(alias="tasks",default=None,)

from .planner_favorite_plan_reference_collection import PlannerFavoritePlanReferenceCollection
from .planner_recent_plan_reference_collection import PlannerRecentPlanReferenceCollection
from .planner_delta import PlannerDelta
from .planner_plan import PlannerPlan
from .planner_task import PlannerTask
from .planner_plan import PlannerPlan
from .planner_plan import PlannerPlan
from .planner_plan import PlannerPlan
from .planner_task import PlannerTask

