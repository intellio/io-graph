from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class PlannerBucketPropertyRule(BaseModel):
	ruleKind: Optional[PlannerRuleKind | str] = Field(alias="ruleKind", default=None,)
	odata_type: Literal["#microsoft.graph.plannerBucketPropertyRule"] = Field(alias="@odata.type", default="#microsoft.graph.plannerBucketPropertyRule")
	order: Optional[list[str]] = Field(alias="order", default=None,)
	title: Optional[list[str]] = Field(alias="title", default=None,)

from .planner_rule_kind import PlannerRuleKind
