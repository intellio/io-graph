from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class PlannerPlanPropertyRule(BaseModel):
	ruleKind: Optional[PlannerRuleKind | str] = Field(alias="ruleKind", default=None,)
	odata_type: Literal["#microsoft.graph.plannerPlanPropertyRule"] = Field(alias="@odata.type", default="#microsoft.graph.plannerPlanPropertyRule")
	buckets: Optional[list[str]] = Field(alias="buckets", default=None,)
	categoryDescriptions: Optional[PlannerFieldRules] = Field(alias="categoryDescriptions", default=None,)
	tasks: Optional[list[str]] = Field(alias="tasks", default=None,)
	title: Optional[PlannerFieldRules] = Field(alias="title", default=None,)

from .planner_rule_kind import PlannerRuleKind
from .planner_field_rules import PlannerFieldRules
from .planner_field_rules import PlannerFieldRules

