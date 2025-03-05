from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class MicrosoftAuthenticatorAuthenticationMethodTarget(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	isRegistrationRequired: Optional[bool] = Field(default=None,alias="isRegistrationRequired",)
	targetType: Optional[AuthenticationMethodTargetType] = Field(default=None,alias="targetType",)
	authenticationMode: Optional[MicrosoftAuthenticatorAuthenticationMode] = Field(default=None,alias="authenticationMode",)

from .authentication_method_target_type import AuthenticationMethodTargetType
from .microsoft_authenticator_authentication_mode import MicrosoftAuthenticatorAuthenticationMode

