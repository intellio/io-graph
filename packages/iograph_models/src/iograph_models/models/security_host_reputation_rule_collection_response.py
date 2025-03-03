from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SecurityHostReputationRuleCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[SecurityHostReputationRule]] = Field(default=None,alias="value",)

from .security_host_reputation_rule import SecurityHostReputationRule

