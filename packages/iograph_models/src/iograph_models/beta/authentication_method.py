from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class AuthenticationMethod(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)

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
			if mapping_key == "#microsoft.graph.emailAuthenticationMethod":
				from .email_authentication_method import EmailAuthenticationMethod
				return EmailAuthenticationMethod.model_validate(data)
			if mapping_key == "#microsoft.graph.fido2AuthenticationMethod":
				from .fido2_authentication_method import Fido2AuthenticationMethod
				return Fido2AuthenticationMethod.model_validate(data)
			if mapping_key == "#microsoft.graph.hardwareOathAuthenticationMethod":
				from .hardware_oath_authentication_method import HardwareOathAuthenticationMethod
				return HardwareOathAuthenticationMethod.model_validate(data)
			if mapping_key == "#microsoft.graph.microsoftAuthenticatorAuthenticationMethod":
				from .microsoft_authenticator_authentication_method import MicrosoftAuthenticatorAuthenticationMethod
				return MicrosoftAuthenticatorAuthenticationMethod.model_validate(data)
			if mapping_key == "#microsoft.graph.passwordAuthenticationMethod":
				from .password_authentication_method import PasswordAuthenticationMethod
				return PasswordAuthenticationMethod.model_validate(data)
			if mapping_key == "#microsoft.graph.passwordlessMicrosoftAuthenticatorAuthenticationMethod":
				from .passwordless_microsoft_authenticator_authentication_method import PasswordlessMicrosoftAuthenticatorAuthenticationMethod
				return PasswordlessMicrosoftAuthenticatorAuthenticationMethod.model_validate(data)
			if mapping_key == "#microsoft.graph.phoneAuthenticationMethod":
				from .phone_authentication_method import PhoneAuthenticationMethod
				return PhoneAuthenticationMethod.model_validate(data)
			if mapping_key == "#microsoft.graph.platformCredentialAuthenticationMethod":
				from .platform_credential_authentication_method import PlatformCredentialAuthenticationMethod
				return PlatformCredentialAuthenticationMethod.model_validate(data)
			if mapping_key == "#microsoft.graph.softwareOathAuthenticationMethod":
				from .software_oath_authentication_method import SoftwareOathAuthenticationMethod
				return SoftwareOathAuthenticationMethod.model_validate(data)
			if mapping_key == "#microsoft.graph.temporaryAccessPassAuthenticationMethod":
				from .temporary_access_pass_authentication_method import TemporaryAccessPassAuthenticationMethod
				return TemporaryAccessPassAuthenticationMethod.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsHelloForBusinessAuthenticationMethod":
				from .windows_hello_for_business_authentication_method import WindowsHelloForBusinessAuthenticationMethod
				return WindowsHelloForBusinessAuthenticationMethod.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e


