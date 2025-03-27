from __future__ import annotations
from typing import Optional
from typing import Union
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class OverprovisionedAzureServicePrincipalFinding(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	actionSummary: Optional[ActionSummary] = Field(alias="actionSummary", default=None,)
	identityDetails: Optional[IdentityDetails] = Field(alias="identityDetails", default=None,)
	permissionsCreepIndex: Optional[PermissionsCreepIndex] = Field(alias="permissionsCreepIndex", default=None,)
	identity: Optional[Union[AwsIdentity, AwsAccessKey, AwsEc2Instance, AwsGroup, AwsLambda, AwsRole, AwsUser, AzureIdentity, AzureGroup, AzureManagedIdentity, AzureServerlessFunction, AzureServicePrincipal, AzureUser, GcpIdentity, GcpCloudFunction, GcpGroup, GcpServiceAccount, GcpUser]] = Field(alias="identity", default=None,discriminator="odata_type", )

from .action_summary import ActionSummary
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

