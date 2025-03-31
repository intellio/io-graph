from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from pydantic import BaseModel, Field


class IdentityGovernanceTriggerAndScopeBasedConditions(BaseModel):
	odata_type: Literal["#microsoft.graph.identityGovernance.triggerAndScopeBasedConditions"] = Field(alias="@odata.type", default="#microsoft.graph.identityGovernance.triggerAndScopeBasedConditions")
	scope: Optional[Union[IdentityGovernanceGroupBasedSubjectSet, IdentityGovernanceRuleBasedSubjectSet]] = Field(alias="scope", default=None,discriminator="odata_type", )
	trigger: Optional[Union[IdentityGovernanceAttributeChangeTrigger, IdentityGovernanceMembershipChangeTrigger, IdentityGovernanceTimeBasedAttributeTrigger]] = Field(alias="trigger", default=None,discriminator="odata_type", )

from .identity_governance_group_based_subject_set import IdentityGovernanceGroupBasedSubjectSet
from .identity_governance_rule_based_subject_set import IdentityGovernanceRuleBasedSubjectSet
from .identity_governance_attribute_change_trigger import IdentityGovernanceAttributeChangeTrigger
from .identity_governance_membership_change_trigger import IdentityGovernanceMembershipChangeTrigger
from .identity_governance_time_based_attribute_trigger import IdentityGovernanceTimeBasedAttributeTrigger
