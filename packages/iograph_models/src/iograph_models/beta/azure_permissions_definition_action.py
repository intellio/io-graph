from __future__ import annotations
from typing import Literal
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from pydantic import BaseModel, Field, SerializeAsAny


class AzurePermissionsDefinitionAction(BaseModel):
	odata_type: Literal["#microsoft.graph.azurePermissionsDefinitionAction"] = Field(alias="@odata.type", default="#microsoft.graph.azurePermissionsDefinitionAction")

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
			if mapping_key == "#microsoft.graph.azureActionPermissionsDefinitionAction":
				from .azure_action_permissions_definition_action import AzureActionPermissionsDefinitionAction
				return AzureActionPermissionsDefinitionAction.model_validate(data)
			if mapping_key == "#microsoft.graph.azureRolePermissionsDefinitionAction":
				from .azure_role_permissions_definition_action import AzureRolePermissionsDefinitionAction
				return AzureRolePermissionsDefinitionAction.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e


