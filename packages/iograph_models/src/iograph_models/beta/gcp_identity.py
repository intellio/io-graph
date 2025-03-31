from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from pydantic import BaseModel, Field
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any


class GcpIdentity(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.gcpIdentity"] = Field(alias="@odata.type", default="#microsoft.graph.gcpIdentity")
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	externalId: Optional[str] = Field(alias="externalId", default=None,)
	source: Optional[Union[AadSource, AwsSource, AzureSource, GsuiteSource, UnknownSource]] = Field(alias="source", default=None,discriminator="odata_type", )
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
			if mapping_key == "#microsoft.graph.gcpCloudFunction":
				from .gcp_cloud_function import GcpCloudFunction
				return GcpCloudFunction.model_validate(data)
			if mapping_key == "#microsoft.graph.gcpGroup":
				from .gcp_group import GcpGroup
				return GcpGroup.model_validate(data)
			if mapping_key == "#microsoft.graph.gcpServiceAccount":
				from .gcp_service_account import GcpServiceAccount
				return GcpServiceAccount.model_validate(data)
			if mapping_key == "#microsoft.graph.gcpUser":
				from .gcp_user import GcpUser
				return GcpUser.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .aad_source import AadSource
from .aws_source import AwsSource
from .azure_source import AzureSource
from .gsuite_source import GsuiteSource
from .unknown_source import UnknownSource
from .aws_authorization_system import AwsAuthorizationSystem
from .azure_authorization_system import AzureAuthorizationSystem
from .gcp_authorization_system import GcpAuthorizationSystem
