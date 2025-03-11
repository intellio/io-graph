from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PlannerTaskCompletionRequirementDetails(BaseModel):
	approvalRequirement: Optional[PlannerApprovalRequirement] = Field(alias="approvalRequirement",default=None,)
	checklistRequirement: Optional[PlannerChecklistRequirement] = Field(alias="checklistRequirement",default=None,)
	formsRequirement: Optional[PlannerFormsRequirement] = Field(alias="formsRequirement",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .planner_approval_requirement import PlannerApprovalRequirement
from .planner_checklist_requirement import PlannerChecklistRequirement
from .planner_forms_requirement import PlannerFormsRequirement

