from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from pydantic import BaseModel, Field, SerializeAsAny


class AuthorizationSystem(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	authorizationSystemId: Optional[str] = Field(alias="authorizationSystemId",default=None,)
	authorizationSystemName: Optional[str] = Field(alias="authorizationSystemName",default=None,)
	authorizationSystemType: Optional[str] = Field(alias="authorizationSystemType",default=None,)
	dataCollectionInfo: Optional[DataCollectionInfo] = Field(alias="dataCollectionInfo",default=None,)

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
			if mapping_key == "#microsoft.graph.awsAuthorizationSystem":
				from .aws_authorization_system import AwsAuthorizationSystem
				return AwsAuthorizationSystem.model_validate(data)
			if mapping_key == "#microsoft.graph.azureAuthorizationSystem":
				from .azure_authorization_system import AzureAuthorizationSystem
				return AzureAuthorizationSystem.model_validate(data)
			if mapping_key == "#microsoft.graph.gcpAuthorizationSystem":
				from .gcp_authorization_system import GcpAuthorizationSystem
				return GcpAuthorizationSystem.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .data_collection_info import DataCollectionInfo

