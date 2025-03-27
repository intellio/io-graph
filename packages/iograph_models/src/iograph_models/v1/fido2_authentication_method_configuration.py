from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class Fido2AuthenticationMethodConfiguration(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.fido2AuthenticationMethodConfiguration"] = Field(alias="@odata.type", default="#microsoft.graph.fido2AuthenticationMethodConfiguration")
	excludeTargets: Optional[list[ExcludeTarget]] = Field(alias="excludeTargets", default=None,)
	state: Optional[AuthenticationMethodState | str] = Field(alias="state", default=None,)
	isAttestationEnforced: Optional[bool] = Field(alias="isAttestationEnforced", default=None,)
	isSelfServiceRegistrationAllowed: Optional[bool] = Field(alias="isSelfServiceRegistrationAllowed", default=None,)
	keyRestrictions: Optional[Fido2KeyRestrictions] = Field(alias="keyRestrictions", default=None,)
	includeTargets: Optional[list[Annotated[Union[MicrosoftAuthenticatorAuthenticationMethodTarget, SmsAuthenticationMethodTarget],Field(discriminator="odata_type")]]] = Field(alias="includeTargets", default=None,)

from .exclude_target import ExcludeTarget
from .authentication_method_state import AuthenticationMethodState
from .fido2_key_restrictions import Fido2KeyRestrictions
from .microsoft_authenticator_authentication_method_target import MicrosoftAuthenticatorAuthenticationMethodTarget
from .sms_authentication_method_target import SmsAuthenticationMethodTarget

