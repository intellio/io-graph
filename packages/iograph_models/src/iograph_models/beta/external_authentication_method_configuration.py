from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from pydantic import BaseModel, Field


class ExternalAuthenticationMethodConfiguration(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.externalAuthenticationMethodConfiguration"] = Field(alias="@odata.type", default="#microsoft.graph.externalAuthenticationMethodConfiguration")
	excludeTargets: Optional[list[ExcludeTarget]] = Field(alias="excludeTargets", default=None,)
	state: Optional[AuthenticationMethodState | str] = Field(alias="state", default=None,)
	appId: Optional[str] = Field(alias="appId", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	openIdConnectSetting: Optional[OpenIdConnectSetting] = Field(alias="openIdConnectSetting", default=None,)
	includeTargets: Optional[list[Annotated[Union[MicrosoftAuthenticatorAuthenticationMethodTarget, PasskeyAuthenticationMethodTarget, SmsAuthenticationMethodTarget, VoiceAuthenticationMethodTarget],Field(discriminator="odata_type")]]] = Field(alias="includeTargets", default=None,)

from .exclude_target import ExcludeTarget
from .authentication_method_state import AuthenticationMethodState
from .open_id_connect_setting import OpenIdConnectSetting
from .microsoft_authenticator_authentication_method_target import MicrosoftAuthenticatorAuthenticationMethodTarget
from .passkey_authentication_method_target import PasskeyAuthenticationMethodTarget
from .sms_authentication_method_target import SmsAuthenticationMethodTarget
from .voice_authentication_method_target import VoiceAuthenticationMethodTarget
