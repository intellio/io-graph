from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PlannerFieldRules(BaseModel):
	defaultRules: Optional[list[str]] = Field(alias="defaultRules", default=None,)
	overrides: Optional[list[PlannerRuleOverride]] = Field(alias="overrides", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .planner_rule_override import PlannerRuleOverride

