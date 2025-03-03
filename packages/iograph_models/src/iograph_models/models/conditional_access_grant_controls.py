from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ConditionalAccessGrantControls(BaseModel):
	builtInControls: Optional[list[ConditionalAccessGrantControl]] = Field(default=None,alias="builtInControls",)
	customAuthenticationFactors: Optional[list[str]] = Field(default=None,alias="customAuthenticationFactors",)
	operator: Optional[str] = Field(default=None,alias="operator",)
	termsOfUse: Optional[list[str]] = Field(default=None,alias="termsOfUse",)
	authenticationStrength: Optional[AuthenticationStrengthPolicy] = Field(default=None,alias="authenticationStrength",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .conditional_access_grant_control import ConditionalAccessGrantControl
from .authentication_strength_policy import AuthenticationStrengthPolicy

