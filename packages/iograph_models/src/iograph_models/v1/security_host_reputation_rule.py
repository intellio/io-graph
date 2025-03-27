from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityHostReputationRule(BaseModel):
	description: Optional[str] = Field(alias="description", default=None,)
	name: Optional[str] = Field(alias="name", default=None,)
	relatedDetailsUrl: Optional[str] = Field(alias="relatedDetailsUrl", default=None,)
	severity: Optional[SecurityHostReputationRuleSeverity | str] = Field(alias="severity", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .security_host_reputation_rule_severity import SecurityHostReputationRuleSeverity

