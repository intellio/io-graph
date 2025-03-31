from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any


class AwsPermissionsDefinitionAction(BaseModel):
	odata_type: Literal["#microsoft.graph.awsPermissionsDefinitionAction"] = Field(alias="@odata.type", default="#microsoft.graph.awsPermissionsDefinitionAction")

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
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

