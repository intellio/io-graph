from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any


class AuthenticationMethodTarget(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	isRegistrationRequired: Optional[bool] = Field(alias="isRegistrationRequired", default=None,)
	targetType: Optional[AuthenticationMethodTargetType | str] = Field(alias="targetType", default=None,)

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
			if mapping_key == "#microsoft.graph.microsoftAuthenticatorAuthenticationMethodTarget":
				from .microsoft_authenticator_authentication_method_target import MicrosoftAuthenticatorAuthenticationMethodTarget
				return MicrosoftAuthenticatorAuthenticationMethodTarget.model_validate(data)
			if mapping_key == "#microsoft.graph.passkeyAuthenticationMethodTarget":
				from .passkey_authentication_method_target import PasskeyAuthenticationMethodTarget
				return PasskeyAuthenticationMethodTarget.model_validate(data)
			if mapping_key == "#microsoft.graph.smsAuthenticationMethodTarget":
				from .sms_authentication_method_target import SmsAuthenticationMethodTarget
				return SmsAuthenticationMethodTarget.model_validate(data)
			if mapping_key == "#microsoft.graph.voiceAuthenticationMethodTarget":
				from .voice_authentication_method_target import VoiceAuthenticationMethodTarget
				return VoiceAuthenticationMethodTarget.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .authentication_method_target_type import AuthenticationMethodTargetType
