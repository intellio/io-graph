from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any


class AuthenticationMethodConfiguration(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	excludeTargets: Optional[list[ExcludeTarget]] = Field(alias="excludeTargets", default=None,)
	state: Optional[AuthenticationMethodState | str] = Field(alias="state", default=None,)

	@model_validator(mode="wrap")
	def convert_discriminator_class(cls, data: Any, handler: ModelWrapValidatorHandler[Self]) -> Self:
		try:
			# check with parent model to catch any errors
			parent_validated_model = handler(data)
			# check if the discriminator field is present
			if "@odata.type" not in data:
				return parent_validated_model
			# get the discriminator value
			mapping_key = data["@odata.type"]
			if mapping_key == "#microsoft.graph.emailAuthenticationMethodConfiguration":
				from .email_authentication_method_configuration import EmailAuthenticationMethodConfiguration
				return EmailAuthenticationMethodConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.fido2AuthenticationMethodConfiguration":
				from .fido2_authentication_method_configuration import Fido2AuthenticationMethodConfiguration
				return Fido2AuthenticationMethodConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.microsoftAuthenticatorAuthenticationMethodConfiguration":
				from .microsoft_authenticator_authentication_method_configuration import MicrosoftAuthenticatorAuthenticationMethodConfiguration
				return MicrosoftAuthenticatorAuthenticationMethodConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.smsAuthenticationMethodConfiguration":
				from .sms_authentication_method_configuration import SmsAuthenticationMethodConfiguration
				return SmsAuthenticationMethodConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.softwareOathAuthenticationMethodConfiguration":
				from .software_oath_authentication_method_configuration import SoftwareOathAuthenticationMethodConfiguration
				return SoftwareOathAuthenticationMethodConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.temporaryAccessPassAuthenticationMethodConfiguration":
				from .temporary_access_pass_authentication_method_configuration import TemporaryAccessPassAuthenticationMethodConfiguration
				return TemporaryAccessPassAuthenticationMethodConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.voiceAuthenticationMethodConfiguration":
				from .voice_authentication_method_configuration import VoiceAuthenticationMethodConfiguration
				return VoiceAuthenticationMethodConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.x509CertificateAuthenticationMethodConfiguration":
				from .x509_certificate_authentication_method_configuration import X509CertificateAuthenticationMethodConfiguration
				return X509CertificateAuthenticationMethodConfiguration.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .exclude_target import ExcludeTarget
from .authentication_method_state import AuthenticationMethodState
