from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityHostReputation(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	classification: Optional[SecurityHostReputationClassification | str] = Field(alias="classification",default=None,)
	rules: Optional[list[SecurityHostReputationRule]] = Field(alias="rules",default=None,)
	score: Optional[int] = Field(alias="score",default=None,)

from .security_host_reputation_classification import SecurityHostReputationClassification
from .security_host_reputation_rule import SecurityHostReputationRule

