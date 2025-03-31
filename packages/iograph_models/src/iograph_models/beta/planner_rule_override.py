from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class PlannerRuleOverride(BaseModel):
	name: Optional[str] = Field(alias="name", default=None,)
	rules: Optional[list[str]] = Field(alias="rules", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

