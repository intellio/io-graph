from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class MicrosoftAuthenticatorAuthenticationMethodTarget(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.microsoftAuthenticatorAuthenticationMethodTarget"] = Field(alias="@odata.type", default="#microsoft.graph.microsoftAuthenticatorAuthenticationMethodTarget")
	isRegistrationRequired: Optional[bool] = Field(alias="isRegistrationRequired", default=None,)
	targetType: Optional[AuthenticationMethodTargetType | str] = Field(alias="targetType", default=None,)
	authenticationMode: Optional[MicrosoftAuthenticatorAuthenticationMode | str] = Field(alias="authenticationMode", default=None,)

from .authentication_method_target_type import AuthenticationMethodTargetType
from .microsoft_authenticator_authentication_mode import MicrosoftAuthenticatorAuthenticationMode
