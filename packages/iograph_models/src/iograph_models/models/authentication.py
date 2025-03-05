from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Authentication(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	emailMethods: Optional[list[EmailAuthenticationMethod]] = Field(default=None,alias="emailMethods",)
	fido2Methods: Optional[list[Fido2AuthenticationMethod]] = Field(default=None,alias="fido2Methods",)
	methods: SerializeAsAny[Optional[list[AuthenticationMethod]]] = Field(default=None,alias="methods",)
	microsoftAuthenticatorMethods: Optional[list[MicrosoftAuthenticatorAuthenticationMethod]] = Field(default=None,alias="microsoftAuthenticatorMethods",)
	operations: SerializeAsAny[Optional[list[LongRunningOperation]]] = Field(default=None,alias="operations",)
	passwordMethods: Optional[list[PasswordAuthenticationMethod]] = Field(default=None,alias="passwordMethods",)
	phoneMethods: Optional[list[PhoneAuthenticationMethod]] = Field(default=None,alias="phoneMethods",)
	softwareOathMethods: Optional[list[SoftwareOathAuthenticationMethod]] = Field(default=None,alias="softwareOathMethods",)
	temporaryAccessPassMethods: Optional[list[TemporaryAccessPassAuthenticationMethod]] = Field(default=None,alias="temporaryAccessPassMethods",)
	windowsHelloForBusinessMethods: Optional[list[WindowsHelloForBusinessAuthenticationMethod]] = Field(default=None,alias="windowsHelloForBusinessMethods",)

from .email_authentication_method import EmailAuthenticationMethod
from .fido2_authentication_method import Fido2AuthenticationMethod
from .authentication_method import AuthenticationMethod
from .microsoft_authenticator_authentication_method import MicrosoftAuthenticatorAuthenticationMethod
from .long_running_operation import LongRunningOperation
from .password_authentication_method import PasswordAuthenticationMethod
from .phone_authentication_method import PhoneAuthenticationMethod
from .software_oath_authentication_method import SoftwareOathAuthenticationMethod
from .temporary_access_pass_authentication_method import TemporaryAccessPassAuthenticationMethod
from .windows_hello_for_business_authentication_method import WindowsHelloForBusinessAuthenticationMethod

