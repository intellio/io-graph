from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Authentication(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	emailMethods: list[EmailAuthenticationMethod] = Field(alias="emailMethods",)
	fido2Methods: list[Fido2AuthenticationMethod] = Field(alias="fido2Methods",)
	methods: list[AuthenticationMethod] = Field(alias="methods",)
	microsoftAuthenticatorMethods: list[MicrosoftAuthenticatorAuthenticationMethod] = Field(alias="microsoftAuthenticatorMethods",)
	operations: list[LongRunningOperation] = Field(alias="operations",)
	passwordMethods: list[PasswordAuthenticationMethod] = Field(alias="passwordMethods",)
	phoneMethods: list[PhoneAuthenticationMethod] = Field(alias="phoneMethods",)
	softwareOathMethods: list[SoftwareOathAuthenticationMethod] = Field(alias="softwareOathMethods",)
	temporaryAccessPassMethods: list[TemporaryAccessPassAuthenticationMethod] = Field(alias="temporaryAccessPassMethods",)
	windowsHelloForBusinessMethods: list[WindowsHelloForBusinessAuthenticationMethod] = Field(alias="windowsHelloForBusinessMethods",)

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

