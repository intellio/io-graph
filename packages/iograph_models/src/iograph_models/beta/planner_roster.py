from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class PlannerRoster(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.plannerRoster"] = Field(alias="@odata.type",)
	assignedSensitivityLabel: Optional[SensitivityLabelAssignment] = Field(alias="assignedSensitivityLabel", default=None,)
	members: Optional[list[PlannerRosterMember]] = Field(alias="members", default=None,)
	plans: Optional[list[PlannerPlan]] = Field(alias="plans", default=None,)

from .sensitivity_label_assignment import SensitivityLabelAssignment
from .planner_roster_member import PlannerRosterMember
from .planner_plan import PlannerPlan
