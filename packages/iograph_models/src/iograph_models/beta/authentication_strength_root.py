from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class AuthenticationStrengthRoot(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.authenticationStrengthRoot"] = Field(alias="@odata.type", default="#microsoft.graph.authenticationStrengthRoot")
	authenticationCombinations: Optional[list[AuthenticationMethodModes | str]] = Field(alias="authenticationCombinations", default=None,)
	combinations: Optional[list[AuthenticationMethodModes | str]] = Field(alias="combinations", default=None,)
	authenticationMethodModes: Optional[list[AuthenticationMethodModeDetail]] = Field(alias="authenticationMethodModes", default=None,)
	policies: Optional[list[AuthenticationStrengthPolicy]] = Field(alias="policies", default=None,)

from .authentication_method_modes import AuthenticationMethodModes
from .authentication_method_mode_detail import AuthenticationMethodModeDetail
from .authentication_strength_policy import AuthenticationStrengthPolicy
