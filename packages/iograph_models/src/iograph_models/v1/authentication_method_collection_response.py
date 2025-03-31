from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field


class AuthenticationMethodCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[EmailAuthenticationMethod, Fido2AuthenticationMethod, MicrosoftAuthenticatorAuthenticationMethod, PasswordAuthenticationMethod, PhoneAuthenticationMethod, SoftwareOathAuthenticationMethod, TemporaryAccessPassAuthenticationMethod, WindowsHelloForBusinessAuthenticationMethod],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .email_authentication_method import EmailAuthenticationMethod
from .fido2_authentication_method import Fido2AuthenticationMethod
from .microsoft_authenticator_authentication_method import MicrosoftAuthenticatorAuthenticationMethod
from .password_authentication_method import PasswordAuthenticationMethod
from .phone_authentication_method import PhoneAuthenticationMethod
from .software_oath_authentication_method import SoftwareOathAuthenticationMethod
from .temporary_access_pass_authentication_method import TemporaryAccessPassAuthenticationMethod
from .windows_hello_for_business_authentication_method import WindowsHelloForBusinessAuthenticationMethod
