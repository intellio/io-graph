from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class BusinessScenarioPlanner(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	planConfiguration: Optional[PlannerPlanConfiguration] = Field(alias="planConfiguration",default=None,)
	taskConfiguration: Optional[PlannerTaskConfiguration] = Field(alias="taskConfiguration",default=None,)
	tasks: Optional[list[BusinessScenarioTask]] = Field(alias="tasks",default=None,)

from .planner_plan_configuration import PlannerPlanConfiguration
from .planner_task_configuration import PlannerTaskConfiguration
from .business_scenario_task import BusinessScenarioTask

