from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class SecurityHostReputation(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.security.hostReputation"] = Field(alias="@odata.type", default="#microsoft.graph.security.hostReputation")
	classification: Optional[SecurityHostReputationClassification | str] = Field(alias="classification", default=None,)
	rules: Optional[list[SecurityHostReputationRule]] = Field(alias="rules", default=None,)
	score: Optional[int] = Field(alias="score", default=None,)

from .security_host_reputation_classification import SecurityHostReputationClassification
from .security_host_reputation_rule import SecurityHostReputationRule
