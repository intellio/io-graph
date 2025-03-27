from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class AuthenticationMethodsPolicy(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	policyMigrationState: Optional[AuthenticationMethodsPolicyMigrationState | str] = Field(alias="policyMigrationState", default=None,)
	policyVersion: Optional[str] = Field(alias="policyVersion", default=None,)
	reconfirmationInDays: Optional[int] = Field(alias="reconfirmationInDays", default=None,)
	registrationEnforcement: Optional[RegistrationEnforcement] = Field(alias="registrationEnforcement", default=None,)
	authenticationMethodConfigurations: Optional[list[Annotated[Union[EmailAuthenticationMethodConfiguration, Fido2AuthenticationMethodConfiguration, MicrosoftAuthenticatorAuthenticationMethodConfiguration, SmsAuthenticationMethodConfiguration, SoftwareOathAuthenticationMethodConfiguration, TemporaryAccessPassAuthenticationMethodConfiguration, VoiceAuthenticationMethodConfiguration, X509CertificateAuthenticationMethodConfiguration]],Field(discriminator="odata_type")]]] = Field(alias="authenticationMethodConfigurations", default=None,)

from .authentication_methods_policy_migration_state import AuthenticationMethodsPolicyMigrationState
from .registration_enforcement import RegistrationEnforcement
from .email_authentication_method_configuration import EmailAuthenticationMethodConfiguration
from .fido2_authentication_method_configuration import Fido2AuthenticationMethodConfiguration
from .microsoft_authenticator_authentication_method_configuration import MicrosoftAuthenticatorAuthenticationMethodConfiguration
from .sms_authentication_method_configuration import SmsAuthenticationMethodConfiguration
from .software_oath_authentication_method_configuration import SoftwareOathAuthenticationMethodConfiguration
from .temporary_access_pass_authentication_method_configuration import TemporaryAccessPassAuthenticationMethodConfiguration
from .voice_authentication_method_configuration import VoiceAuthenticationMethodConfiguration
from .x509_certificate_authentication_method_configuration import X509CertificateAuthenticationMethodConfiguration

