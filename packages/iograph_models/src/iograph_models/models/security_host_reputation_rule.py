from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SecurityHostReputationRule(BaseModel):
	description: Optional[str] = Field(default=None,alias="description",)
	name: Optional[str] = Field(default=None,alias="name",)
	relatedDetailsUrl: Optional[str] = Field(default=None,alias="relatedDetailsUrl",)
	severity: Optional[SecurityHostReputationRuleSeverity] = Field(default=None,alias="severity",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .security_host_reputation_rule_severity import SecurityHostReputationRuleSeverity

