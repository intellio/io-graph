from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AuthenticationStrength(BaseModel):
	authenticationStrengthId: Optional[str] = Field(alias="authenticationStrengthId", default=None,)
	authenticationStrengthResult: Optional[AuthenticationStrengthResult | str] = Field(alias="authenticationStrengthResult", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .authentication_strength_result import AuthenticationStrengthResult

