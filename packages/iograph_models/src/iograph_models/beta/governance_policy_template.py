from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class GovernancePolicyTemplate(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.governancePolicyTemplate"] = Field(alias="@odata.type",)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	policy: Optional[GovernancePolicy] = Field(alias="policy", default=None,)
	settings: Optional[BusinessFlowSettings] = Field(alias="settings", default=None,)

from .governance_policy import GovernancePolicy
from .business_flow_settings import BusinessFlowSettings
