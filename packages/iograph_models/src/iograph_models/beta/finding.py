from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class Finding(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)

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
			if mapping_key == "#microsoft.graph.awsExternalSystemAccessFinding":
				from .aws_external_system_access_finding import AwsExternalSystemAccessFinding
				return AwsExternalSystemAccessFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.awsExternalSystemAccessRoleFinding":
				from .aws_external_system_access_role_finding import AwsExternalSystemAccessRoleFinding
				return AwsExternalSystemAccessRoleFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.awsIdentityAccessManagementKeyAgeFinding":
				from .aws_identity_access_management_key_age_finding import AwsIdentityAccessManagementKeyAgeFinding
				return AwsIdentityAccessManagementKeyAgeFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.awsIdentityAccessManagementKeyUsageFinding":
				from .aws_identity_access_management_key_usage_finding import AwsIdentityAccessManagementKeyUsageFinding
				return AwsIdentityAccessManagementKeyUsageFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.awsSecretInformationAccessFinding":
				from .aws_secret_information_access_finding import AwsSecretInformationAccessFinding
				return AwsSecretInformationAccessFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.secretInformationAccessAwsResourceFinding":
				from .secret_information_access_aws_resource_finding import SecretInformationAccessAwsResourceFinding
				return SecretInformationAccessAwsResourceFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.secretInformationAccessAwsRoleFinding":
				from .secret_information_access_aws_role_finding import SecretInformationAccessAwsRoleFinding
				return SecretInformationAccessAwsRoleFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.secretInformationAccessAwsServerlessFunctionFinding":
				from .secret_information_access_aws_serverless_function_finding import SecretInformationAccessAwsServerlessFunctionFinding
				return SecretInformationAccessAwsServerlessFunctionFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.secretInformationAccessAwsUserFinding":
				from .secret_information_access_aws_user_finding import SecretInformationAccessAwsUserFinding
				return SecretInformationAccessAwsUserFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.awsSecurityToolAdministrationFinding":
				from .aws_security_tool_administration_finding import AwsSecurityToolAdministrationFinding
				return AwsSecurityToolAdministrationFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.securityToolAwsResourceAdministratorFinding":
				from .security_tool_aws_resource_administrator_finding import SecurityToolAwsResourceAdministratorFinding
				return SecurityToolAwsResourceAdministratorFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.securityToolAwsRoleAdministratorFinding":
				from .security_tool_aws_role_administrator_finding import SecurityToolAwsRoleAdministratorFinding
				return SecurityToolAwsRoleAdministratorFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.securityToolAwsServerlessFunctionAdministratorFinding":
				from .security_tool_aws_serverless_function_administrator_finding import SecurityToolAwsServerlessFunctionAdministratorFinding
				return SecurityToolAwsServerlessFunctionAdministratorFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.securityToolAwsUserAdministratorFinding":
				from .security_tool_aws_user_administrator_finding import SecurityToolAwsUserAdministratorFinding
				return SecurityToolAwsUserAdministratorFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.encryptedAwsStorageBucketFinding":
				from .encrypted_aws_storage_bucket_finding import EncryptedAwsStorageBucketFinding
				return EncryptedAwsStorageBucketFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.encryptedAzureStorageAccountFinding":
				from .encrypted_azure_storage_account_finding import EncryptedAzureStorageAccountFinding
				return EncryptedAzureStorageAccountFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.encryptedGcpStorageBucketFinding":
				from .encrypted_gcp_storage_bucket_finding import EncryptedGcpStorageBucketFinding
				return EncryptedGcpStorageBucketFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.externallyAccessibleAwsStorageBucketFinding":
				from .externally_accessible_aws_storage_bucket_finding import ExternallyAccessibleAwsStorageBucketFinding
				return ExternallyAccessibleAwsStorageBucketFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.externallyAccessibleAzureBlobContainerFinding":
				from .externally_accessible_azure_blob_container_finding import ExternallyAccessibleAzureBlobContainerFinding
				return ExternallyAccessibleAzureBlobContainerFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.externallyAccessibleGcpStorageBucketFinding":
				from .externally_accessible_gcp_storage_bucket_finding import ExternallyAccessibleGcpStorageBucketFinding
				return ExternallyAccessibleGcpStorageBucketFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.identityFinding":
				from .identity_finding import IdentityFinding
				return IdentityFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.inactiveAwsResourceFinding":
				from .inactive_aws_resource_finding import InactiveAwsResourceFinding
				return InactiveAwsResourceFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.inactiveAwsRoleFinding":
				from .inactive_aws_role_finding import InactiveAwsRoleFinding
				return InactiveAwsRoleFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.inactiveAzureServicePrincipalFinding":
				from .inactive_azure_service_principal_finding import InactiveAzureServicePrincipalFinding
				return InactiveAzureServicePrincipalFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.inactiveGcpServiceAccountFinding":
				from .inactive_gcp_service_account_finding import InactiveGcpServiceAccountFinding
				return InactiveGcpServiceAccountFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.inactiveServerlessFunctionFinding":
				from .inactive_serverless_function_finding import InactiveServerlessFunctionFinding
				return InactiveServerlessFunctionFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.inactiveUserFinding":
				from .inactive_user_finding import InactiveUserFinding
				return InactiveUserFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.overprovisionedAwsResourceFinding":
				from .overprovisioned_aws_resource_finding import OverprovisionedAwsResourceFinding
				return OverprovisionedAwsResourceFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.overprovisionedAwsRoleFinding":
				from .overprovisioned_aws_role_finding import OverprovisionedAwsRoleFinding
				return OverprovisionedAwsRoleFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.overprovisionedAzureServicePrincipalFinding":
				from .overprovisioned_azure_service_principal_finding import OverprovisionedAzureServicePrincipalFinding
				return OverprovisionedAzureServicePrincipalFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.overprovisionedGcpServiceAccountFinding":
				from .overprovisioned_gcp_service_account_finding import OverprovisionedGcpServiceAccountFinding
				return OverprovisionedGcpServiceAccountFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.overprovisionedServerlessFunctionFinding":
				from .overprovisioned_serverless_function_finding import OverprovisionedServerlessFunctionFinding
				return OverprovisionedServerlessFunctionFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.overprovisionedUserFinding":
				from .overprovisioned_user_finding import OverprovisionedUserFinding
				return OverprovisionedUserFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.superAwsResourceFinding":
				from .super_aws_resource_finding import SuperAwsResourceFinding
				return SuperAwsResourceFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.superAwsRoleFinding":
				from .super_aws_role_finding import SuperAwsRoleFinding
				return SuperAwsRoleFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.superAzureServicePrincipalFinding":
				from .super_azure_service_principal_finding import SuperAzureServicePrincipalFinding
				return SuperAzureServicePrincipalFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.superGcpServiceAccountFinding":
				from .super_gcp_service_account_finding import SuperGcpServiceAccountFinding
				return SuperGcpServiceAccountFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.superServerlessFunctionFinding":
				from .super_serverless_function_finding import SuperServerlessFunctionFinding
				return SuperServerlessFunctionFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.superUserFinding":
				from .super_user_finding import SuperUserFinding
				return SuperUserFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.unenforcedMfaAwsUserFinding":
				from .unenforced_mfa_aws_user_finding import UnenforcedMfaAwsUserFinding
				return UnenforcedMfaAwsUserFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.inactiveGroupFinding":
				from .inactive_group_finding import InactiveGroupFinding
				return InactiveGroupFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.openAwsSecurityGroupFinding":
				from .open_aws_security_group_finding import OpenAwsSecurityGroupFinding
				return OpenAwsSecurityGroupFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.openNetworkAzureSecurityGroupFinding":
				from .open_network_azure_security_group_finding import OpenNetworkAzureSecurityGroupFinding
				return OpenNetworkAzureSecurityGroupFinding.model_validate(data)
			if mapping_key == "#microsoft.graph.privilegeEscalationFinding":
				from .privilege_escalation_finding import PrivilegeEscalationFinding
				return PrivilegeEscalationFinding.model_validate(data)
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
			if mapping_key == "#microsoft.graph.virtualMachineWithAwsStorageBucketAccessFinding":
				from .virtual_machine_with_aws_storage_bucket_access_finding import VirtualMachineWithAwsStorageBucketAccessFinding
				return VirtualMachineWithAwsStorageBucketAccessFinding.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e


