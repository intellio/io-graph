from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class AuthenticationStrengthPolicy(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	allowedCombinations: Optional[list[AuthenticationMethodModes]] = Field(default=None,alias="allowedCombinations",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	modifiedDateTime: Optional[datetime] = Field(default=None,alias="modifiedDateTime",)
	policyType: Optional[AuthenticationStrengthPolicyType] = Field(default=None,alias="policyType",)
	requirementsSatisfied: Optional[AuthenticationStrengthRequirements] = Field(default=None,alias="requirementsSatisfied",)
	combinationConfigurations: Optional[list[AuthenticationCombinationConfiguration]] = Field(default=None,alias="combinationConfigurations",)

from .authentication_method_modes import AuthenticationMethodModes
from .authentication_strength_policy_type import AuthenticationStrengthPolicyType
from .authentication_strength_requirements import AuthenticationStrengthRequirements
from .authentication_combination_configuration import AuthenticationCombinationConfiguration

