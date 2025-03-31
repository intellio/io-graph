from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any


class PermissionsDefinitionAction(BaseModel):
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
			if mapping_key == "#microsoft.graph.awsActionsPermissionsDefinitionAction":
				from .aws_actions_permissions_definition_action import AwsActionsPermissionsDefinitionAction
				return AwsActionsPermissionsDefinitionAction.model_validate(data)
			if mapping_key == "#microsoft.graph.awsPolicyPermissionsDefinitionAction":
				from .aws_policy_permissions_definition_action import AwsPolicyPermissionsDefinitionAction
				return AwsPolicyPermissionsDefinitionAction.model_validate(data)
			if mapping_key == "#microsoft.graph.azureActionPermissionsDefinitionAction":
				from .azure_action_permissions_definition_action import AzureActionPermissionsDefinitionAction
				return AzureActionPermissionsDefinitionAction.model_validate(data)
			if mapping_key == "#microsoft.graph.azureRolePermissionsDefinitionAction":
				from .azure_role_permissions_definition_action import AzureRolePermissionsDefinitionAction
				return AzureRolePermissionsDefinitionAction.model_validate(data)
			if mapping_key == "#microsoft.graph.gcpActionPermissionsDefinitionAction":
				from .gcp_action_permissions_definition_action import GcpActionPermissionsDefinitionAction
				return GcpActionPermissionsDefinitionAction.model_validate(data)
			if mapping_key == "#microsoft.graph.gcpRolePermissionsDefinitionAction":
				from .gcp_role_permissions_definition_action import GcpRolePermissionsDefinitionAction
				return GcpRolePermissionsDefinitionAction.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

