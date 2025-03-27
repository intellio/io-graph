from __future__ import annotations
from typing import Optional
from typing import Union
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from pydantic import BaseModel, Field, SerializeAsAny


class AuthorizationSystemIdentity(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
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
			if mapping_key == "#microsoft.graph.awsIdentity":
				from .aws_identity import AwsIdentity
				return AwsIdentity.model_validate(data)
			if mapping_key == "#microsoft.graph.awsAccessKey":
				from .aws_access_key import AwsAccessKey
				return AwsAccessKey.model_validate(data)
			if mapping_key == "#microsoft.graph.awsEc2Instance":
				from .aws_ec2_instance import AwsEc2Instance
				return AwsEc2Instance.model_validate(data)
			if mapping_key == "#microsoft.graph.awsGroup":
				from .aws_group import AwsGroup
				return AwsGroup.model_validate(data)
			if mapping_key == "#microsoft.graph.awsLambda":
				from .aws_lambda import AwsLambda
				return AwsLambda.model_validate(data)
			if mapping_key == "#microsoft.graph.awsRole":
				from .aws_role import AwsRole
				return AwsRole.model_validate(data)
			if mapping_key == "#microsoft.graph.awsUser":
				from .aws_user import AwsUser
				return AwsUser.model_validate(data)
			if mapping_key == "#microsoft.graph.azureIdentity":
				from .azure_identity import AzureIdentity
				return AzureIdentity.model_validate(data)
			if mapping_key == "#microsoft.graph.azureGroup":
				from .azure_group import AzureGroup
				return AzureGroup.model_validate(data)
			if mapping_key == "#microsoft.graph.azureManagedIdentity":
				from .azure_managed_identity import AzureManagedIdentity
				return AzureManagedIdentity.model_validate(data)
			if mapping_key == "#microsoft.graph.azureServerlessFunction":
				from .azure_serverless_function import AzureServerlessFunction
				return AzureServerlessFunction.model_validate(data)
			if mapping_key == "#microsoft.graph.azureServicePrincipal":
				from .azure_service_principal import AzureServicePrincipal
				return AzureServicePrincipal.model_validate(data)
			if mapping_key == "#microsoft.graph.azureUser":
				from .azure_user import AzureUser
				return AzureUser.model_validate(data)
			if mapping_key == "#microsoft.graph.gcpIdentity":
				from .gcp_identity import GcpIdentity
				return GcpIdentity.model_validate(data)
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

