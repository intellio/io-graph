from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class IdentityGovernanceAttributeChangeTrigger(BaseModel):
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	triggerAttributes: Optional[list[IdentityGovernanceTriggerAttribute]] = Field(default=None,alias="triggerAttributes",)

from .identity_governance_trigger_attribute import IdentityGovernanceTriggerAttribute

