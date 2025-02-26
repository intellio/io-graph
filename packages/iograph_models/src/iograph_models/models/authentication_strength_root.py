from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AuthenticationStrengthRoot(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	combinations: list[AuthenticationMethodModes] = Field(alias="combinations",)
	authenticationMethodModes: list[AuthenticationMethodModeDetail] = Field(alias="authenticationMethodModes",)
	policies: list[AuthenticationStrengthPolicy] = Field(alias="policies",)

from .authentication_method_modes import AuthenticationMethodModes
from .authentication_method_mode_detail import AuthenticationMethodModeDetail
from .authentication_strength_policy import AuthenticationStrengthPolicy

