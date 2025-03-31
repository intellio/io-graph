from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from pydantic import BaseModel, Field


class PlannerUser(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.plannerUser"] = Field(alias="@odata.type",)
	favoritePlanReferences: Optional[PlannerFavoritePlanReferenceCollection] = Field(alias="favoritePlanReferences", default=None,)
	recentPlanReferences: Optional[PlannerRecentPlanReferenceCollection] = Field(alias="recentPlanReferences", default=None,)
	all: Optional[list[Annotated[Union[PlannerAssignedToTaskBoardTaskFormat, PlannerBucket, PlannerBucketTaskBoardTaskFormat, PlannerPlan, PlannerPlanDetails, PlannerProgressTaskBoardTaskFormat, BusinessScenarioTask, PlannerTaskDetails, PlannerUser],Field(discriminator="odata_type")]]] = Field(alias="all", default=None,)
	favoritePlans: Optional[list[PlannerPlan]] = Field(alias="favoritePlans", default=None,)
	myDayTasks: Optional[list[Annotated[Union[BusinessScenarioTask],Field(discriminator="odata_type")]]] = Field(alias="myDayTasks", default=None,)
	plans: Optional[list[PlannerPlan]] = Field(alias="plans", default=None,)
	recentPlans: Optional[list[PlannerPlan]] = Field(alias="recentPlans", default=None,)
	rosterPlans: Optional[list[PlannerPlan]] = Field(alias="rosterPlans", default=None,)
	tasks: Optional[list[Annotated[Union[BusinessScenarioTask],Field(discriminator="odata_type")]]] = Field(alias="tasks", default=None,)

from .planner_favorite_plan_reference_collection import PlannerFavoritePlanReferenceCollection
from .planner_recent_plan_reference_collection import PlannerRecentPlanReferenceCollection
from .planner_assigned_to_task_board_task_format import PlannerAssignedToTaskBoardTaskFormat
from .planner_bucket import PlannerBucket
from .planner_bucket_task_board_task_format import PlannerBucketTaskBoardTaskFormat
from .planner_plan import PlannerPlan
from .planner_plan_details import PlannerPlanDetails
from .planner_progress_task_board_task_format import PlannerProgressTaskBoardTaskFormat
from .business_scenario_task import BusinessScenarioTask
from .planner_task_details import PlannerTaskDetails
