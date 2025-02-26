from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from pydantic import BaseModel, Field


class CustomExtensionData(BaseModel):
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

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
			if mapping_key == "#microsoft.graph.accessPackageAssignmentRequestCallbackData":
				from .access_package_assignment_request_callback_data import AccessPackageAssignmentRequestCallbackData
				return AccessPackageAssignmentRequestCallbackData.model_validate(data)
			if mapping_key == "#microsoft.graph.identityGovernance.customTaskExtensionCallbackData":
				from .identity_governance_custom_task_extension_callback_data import IdentityGovernanceCustomTaskExtensionCallbackData
				return IdentityGovernanceCustomTaskExtensionCallbackData.model_validate(data)
			if mapping_key == "#microsoft.graph.identityGovernance.customTaskExtensionCalloutData":
				from .identity_governance_custom_task_extension_callout_data import IdentityGovernanceCustomTaskExtensionCalloutData
				return IdentityGovernanceCustomTaskExtensionCalloutData.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e


