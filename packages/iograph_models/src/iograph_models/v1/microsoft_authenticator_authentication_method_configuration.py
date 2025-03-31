from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class MicrosoftAuthenticatorAuthenticationMethodConfiguration(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.microsoftAuthenticatorAuthenticationMethodConfiguration"] = Field(alias="@odata.type", default="#microsoft.graph.microsoftAuthenticatorAuthenticationMethodConfiguration")
	excludeTargets: Optional[list[ExcludeTarget]] = Field(alias="excludeTargets", default=None,)
	state: Optional[AuthenticationMethodState | str] = Field(alias="state", default=None,)
	featureSettings: Optional[MicrosoftAuthenticatorFeatureSettings] = Field(alias="featureSettings", default=None,)
	isSoftwareOathEnabled: Optional[bool] = Field(alias="isSoftwareOathEnabled", default=None,)
	includeTargets: Optional[list[MicrosoftAuthenticatorAuthenticationMethodTarget]] = Field(alias="includeTargets", default=None,)

from .exclude_target import ExcludeTarget
from .authentication_method_state import AuthenticationMethodState
from .microsoft_authenticator_feature_settings import MicrosoftAuthenticatorFeatureSettings
from .microsoft_authenticator_authentication_method_target import MicrosoftAuthenticatorAuthenticationMethodTarget
