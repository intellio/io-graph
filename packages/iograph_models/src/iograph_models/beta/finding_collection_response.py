from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field


class FindingCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[AwsExternalSystemAccessFinding, AwsExternalSystemAccessRoleFinding, AwsIdentityAccessManagementKeyAgeFinding, AwsIdentityAccessManagementKeyUsageFinding, SecretInformationAccessAwsResourceFinding, SecretInformationAccessAwsRoleFinding, SecretInformationAccessAwsServerlessFunctionFinding, SecretInformationAccessAwsUserFinding, SecurityToolAwsResourceAdministratorFinding, SecurityToolAwsRoleAdministratorFinding, SecurityToolAwsServerlessFunctionAdministratorFinding, SecurityToolAwsUserAdministratorFinding, EncryptedAwsStorageBucketFinding, EncryptedAzureStorageAccountFinding, EncryptedGcpStorageBucketFinding, ExternallyAccessibleAwsStorageBucketFinding, ExternallyAccessibleAzureBlobContainerFinding, ExternallyAccessibleGcpStorageBucketFinding, InactiveAwsResourceFinding, InactiveAwsRoleFinding, InactiveAzureServicePrincipalFinding, InactiveGcpServiceAccountFinding, InactiveServerlessFunctionFinding, InactiveUserFinding, OverprovisionedAwsResourceFinding, OverprovisionedAwsRoleFinding, OverprovisionedAzureServicePrincipalFinding, OverprovisionedGcpServiceAccountFinding, OverprovisionedServerlessFunctionFinding, OverprovisionedUserFinding, SuperAwsResourceFinding, SuperAwsRoleFinding, SuperAzureServicePrincipalFinding, SuperGcpServiceAccountFinding, SuperServerlessFunctionFinding, SuperUserFinding, UnenforcedMfaAwsUserFinding, InactiveGroupFinding, OpenAwsSecurityGroupFinding, OpenNetworkAzureSecurityGroupFinding, PrivilegeEscalationAwsResourceFinding, PrivilegeEscalationAwsRoleFinding, PrivilegeEscalationGcpServiceAccountFinding, PrivilegeEscalationUserFinding, VirtualMachineWithAwsStorageBucketAccessFinding],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .aws_external_system_access_finding import AwsExternalSystemAccessFinding
from .aws_external_system_access_role_finding import AwsExternalSystemAccessRoleFinding
from .aws_identity_access_management_key_age_finding import AwsIdentityAccessManagementKeyAgeFinding
from .aws_identity_access_management_key_usage_finding import AwsIdentityAccessManagementKeyUsageFinding
from .secret_information_access_aws_resource_finding import SecretInformationAccessAwsResourceFinding
from .secret_information_access_aws_role_finding import SecretInformationAccessAwsRoleFinding
from .secret_information_access_aws_serverless_function_finding import SecretInformationAccessAwsServerlessFunctionFinding
from .secret_information_access_aws_user_finding import SecretInformationAccessAwsUserFinding
from .security_tool_aws_resource_administrator_finding import SecurityToolAwsResourceAdministratorFinding
from .security_tool_aws_role_administrator_finding import SecurityToolAwsRoleAdministratorFinding
from .security_tool_aws_serverless_function_administrator_finding import SecurityToolAwsServerlessFunctionAdministratorFinding
from .security_tool_aws_user_administrator_finding import SecurityToolAwsUserAdministratorFinding
from .encrypted_aws_storage_bucket_finding import EncryptedAwsStorageBucketFinding
from .encrypted_azure_storage_account_finding import EncryptedAzureStorageAccountFinding
from .encrypted_gcp_storage_bucket_finding import EncryptedGcpStorageBucketFinding
from .externally_accessible_aws_storage_bucket_finding import ExternallyAccessibleAwsStorageBucketFinding
from .externally_accessible_azure_blob_container_finding import ExternallyAccessibleAzureBlobContainerFinding
from .externally_accessible_gcp_storage_bucket_finding import ExternallyAccessibleGcpStorageBucketFinding
from .inactive_aws_resource_finding import InactiveAwsResourceFinding
from .inactive_aws_role_finding import InactiveAwsRoleFinding
from .inactive_azure_service_principal_finding import InactiveAzureServicePrincipalFinding
from .inactive_gcp_service_account_finding import InactiveGcpServiceAccountFinding
from .inactive_serverless_function_finding import InactiveServerlessFunctionFinding
from .inactive_user_finding import InactiveUserFinding
from .overprovisioned_aws_resource_finding import OverprovisionedAwsResourceFinding
from .overprovisioned_aws_role_finding import OverprovisionedAwsRoleFinding
from .overprovisioned_azure_service_principal_finding import OverprovisionedAzureServicePrincipalFinding
from .overprovisioned_gcp_service_account_finding import OverprovisionedGcpServiceAccountFinding
from .overprovisioned_serverless_function_finding import OverprovisionedServerlessFunctionFinding
from .overprovisioned_user_finding import OverprovisionedUserFinding
from .super_aws_resource_finding import SuperAwsResourceFinding
from .super_aws_role_finding import SuperAwsRoleFinding
from .super_azure_service_principal_finding import SuperAzureServicePrincipalFinding
from .super_gcp_service_account_finding import SuperGcpServiceAccountFinding
from .super_serverless_function_finding import SuperServerlessFunctionFinding
from .super_user_finding import SuperUserFinding
from .unenforced_mfa_aws_user_finding import UnenforcedMfaAwsUserFinding
from .inactive_group_finding import InactiveGroupFinding
from .open_aws_security_group_finding import OpenAwsSecurityGroupFinding
from .open_network_azure_security_group_finding import OpenNetworkAzureSecurityGroupFinding
from .privilege_escalation_aws_resource_finding import PrivilegeEscalationAwsResourceFinding
from .privilege_escalation_aws_role_finding import PrivilegeEscalationAwsRoleFinding
from .privilege_escalation_gcp_service_account_finding import PrivilegeEscalationGcpServiceAccountFinding
from .privilege_escalation_user_finding import PrivilegeEscalationUserFinding
from .virtual_machine_with_aws_storage_bucket_access_finding import VirtualMachineWithAwsStorageBucketAccessFinding
