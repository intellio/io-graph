from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Get_policy_setsPostRequest(BaseModel):
	policySetIds: Optional[list[str]] = Field(alias="policySetIds", default=None,)

