from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class TemporaryAccessPassAuthenticationMethodConfiguration(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.temporaryAccessPassAuthenticationMethodConfiguration"] = Field(alias="@odata.type", default="#microsoft.graph.temporaryAccessPassAuthenticationMethodConfiguration")
	excludeTargets: Optional[list[ExcludeTarget]] = Field(alias="excludeTargets", default=None,)
	state: Optional[AuthenticationMethodState | str] = Field(alias="state", default=None,)
	defaultLength: Optional[int] = Field(alias="defaultLength", default=None,)
	defaultLifetimeInMinutes: Optional[int] = Field(alias="defaultLifetimeInMinutes", default=None,)
	isUsableOnce: Optional[bool] = Field(alias="isUsableOnce", default=None,)
	maximumLifetimeInMinutes: Optional[int] = Field(alias="maximumLifetimeInMinutes", default=None,)
	minimumLifetimeInMinutes: Optional[int] = Field(alias="minimumLifetimeInMinutes", default=None,)
	includeTargets: Optional[list[Annotated[Union[MicrosoftAuthenticatorAuthenticationMethodTarget, SmsAuthenticationMethodTarget]],Field(discriminator="odata_type")]]] = Field(alias="includeTargets", default=None,)

from .exclude_target import ExcludeTarget
from .authentication_method_state import AuthenticationMethodState
from .microsoft_authenticator_authentication_method_target import MicrosoftAuthenticatorAuthenticationMethodTarget
from .sms_authentication_method_target import SmsAuthenticationMethodTarget

