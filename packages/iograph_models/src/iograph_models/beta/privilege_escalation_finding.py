from __future__ import annotations
from typing import Optional
from typing import Union
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class PrivilegeEscalationFinding(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	identityDetails: Optional[IdentityDetails] = Field(alias="identityDetails", default=None,)
	permissionsCreepIndex: Optional[PermissionsCreepIndex] = Field(alias="permissionsCreepIndex", default=None,)
	identity: Optional[Union[AwsIdentity, AwsAccessKey, AwsEc2Instance, AwsGroup, AwsLambda, AwsRole, AwsUser, AzureIdentity, AzureGroup, AzureManagedIdentity, AzureServerlessFunction, AzureServicePrincipal, AzureUser, GcpIdentity, GcpCloudFunction, GcpGroup, GcpServiceAccount, GcpUser]] = Field(alias="identity", default=None,discriminator="odata_type", )
	privilegeEscalationDetails: Optional[list[PrivilegeEscalation]] = Field(alias="privilegeEscalationDetails", default=None,)

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
			if mapping_key == "#microsoft.graph.privilegeEscalationAwsResourceFinding":
				from .privilege_escalation_aws_resource_finding import PrivilegeEscalationAwsResourceFinding
				return PrivilegeEscalationAwsResourceFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.privilegeEscalationAwsRoleFinding":
				from .privilege_escalation_aws_role_finding import PrivilegeEscalationAwsRoleFinding
				return PrivilegeEscalationAwsRoleFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.privilegeEscalationGcpServiceAccountFinding":
				from .privilege_escalation_gcp_service_account_finding import PrivilegeEscalationGcpServiceAccountFinding
				return PrivilegeEscalationGcpServiceAccountFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.privilegeEscalationUserFinding":
				from .privilege_escalation_user_finding import PrivilegeEscalationUserFinding
				return PrivilegeEscalationUserFinding.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .identity_details import IdentityDetails
from .permissions_creep_index import PermissionsCreepIndex
from .aws_identity import AwsIdentity
from .aws_access_key import AwsAccessKey
from .aws_ec2_instance import AwsEc2Instance
from .aws_group import AwsGroup
from .aws_lambda import AwsLambda
from .aws_role import AwsRole
from .aws_user import AwsUser
from .azure_identity import AzureIdentity
from .azure_group import AzureGroup
from .azure_managed_identity import AzureManagedIdentity
from .azure_serverless_function import AzureServerlessFunction
from .azure_service_principal import AzureServicePrincipal
from .azure_user import AzureUser
from .gcp_identity import GcpIdentity
from .gcp_cloud_function import GcpCloudFunction
from .gcp_group import GcpGroup
from .gcp_service_account import GcpServiceAccount
from .gcp_user import GcpUser
from .privilege_escalation import PrivilegeEscalation

