from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PlannerBucketPropertyRule(BaseModel):
	ruleKind: Optional[PlannerRuleKind | str] = Field(alias="ruleKind",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	order: Optional[list[str]] = Field(alias="order",default=None,)
	title: Optional[list[str]] = Field(alias="title",default=None,)

from .planner_rule_kind import PlannerRuleKind

