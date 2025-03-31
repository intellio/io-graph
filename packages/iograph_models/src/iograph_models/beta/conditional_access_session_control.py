from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any


class ConditionalAccessSessionControl(BaseModel):
	isEnabled: Optional[bool] = Field(alias="isEnabled", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

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
			if mapping_key == "#microsoft.graph.applicationEnforcedRestrictionsSessionControl":
				from .application_enforced_restrictions_session_control import ApplicationEnforcedRestrictionsSessionControl
				return ApplicationEnforcedRestrictionsSessionControl.model_validate(data)
			if mapping_key == "#microsoft.graph.cloudAppSecuritySessionControl":
				from .cloud_app_security_session_control import CloudAppSecuritySessionControl
				return CloudAppSecuritySessionControl.model_validate(data)
			if mapping_key == "#microsoft.graph.persistentBrowserSessionControl":
				from .persistent_browser_session_control import PersistentBrowserSessionControl
				return PersistentBrowserSessionControl.model_validate(data)
			if mapping_key == "#microsoft.graph.secureSignInSessionControl":
				from .secure_sign_in_session_control import SecureSignInSessionControl
				return SecureSignInSessionControl.model_validate(data)
			if mapping_key == "#microsoft.graph.signInFrequencySessionControl":
				from .sign_in_frequency_session_control import SignInFrequencySessionControl
				return SignInFrequencySessionControl.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

