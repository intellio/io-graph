from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Authentication(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	requirements: Optional[StrongAuthenticationRequirements] = Field(alias="requirements",default=None,)
	signInPreferences: Optional[SignInPreferences] = Field(alias="signInPreferences",default=None,)
	emailMethods: Optional[list[EmailAuthenticationMethod]] = Field(alias="emailMethods",default=None,)
	fido2Methods: Optional[list[Fido2AuthenticationMethod]] = Field(alias="fido2Methods",default=None,)
	hardwareOathMethods: Optional[list[HardwareOathAuthenticationMethod]] = Field(alias="hardwareOathMethods",default=None,)
	methods: SerializeAsAny[Optional[list[AuthenticationMethod]]] = Field(alias="methods",default=None,)
	microsoftAuthenticatorMethods: Optional[list[MicrosoftAuthenticatorAuthenticationMethod]] = Field(alias="microsoftAuthenticatorMethods",default=None,)
	operations: SerializeAsAny[Optional[list[LongRunningOperation]]] = Field(alias="operations",default=None,)
	passwordlessMicrosoftAuthenticatorMethods: Optional[list[PasswordlessMicrosoftAuthenticatorAuthenticationMethod]] = Field(alias="passwordlessMicrosoftAuthenticatorMethods",default=None,)
	passwordMethods: Optional[list[PasswordAuthenticationMethod]] = Field(alias="passwordMethods",default=None,)
	phoneMethods: Optional[list[PhoneAuthenticationMethod]] = Field(alias="phoneMethods",default=None,)
	platformCredentialMethods: Optional[list[PlatformCredentialAuthenticationMethod]] = Field(alias="platformCredentialMethods",default=None,)
	softwareOathMethods: Optional[list[SoftwareOathAuthenticationMethod]] = Field(alias="softwareOathMethods",default=None,)
	temporaryAccessPassMethods: Optional[list[TemporaryAccessPassAuthenticationMethod]] = Field(alias="temporaryAccessPassMethods",default=None,)
	windowsHelloForBusinessMethods: Optional[list[WindowsHelloForBusinessAuthenticationMethod]] = Field(alias="windowsHelloForBusinessMethods",default=None,)

from .strong_authentication_requirements import StrongAuthenticationRequirements
from .sign_in_preferences import SignInPreferences
from .email_authentication_method import EmailAuthenticationMethod
from .fido2_authentication_method import Fido2AuthenticationMethod
from .hardware_oath_authentication_method import HardwareOathAuthenticationMethod
from .authentication_method import AuthenticationMethod
from .microsoft_authenticator_authentication_method import MicrosoftAuthenticatorAuthenticationMethod
from .long_running_operation import LongRunningOperation
from .passwordless_microsoft_authenticator_authentication_method import PasswordlessMicrosoftAuthenticatorAuthenticationMethod
from .password_authentication_method import PasswordAuthenticationMethod
from .phone_authentication_method import PhoneAuthenticationMethod
from .platform_credential_authentication_method import PlatformCredentialAuthenticationMethod
from .software_oath_authentication_method import SoftwareOathAuthenticationMethod
from .temporary_access_pass_authentication_method import TemporaryAccessPassAuthenticationMethod
from .windows_hello_for_business_authentication_method import WindowsHelloForBusinessAuthenticationMethod

