from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class Authentication(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	requirements: Optional[StrongAuthenticationRequirements] = Field(alias="requirements", default=None,)
	signInPreferences: Optional[SignInPreferences] = Field(alias="signInPreferences", default=None,)
	emailMethods: Optional[list[EmailAuthenticationMethod]] = Field(alias="emailMethods", default=None,)
	fido2Methods: Optional[list[Fido2AuthenticationMethod]] = Field(alias="fido2Methods", default=None,)
	hardwareOathMethods: Optional[list[HardwareOathAuthenticationMethod]] = Field(alias="hardwareOathMethods", default=None,)
	methods: Optional[list[Annotated[Union[EmailAuthenticationMethod, Fido2AuthenticationMethod, HardwareOathAuthenticationMethod, MicrosoftAuthenticatorAuthenticationMethod, PasswordAuthenticationMethod, PasswordlessMicrosoftAuthenticatorAuthenticationMethod, PhoneAuthenticationMethod, PlatformCredentialAuthenticationMethod, SoftwareOathAuthenticationMethod, TemporaryAccessPassAuthenticationMethod, WindowsHelloForBusinessAuthenticationMethod],Field(discriminator="odata_type")]]] = Field(alias="methods", default=None,)
	microsoftAuthenticatorMethods: Optional[list[MicrosoftAuthenticatorAuthenticationMethod]] = Field(alias="microsoftAuthenticatorMethods", default=None,)
	operations: Optional[list[Annotated[Union[AttackSimulationOperation, EngagementAsyncOperation, GoalsExportJob, RichLongRunningOperation, IndustryDataValidateOperation, IndustryDataFileValidateOperation],Field(discriminator="odata_type")]]] = Field(alias="operations", default=None,)
	passwordlessMicrosoftAuthenticatorMethods: Optional[list[PasswordlessMicrosoftAuthenticatorAuthenticationMethod]] = Field(alias="passwordlessMicrosoftAuthenticatorMethods", default=None,)
	passwordMethods: Optional[list[PasswordAuthenticationMethod]] = Field(alias="passwordMethods", default=None,)
	phoneMethods: Optional[list[PhoneAuthenticationMethod]] = Field(alias="phoneMethods", default=None,)
	platformCredentialMethods: Optional[list[PlatformCredentialAuthenticationMethod]] = Field(alias="platformCredentialMethods", default=None,)
	softwareOathMethods: Optional[list[SoftwareOathAuthenticationMethod]] = Field(alias="softwareOathMethods", default=None,)
	temporaryAccessPassMethods: Optional[list[TemporaryAccessPassAuthenticationMethod]] = Field(alias="temporaryAccessPassMethods", default=None,)
	windowsHelloForBusinessMethods: Optional[list[WindowsHelloForBusinessAuthenticationMethod]] = Field(alias="windowsHelloForBusinessMethods", default=None,)

from .strong_authentication_requirements import StrongAuthenticationRequirements
from .sign_in_preferences import SignInPreferences
from .email_authentication_method import EmailAuthenticationMethod
from .fido2_authentication_method import Fido2AuthenticationMethod
from .hardware_oath_authentication_method import HardwareOathAuthenticationMethod
from .email_authentication_method import EmailAuthenticationMethod
from .fido2_authentication_method import Fido2AuthenticationMethod
from .hardware_oath_authentication_method import HardwareOathAuthenticationMethod
from .microsoft_authenticator_authentication_method import MicrosoftAuthenticatorAuthenticationMethod
from .password_authentication_method import PasswordAuthenticationMethod
from .passwordless_microsoft_authenticator_authentication_method import PasswordlessMicrosoftAuthenticatorAuthenticationMethod
from .phone_authentication_method import PhoneAuthenticationMethod
from .platform_credential_authentication_method import PlatformCredentialAuthenticationMethod
from .software_oath_authentication_method import SoftwareOathAuthenticationMethod
from .temporary_access_pass_authentication_method import TemporaryAccessPassAuthenticationMethod
from .windows_hello_for_business_authentication_method import WindowsHelloForBusinessAuthenticationMethod
from .microsoft_authenticator_authentication_method import MicrosoftAuthenticatorAuthenticationMethod
from .attack_simulation_operation import AttackSimulationOperation
from .engagement_async_operation import EngagementAsyncOperation
from .goals_export_job import GoalsExportJob
from .rich_long_running_operation import RichLongRunningOperation
from .industry_data_validate_operation import IndustryDataValidateOperation
from .industry_data_file_validate_operation import IndustryDataFileValidateOperation
from .passwordless_microsoft_authenticator_authentication_method import PasswordlessMicrosoftAuthenticatorAuthenticationMethod
from .password_authentication_method import PasswordAuthenticationMethod
from .phone_authentication_method import PhoneAuthenticationMethod
from .platform_credential_authentication_method import PlatformCredentialAuthenticationMethod
from .software_oath_authentication_method import SoftwareOathAuthenticationMethod
from .temporary_access_pass_authentication_method import TemporaryAccessPassAuthenticationMethod
from .windows_hello_for_business_authentication_method import WindowsHelloForBusinessAuthenticationMethod

