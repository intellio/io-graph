from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class GovernancePolicyTemplate(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	policy: Optional[GovernancePolicy] = Field(alias="policy", default=None,)
	settings: Optional[BusinessFlowSettings] = Field(alias="settings", default=None,)

from .governance_policy import GovernancePolicy
from .business_flow_settings import BusinessFlowSettings

