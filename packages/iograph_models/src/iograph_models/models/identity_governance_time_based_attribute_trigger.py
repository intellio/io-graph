from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class IdentityGovernanceTimeBasedAttributeTrigger(BaseModel):
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	offsetInDays: Optional[int] = Field(default=None,alias="offsetInDays",)
	timeBasedAttribute: Optional[IdentityGovernanceWorkflowTriggerTimeBasedAttribute] = Field(default=None,alias="timeBasedAttribute",)

from .identity_governance_workflow_trigger_time_based_attribute import IdentityGovernanceWorkflowTriggerTimeBasedAttribute

