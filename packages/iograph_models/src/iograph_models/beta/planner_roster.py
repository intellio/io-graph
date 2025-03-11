from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PlannerRoster(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	assignedSensitivityLabel: Optional[SensitivityLabelAssignment] = Field(alias="assignedSensitivityLabel",default=None,)
	members: Optional[list[PlannerRosterMember]] = Field(alias="members",default=None,)
	plans: Optional[list[PlannerPlan]] = Field(alias="plans",default=None,)

from .sensitivity_label_assignment import SensitivityLabelAssignment
from .planner_roster_member import PlannerRosterMember
from .planner_plan import PlannerPlan

