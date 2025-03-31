from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field


class PlannerDeltaCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[PlannerAssignedToTaskBoardTaskFormat, PlannerBucket, PlannerBucketTaskBoardTaskFormat, PlannerPlan, PlannerPlanDetails, PlannerProgressTaskBoardTaskFormat, BusinessScenarioTask, PlannerTaskDetails, PlannerUser],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .planner_assigned_to_task_board_task_format import PlannerAssignedToTaskBoardTaskFormat
from .planner_bucket import PlannerBucket
from .planner_bucket_task_board_task_format import PlannerBucketTaskBoardTaskFormat
from .planner_plan import PlannerPlan
from .planner_plan_details import PlannerPlanDetails
from .planner_progress_task_board_task_format import PlannerProgressTaskBoardTaskFormat
from .business_scenario_task import BusinessScenarioTask
from .planner_task_details import PlannerTaskDetails
from .planner_user import PlannerUser
