from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ConditionalAccessGrantControls(BaseModel):
	builtInControls: list[ConditionalAccessGrantControl] = Field(alias="builtInControls",)
	customAuthenticationFactors: list[str] = Field(alias="customAuthenticationFactors",)
	operator: Optional[str] = Field(default=None,alias="operator",)
	termsOfUse: list[str] = Field(alias="termsOfUse",)
	authenticationStrength: Optional[AuthenticationStrengthPolicy] = Field(default=None,alias="authenticationStrength",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .conditional_access_grant_control import ConditionalAccessGrantControl
from .authentication_strength_policy import AuthenticationStrengthPolicy

