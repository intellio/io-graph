from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class IdentityGovernanceRuleBasedSubjectSet(BaseModel):
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	rule: Optional[str] = Field(default=None,alias="rule",)


