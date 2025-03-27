from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class IdentityGovernanceAttributeChangeTrigger(BaseModel):
	odata_type: Literal["#microsoft.graph.identityGovernance.attributeChangeTrigger"] = Field(alias="@odata.type", default="#microsoft.graph.identityGovernance.attributeChangeTrigger")
	triggerAttributes: Optional[list[IdentityGovernanceTriggerAttribute]] = Field(alias="triggerAttributes", default=None,)

from .identity_governance_trigger_attribute import IdentityGovernanceTriggerAttribute

