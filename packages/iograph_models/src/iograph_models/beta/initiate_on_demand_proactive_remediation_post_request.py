from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Initiate_on_demand_proactive_remediationPostRequest(BaseModel):
	scriptPolicyId: Optional[str] = Field(alias="scriptPolicyId", default=None,)

