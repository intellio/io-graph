from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class IdentityGovernanceTimeBasedAttributeTrigger(BaseModel):
	odata_type: Literal["#microsoft.graph.identityGovernance.timeBasedAttributeTrigger"] = Field(alias="@odata.type", default="#microsoft.graph.identityGovernance.timeBasedAttributeTrigger")
	offsetInDays: Optional[int] = Field(alias="offsetInDays", default=None,)
	timeBasedAttribute: Optional[IdentityGovernanceWorkflowTriggerTimeBasedAttribute | str] = Field(alias="timeBasedAttribute", default=None,)

from .identity_governance_workflow_trigger_time_based_attribute import IdentityGovernanceWorkflowTriggerTimeBasedAttribute

