from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from pydantic import BaseModel, Field


class AuthenticationMethodTarget(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	isRegistrationRequired: Optional[bool] = Field(default=None,alias="isRegistrationRequired",)
	targetType: Optional[AuthenticationMethodTargetType] = Field(default=None,alias="targetType",)

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
			if mapping_key == "#microsoft.graph.smsAuthenticationMethodTarget":
				from .sms_authentication_method_target import SmsAuthenticationMethodTarget
				return SmsAuthenticationMethodTarget.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .authentication_method_target_type import AuthenticationMethodTargetType

