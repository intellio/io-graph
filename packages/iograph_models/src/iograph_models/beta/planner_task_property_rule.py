from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class PlannerTaskPropertyRule(BaseModel):
	ruleKind: Optional[PlannerRuleKind | str] = Field(alias="ruleKind", default=None,)
	odata_type: Literal["#microsoft.graph.plannerTaskPropertyRule"] = Field(alias="@odata.type", default="#microsoft.graph.plannerTaskPropertyRule")
	appliedCategories: Optional[PlannerFieldRules] = Field(alias="appliedCategories", default=None,)
	approvalAttachment: Optional[PlannerFieldRules] = Field(alias="approvalAttachment", default=None,)
	assignments: Optional[PlannerFieldRules] = Field(alias="assignments", default=None,)
	checkLists: Optional[PlannerFieldRules] = Field(alias="checkLists", default=None,)
	completionRequirements: Optional[list[str]] = Field(alias="completionRequirements", default=None,)
	delete: Optional[list[str]] = Field(alias="delete", default=None,)
	dueDate: Optional[list[str]] = Field(alias="dueDate", default=None,)
	forms: Optional[PlannerFieldRules] = Field(alias="forms", default=None,)
	move: Optional[list[str]] = Field(alias="move", default=None,)
	notes: Optional[list[str]] = Field(alias="notes", default=None,)
	order: Optional[list[str]] = Field(alias="order", default=None,)
	percentComplete: Optional[list[str]] = Field(alias="percentComplete", default=None,)
	previewType: Optional[list[str]] = Field(alias="previewType", default=None,)
	priority: Optional[list[str]] = Field(alias="priority", default=None,)
	references: Optional[PlannerFieldRules] = Field(alias="references", default=None,)
	startDate: Optional[list[str]] = Field(alias="startDate", default=None,)
	title: Optional[list[str]] = Field(alias="title", default=None,)

from .planner_rule_kind import PlannerRuleKind
from .planner_field_rules import PlannerFieldRules
