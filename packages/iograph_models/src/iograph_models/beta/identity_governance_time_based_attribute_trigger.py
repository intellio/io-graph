from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class IdentityGovernanceTimeBasedAttributeTrigger(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	offsetInDays: Optional[int] = Field(alias="offsetInDays",default=None,)
	timeBasedAttribute: Optional[IdentityGovernanceWorkflowTriggerTimeBasedAttribute | str] = Field(alias="timeBasedAttribute",default=None,)

from .identity_governance_workflow_trigger_time_based_attribute import IdentityGovernanceWorkflowTriggerTimeBasedAttribute

