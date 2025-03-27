from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AuthenticationStrengthRoot(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	combinations: Optional[list[AuthenticationMethodModes | str]] = Field(alias="combinations", default=None,)
	authenticationMethodModes: Optional[list[AuthenticationMethodModeDetail]] = Field(alias="authenticationMethodModes", default=None,)
	policies: Optional[list[AuthenticationStrengthPolicy]] = Field(alias="policies", default=None,)

from .authentication_method_modes import AuthenticationMethodModes
from .authentication_method_mode_detail import AuthenticationMethodModeDetail
from .authentication_strength_policy import AuthenticationStrengthPolicy

