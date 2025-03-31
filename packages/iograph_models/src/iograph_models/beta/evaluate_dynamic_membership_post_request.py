from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Evaluate_dynamic_membershipPostRequest(BaseModel):
	memberId: Optional[str] = Field(alias="memberId", default=None,)
	membershipRule: Optional[str] = Field(alias="membershipRule", default=None,)

