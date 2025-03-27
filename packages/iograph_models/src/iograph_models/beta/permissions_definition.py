from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from pydantic import BaseModel, Field, SerializeAsAny


class PermissionsDefinition(BaseModel):
	authorizationSystemInfo: Optional[PermissionsDefinitionAuthorizationSystem] = Field(alias="authorizationSystemInfo", default=None,)
	identityInfo: Optional[PermissionsDefinitionAuthorizationSystemIdentity] = Field(alias="identityInfo", default=None,)
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
			if mapping_key == "#microsoft.graph.awsPermissionsDefinition":
				from .aws_permissions_definition import AwsPermissionsDefinition
				return AwsPermissionsDefinition.model_validate(data)
			if mapping_key == "#microsoft.graph.singleResourceAzurePermissionsDefinition":
				from .single_resource_azure_permissions_definition import SingleResourceAzurePermissionsDefinition
				return SingleResourceAzurePermissionsDefinition.model_validate(data)
			if mapping_key == "#microsoft.graph.singleResourceGcpPermissionsDefinition":
				from .single_resource_gcp_permissions_definition import SingleResourceGcpPermissionsDefinition
				return SingleResourceGcpPermissionsDefinition.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .permissions_definition_authorization_system import PermissionsDefinitionAuthorizationSystem
from .permissions_definition_authorization_system_identity import PermissionsDefinitionAuthorizationSystemIdentity

