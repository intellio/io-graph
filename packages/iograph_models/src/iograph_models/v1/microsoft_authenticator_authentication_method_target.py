from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class MicrosoftAuthenticatorAuthenticationMethodTarget(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	isRegistrationRequired: Optional[bool] = Field(alias="isRegistrationRequired", default=None,)
	targetType: Optional[AuthenticationMethodTargetType | str] = Field(alias="targetType", default=None,)
	authenticationMode: Optional[MicrosoftAuthenticatorAuthenticationMode | str] = Field(alias="authenticationMode", default=None,)

from .authentication_method_target_type import AuthenticationMethodTargetType
from .microsoft_authenticator_authentication_mode import MicrosoftAuthenticatorAuthenticationMode

