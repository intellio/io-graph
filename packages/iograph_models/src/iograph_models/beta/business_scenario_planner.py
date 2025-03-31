from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class BusinessScenarioPlanner(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.businessScenarioPlanner"] = Field(alias="@odata.type",)
	planConfiguration: Optional[PlannerPlanConfiguration] = Field(alias="planConfiguration", default=None,)
	taskConfiguration: Optional[PlannerTaskConfiguration] = Field(alias="taskConfiguration", default=None,)
	tasks: Optional[list[BusinessScenarioTask]] = Field(alias="tasks", default=None,)

from .planner_plan_configuration import PlannerPlanConfiguration
from .planner_task_configuration import PlannerTaskConfiguration
from .business_scenario_task import BusinessScenarioTask
