from __future__ import annotations
from typing import Optional
from typing import Union
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from pydantic import BaseModel, Field, SerializeAsAny


class AuthorizationSystemResource(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	externalId: Optional[str] = Field(alias="externalId", default=None,)
	resourceType: Optional[str] = Field(alias="resourceType", default=None,)
	authorizationSystem: Optional[Union[AwsAuthorizationSystem, AzureAuthorizationSystem, GcpAuthorizationSystem]] = Field(alias="authorizationSystem", default=None,discriminator="odata_type", )

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
			if mapping_key == "#microsoft.graph.awsAuthorizationSystemResource":
				from .aws_authorization_system_resource import AwsAuthorizationSystemResource
				return AwsAuthorizationSystemResource.model_validate(data)
			if mapping_key == "#microsoft.graph.azureAuthorizationSystemResource":
				from .azure_authorization_system_resource import AzureAuthorizationSystemResource
				return AzureAuthorizationSystemResource.model_validate(data)
			if mapping_key == "#microsoft.graph.gcpAuthorizationSystemResource":
				from .gcp_authorization_system_resource import GcpAuthorizationSystemResource
				return GcpAuthorizationSystemResource.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .aws_authorization_system import AwsAuthorizationSystem
from .azure_authorization_system import AzureAuthorizationSystem
from .gcp_authorization_system import GcpAuthorizationSystem

