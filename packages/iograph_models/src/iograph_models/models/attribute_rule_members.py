from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AttributeRuleMembers(BaseModel):
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	description: Optional[str] = Field(default=None,alias="description",)
	membershipRule: Optional[str] = Field(default=None,alias="membershipRule",)


