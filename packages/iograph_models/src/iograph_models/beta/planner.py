from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from pydantic import BaseModel, Field


class Planner(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.planner"] = Field(alias="@odata.type", default="#microsoft.graph.planner")
	buckets: Optional[list[PlannerBucket]] = Field(alias="buckets", default=None,)
	plans: Optional[list[PlannerPlan]] = Field(alias="plans", default=None,)
	rosters: Optional[list[PlannerRoster]] = Field(alias="rosters", default=None,)
	tasks: Optional[list[Annotated[Union[BusinessScenarioTask],Field(discriminator="odata_type")]]] = Field(alias="tasks", default=None,)

from .planner_bucket import PlannerBucket
from .planner_plan import PlannerPlan
from .planner_roster import PlannerRoster
from .business_scenario_task import BusinessScenarioTask
