from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from pydantic import BaseModel, Field, SerializeAsAny


class CustomExtensionCallbackConfiguration(BaseModel):
	timeoutDuration: Optional[str] = Field(alias="timeoutDuration",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

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
			if mapping_key == "#microsoft.graph.identityGovernance.customTaskExtensionCallbackConfiguration":
				from .identity_governance_custom_task_extension_callback_configuration import IdentityGovernanceCustomTaskExtensionCallbackConfiguration
				return IdentityGovernanceCustomTaskExtensionCallbackConfiguration.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e


