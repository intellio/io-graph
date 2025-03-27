from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ConditionalAccessGrantControls(BaseModel):
	builtInControls: Optional[list[ConditionalAccessGrantControl | str]] = Field(alias="builtInControls", default=None,)
	customAuthenticationFactors: Optional[list[str]] = Field(alias="customAuthenticationFactors", default=None,)
	operator: Optional[str] = Field(alias="operator", default=None,)
	termsOfUse: Optional[list[str]] = Field(alias="termsOfUse", default=None,)
	authenticationStrength: Optional[AuthenticationStrengthPolicy] = Field(alias="authenticationStrength", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .conditional_access_grant_control import ConditionalAccessGrantControl
from .authentication_strength_policy import AuthenticationStrengthPolicy

