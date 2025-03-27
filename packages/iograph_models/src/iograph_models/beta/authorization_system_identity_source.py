from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from pydantic import BaseModel, Field, SerializeAsAny


class AuthorizationSystemIdentitySource(BaseModel):
	identityProviderType: Optional[str] = Field(alias="identityProviderType", default=None,)
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
			if mapping_key == "#microsoft.graph.aadSource":
				from .aad_source import AadSource
				return AadSource.model_validate(data)
			if mapping_key == "#microsoft.graph.awsSource":
				from .aws_source import AwsSource
				return AwsSource.model_validate(data)
			if mapping_key == "#microsoft.graph.azureSource":
				from .azure_source import AzureSource
				return AzureSource.model_validate(data)
			if mapping_key == "#microsoft.graph.gsuiteSource":
				from .gsuite_source import GsuiteSource
				return GsuiteSource.model_validate(data)
			if mapping_key == "#microsoft.graph.unknownSource":
				from .unknown_source import UnknownSource
				return UnknownSource.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e


