from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any


class VerifiableCredentialRequirementStatus(BaseModel):
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
			if mapping_key == "#microsoft.graph.verifiableCredentialRequired":
				from .verifiable_credential_required import VerifiableCredentialRequired
				return VerifiableCredentialRequired.model_validate(data)
			if mapping_key == "#microsoft.graph.verifiableCredentialRetrieved":
				from .verifiable_credential_retrieved import VerifiableCredentialRetrieved
				return VerifiableCredentialRetrieved.model_validate(data)
			if mapping_key == "#microsoft.graph.verifiableCredentialVerified":
				from .verifiable_credential_verified import VerifiableCredentialVerified
				return VerifiableCredentialVerified.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

