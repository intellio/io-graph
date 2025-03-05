from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from pydantic import BaseModel, Field, SerializeAsAny


class AuthenticationCombinationConfiguration(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	appliesToCombinations: Optional[list[AuthenticationMethodModes]] = Field(default=None,alias="appliesToCombinations",)

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
			if mapping_key == "#microsoft.graph.fido2CombinationConfiguration":
				from .fido2_combination_configuration import Fido2CombinationConfiguration
				return Fido2CombinationConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.x509CertificateCombinationConfiguration":
				from .x509_certificate_combination_configuration import X509CertificateCombinationConfiguration
				return X509CertificateCombinationConfiguration.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .authentication_method_modes import AuthenticationMethodModes

