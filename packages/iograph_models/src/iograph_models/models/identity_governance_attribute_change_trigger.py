from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class IdentityGovernanceAttributeChangeTrigger(BaseModel):
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	triggerAttributes: list[IdentityGovernanceTriggerAttribute] = Field(alias="triggerAttributes",)

from .identity_governance_trigger_attribute import IdentityGovernanceTriggerAttribute

