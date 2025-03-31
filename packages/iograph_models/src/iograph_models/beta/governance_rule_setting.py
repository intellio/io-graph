from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class GovernanceRuleSetting(BaseModel):
	ruleIdentifier: Optional[str] = Field(alias="ruleIdentifier", default=None,)
	setting: Optional[str] = Field(alias="setting", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

