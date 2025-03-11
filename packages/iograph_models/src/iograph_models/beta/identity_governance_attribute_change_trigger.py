from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class IdentityGovernanceAttributeChangeTrigger(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	triggerAttributes: Optional[list[IdentityGovernanceTriggerAttribute]] = Field(alias="triggerAttributes",default=None,)

from .identity_governance_trigger_attribute import IdentityGovernanceTriggerAttribute

