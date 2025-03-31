from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class IdentityGovernanceOnDemandExecutionOnly(BaseModel):
	odata_type: Literal["#microsoft.graph.identityGovernance.onDemandExecutionOnly"] = Field(alias="@odata.type", default="#microsoft.graph.identityGovernance.onDemandExecutionOnly")

