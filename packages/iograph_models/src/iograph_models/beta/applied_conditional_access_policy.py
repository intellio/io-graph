from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AppliedConditionalAccessPolicy(BaseModel):
	authenticationStrength: Optional[AuthenticationStrength] = Field(alias="authenticationStrength", default=None,)
	conditionsNotSatisfied: Optional[ConditionalAccessConditions | str] = Field(alias="conditionsNotSatisfied", default=None,)
	conditionsSatisfied: Optional[ConditionalAccessConditions | str] = Field(alias="conditionsSatisfied", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	enforcedGrantControls: Optional[list[str]] = Field(alias="enforcedGrantControls", default=None,)
	enforcedSessionControls: Optional[list[str]] = Field(alias="enforcedSessionControls", default=None,)
	excludeRulesSatisfied: Optional[list[ConditionalAccessRuleSatisfied]] = Field(alias="excludeRulesSatisfied", default=None,)
	id: Optional[str] = Field(alias="id", default=None,)
	includeRulesSatisfied: Optional[list[ConditionalAccessRuleSatisfied]] = Field(alias="includeRulesSatisfied", default=None,)
	result: Optional[AppliedConditionalAccessPolicyResult | str] = Field(alias="result", default=None,)
	sessionControlsNotSatisfied: Optional[list[str]] = Field(alias="sessionControlsNotSatisfied", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .authentication_strength import AuthenticationStrength
from .conditional_access_conditions import ConditionalAccessConditions
from .conditional_access_rule_satisfied import ConditionalAccessRuleSatisfied
from .applied_conditional_access_policy_result import AppliedConditionalAccessPolicyResult
