from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field


class AuthenticationMethodTargetCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[MicrosoftAuthenticatorAuthenticationMethodTarget, SmsAuthenticationMethodTarget],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .microsoft_authenticator_authentication_method_target import MicrosoftAuthenticatorAuthenticationMethodTarget
from .sms_authentication_method_target import SmsAuthenticationMethodTarget
