from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class SecurityToolAwsRoleAdministratorFinding(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.securityToolAwsRoleAdministratorFinding"] = Field(alias="@odata.type", default="#microsoft.graph.securityToolAwsRoleAdministratorFinding")
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	identityDetails: Optional[IdentityDetails] = Field(alias="identityDetails", default=None,)
	permissionsCreepIndex: Optional[PermissionsCreepIndex] = Field(alias="permissionsCreepIndex", default=None,)
	securityTools: Optional[AwsSecurityToolWebServices | str] = Field(alias="securityTools", default=None,)
	identity: Optional[Union[AwsAccessKey, AwsEc2Instance, AwsGroup, AwsLambda, AwsRole, AwsUser, AzureGroup, AzureManagedIdentity, AzureServerlessFunction, AzureServicePrincipal, AzureUser, GcpCloudFunction, GcpGroup, GcpServiceAccount, GcpUser]] = Field(alias="identity", default=None,discriminator="odata_type", )

from .identity_details import IdentityDetails
from .permissions_creep_index import PermissionsCreepIndex
from .aws_security_tool_web_services import AwsSecurityToolWebServices
from .aws_access_key import AwsAccessKey
from .aws_ec2_instance import AwsEc2Instance
from .aws_group import AwsGroup
from .aws_lambda import AwsLambda
from .aws_role import AwsRole
from .aws_user import AwsUser
from .azure_group import AzureGroup
from .azure_managed_identity import AzureManagedIdentity
from .azure_serverless_function import AzureServerlessFunction
from .azure_service_principal import AzureServicePrincipal
from .azure_user import AzureUser
from .gcp_cloud_function import GcpCloudFunction
from .gcp_group import GcpGroup
from .gcp_service_account import GcpServiceAccount
from .gcp_user import GcpUser
