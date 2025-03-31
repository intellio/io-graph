from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any


class AuthorizationSystemTypeAction(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	actionType: Optional[AuthorizationSystemActionType | str] = Field(alias="actionType", default=None,)
	externalId: Optional[str] = Field(alias="externalId", default=None,)
	resourceTypes: Optional[list[str]] = Field(alias="resourceTypes", default=None,)
	severity: Optional[AuthorizationSystemActionSeverity | str] = Field(alias="severity", default=None,)

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
			if mapping_key == "#microsoft.graph.awsAuthorizationSystemTypeAction":
				from .aws_authorization_system_type_action import AwsAuthorizationSystemTypeAction
				return AwsAuthorizationSystemTypeAction.model_validate(data)
			if mapping_key == "#microsoft.graph.azureAuthorizationSystemTypeAction":
				from .azure_authorization_system_type_action import AzureAuthorizationSystemTypeAction
				return AzureAuthorizationSystemTypeAction.model_validate(data)
			if mapping_key == "#microsoft.graph.gcpAuthorizationSystemTypeAction":
				from .gcp_authorization_system_type_action import GcpAuthorizationSystemTypeAction
				return GcpAuthorizationSystemTypeAction.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .authorization_system_action_type import AuthorizationSystemActionType
from .authorization_system_action_severity import AuthorizationSystemActionSeverity
