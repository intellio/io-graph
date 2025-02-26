from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SecurityHostReputation(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	classification: Optional[SecurityHostReputationClassification] = Field(default=None,alias="classification",)
	rules: list[SecurityHostReputationRule] = Field(alias="rules",)
	score: Optional[int] = Field(default=None,alias="score",)

from .security_host_reputation_classification import SecurityHostReputationClassification
from .security_host_reputation_rule import SecurityHostReputationRule

