from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityAlertEvidence(BaseModel):
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	detailedRoles: Optional[list[str]] = Field(alias="detailedRoles", default=None,)
	remediationStatus: Optional[SecurityEvidenceRemediationStatus | str] = Field(alias="remediationStatus", default=None,)
	remediationStatusDetails: Optional[str] = Field(alias="remediationStatusDetails", default=None,)
	roles: Optional[list[SecurityEvidenceRole | str]] = Field(alias="roles", default=None,)
	tags: Optional[list[str]] = Field(alias="tags", default=None,)
	verdict: Optional[SecurityEvidenceVerdict | str] = Field(alias="verdict", default=None,)
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
			if mapping_key == "#microsoft.graph.security.amazonResourceEvidence":
				from .security_amazon_resource_evidence import SecurityAmazonResourceEvidence
				return SecurityAmazonResourceEvidence.model_validate(data)
			if mapping_key == "#microsoft.graph.security.analyzedMessageEvidence":
				from .security_analyzed_message_evidence import SecurityAnalyzedMessageEvidence
				return SecurityAnalyzedMessageEvidence.model_validate(data)
			if mapping_key == "#microsoft.graph.security.azureResourceEvidence":
				from .security_azure_resource_evidence import SecurityAzureResourceEvidence
				return SecurityAzureResourceEvidence.model_validate(data)
			if mapping_key == "#microsoft.graph.security.blobContainerEvidence":
				from .security_blob_container_evidence import SecurityBlobContainerEvidence
				return SecurityBlobContainerEvidence.model_validate(data)
			if mapping_key == "#microsoft.graph.security.blobEvidence":
				from .security_blob_evidence import SecurityBlobEvidence
				return SecurityBlobEvidence.model_validate(data)
			if mapping_key == "#microsoft.graph.security.cloudApplicationEvidence":
				from .security_cloud_application_evidence import SecurityCloudApplicationEvidence
				return SecurityCloudApplicationEvidence.model_validate(data)
			if mapping_key == "#microsoft.graph.security.cloudLogonRequestEvidence":
				from .security_cloud_logon_request_evidence import SecurityCloudLogonRequestEvidence
				return SecurityCloudLogonRequestEvidence.model_validate(data)
			if mapping_key == "#microsoft.graph.security.cloudLogonSessionEvidence":
				from .security_cloud_logon_session_evidence import SecurityCloudLogonSessionEvidence
				return SecurityCloudLogonSessionEvidence.model_validate(data)
			if mapping_key == "#microsoft.graph.security.containerEvidence":
				from .security_container_evidence import SecurityContainerEvidence
				return SecurityContainerEvidence.model_validate(data)
			if mapping_key == "#microsoft.graph.security.containerImageEvidence":
				from .security_container_image_evidence import SecurityContainerImageEvidence
				return SecurityContainerImageEvidence.model_validate(data)
			if mapping_key == "#microsoft.graph.security.containerRegistryEvidence":
				from .security_container_registry_evidence import SecurityContainerRegistryEvidence
				return SecurityContainerRegistryEvidence.model_validate(data)
			if mapping_key == "#microsoft.graph.security.deviceEvidence":
				from .security_device_evidence import SecurityDeviceEvidence
				return SecurityDeviceEvidence.model_validate(data)
			if mapping_key == "#microsoft.graph.security.dnsEvidence":
				from .security_dns_evidence import SecurityDnsEvidence
				return SecurityDnsEvidence.model_validate(data)
			if mapping_key == "#microsoft.graph.security.fileEvidence":
				from .security_file_evidence import SecurityFileEvidence
				return SecurityFileEvidence.model_validate(data)
			if mapping_key == "#microsoft.graph.security.fileHashEvidence":
				from .security_file_hash_evidence import SecurityFileHashEvidence
				return SecurityFileHashEvidence.model_validate(data)
			if mapping_key == "#microsoft.graph.security.gitHubOrganizationEvidence":
				from .security_git_hub_organization_evidence import SecurityGitHubOrganizationEvidence
				return SecurityGitHubOrganizationEvidence.model_validate(data)
			if mapping_key == "#microsoft.graph.security.gitHubRepoEvidence":
				from .security_git_hub_repo_evidence import SecurityGitHubRepoEvidence
				return SecurityGitHubRepoEvidence.model_validate(data)
			if mapping_key == "#microsoft.graph.security.gitHubUserEvidence":
				from .security_git_hub_user_evidence import SecurityGitHubUserEvidence
				return SecurityGitHubUserEvidence.model_validate(data)
			if mapping_key == "#microsoft.graph.security.googleCloudResourceEvidence":
				from .security_google_cloud_resource_evidence import SecurityGoogleCloudResourceEvidence
				return SecurityGoogleCloudResourceEvidence.model_validate(data)
			if mapping_key == "#microsoft.graph.security.hostLogonSessionEvidence":
				from .security_host_logon_session_evidence import SecurityHostLogonSessionEvidence
				return SecurityHostLogonSessionEvidence.model_validate(data)
			if mapping_key == "#microsoft.graph.security.ioTDeviceEvidence":
				from .security_io_t_device_evidence import SecurityIoTDeviceEvidence
				return SecurityIoTDeviceEvidence.model_validate(data)
			if mapping_key == "#microsoft.graph.security.ipEvidence":
				from .security_ip_evidence import SecurityIpEvidence
				return SecurityIpEvidence.model_validate(data)
			if mapping_key == "#microsoft.graph.security.kubernetesClusterEvidence":
				from .security_kubernetes_cluster_evidence import SecurityKubernetesClusterEvidence
				return SecurityKubernetesClusterEvidence.model_validate(data)
			if mapping_key == "#microsoft.graph.security.kubernetesControllerEvidence":
				from .security_kubernetes_controller_evidence import SecurityKubernetesControllerEvidence
				return SecurityKubernetesControllerEvidence.model_validate(data)
			if mapping_key == "#microsoft.graph.security.kubernetesNamespaceEvidence":
				from .security_kubernetes_namespace_evidence import SecurityKubernetesNamespaceEvidence
				return SecurityKubernetesNamespaceEvidence.model_validate(data)
			if mapping_key == "#microsoft.graph.security.kubernetesPodEvidence":
				from .security_kubernetes_pod_evidence import SecurityKubernetesPodEvidence
				return SecurityKubernetesPodEvidence.model_validate(data)
			if mapping_key == "#microsoft.graph.security.kubernetesSecretEvidence":
				from .security_kubernetes_secret_evidence import SecurityKubernetesSecretEvidence
				return SecurityKubernetesSecretEvidence.model_validate(data)
			if mapping_key == "#microsoft.graph.security.kubernetesServiceAccountEvidence":
				from .security_kubernetes_service_account_evidence import SecurityKubernetesServiceAccountEvidence
				return SecurityKubernetesServiceAccountEvidence.model_validate(data)
			if mapping_key == "#microsoft.graph.security.kubernetesServiceEvidence":
				from .security_kubernetes_service_evidence import SecurityKubernetesServiceEvidence
				return SecurityKubernetesServiceEvidence.model_validate(data)
			if mapping_key == "#microsoft.graph.security.mailboxConfigurationEvidence":
				from .security_mailbox_configuration_evidence import SecurityMailboxConfigurationEvidence
				return SecurityMailboxConfigurationEvidence.model_validate(data)
			if mapping_key == "#microsoft.graph.security.mailboxEvidence":
				from .security_mailbox_evidence import SecurityMailboxEvidence
				return SecurityMailboxEvidence.model_validate(data)
			if mapping_key == "#microsoft.graph.security.mailClusterEvidence":
				from .security_mail_cluster_evidence import SecurityMailClusterEvidence
				return SecurityMailClusterEvidence.model_validate(data)
			if mapping_key == "#microsoft.graph.security.malwareEvidence":
				from .security_malware_evidence import SecurityMalwareEvidence
				return SecurityMalwareEvidence.model_validate(data)
			if mapping_key == "#microsoft.graph.security.networkConnectionEvidence":
				from .security_network_connection_evidence import SecurityNetworkConnectionEvidence
				return SecurityNetworkConnectionEvidence.model_validate(data)
			if mapping_key == "#microsoft.graph.security.nicEvidence":
				from .security_nic_evidence import SecurityNicEvidence
				return SecurityNicEvidence.model_validate(data)
			if mapping_key == "#microsoft.graph.security.oauthApplicationEvidence":
				from .security_oauth_application_evidence import SecurityOauthApplicationEvidence
				return SecurityOauthApplicationEvidence.model_validate(data)
			if mapping_key == "#microsoft.graph.security.processEvidence":
				from .security_process_evidence import SecurityProcessEvidence
				return SecurityProcessEvidence.model_validate(data)
			if mapping_key == "#microsoft.graph.security.registryKeyEvidence":
				from .security_registry_key_evidence import SecurityRegistryKeyEvidence
				return SecurityRegistryKeyEvidence.model_validate(data)
			if mapping_key == "#microsoft.graph.security.registryValueEvidence":
				from .security_registry_value_evidence import SecurityRegistryValueEvidence
				return SecurityRegistryValueEvidence.model_validate(data)
			if mapping_key == "#microsoft.graph.security.sasTokenEvidence":
				from .security_sas_token_evidence import SecuritySasTokenEvidence
				return SecuritySasTokenEvidence.model_validate(data)
			if mapping_key == "#microsoft.graph.security.securityGroupEvidence":
				from .security_security_group_evidence import SecuritySecurityGroupEvidence
				return SecuritySecurityGroupEvidence.model_validate(data)
			if mapping_key == "#microsoft.graph.security.servicePrincipalEvidence":
				from .security_service_principal_evidence import SecurityServicePrincipalEvidence
				return SecurityServicePrincipalEvidence.model_validate(data)
			if mapping_key == "#microsoft.graph.security.submissionMailEvidence":
				from .security_submission_mail_evidence import SecuritySubmissionMailEvidence
				return SecuritySubmissionMailEvidence.model_validate(data)
			if mapping_key == "#microsoft.graph.security.teamsMessageEvidence":
				from .security_teams_message_evidence import SecurityTeamsMessageEvidence
				return SecurityTeamsMessageEvidence.model_validate(data)
			if mapping_key == "#microsoft.graph.security.urlEvidence":
				from .security_url_evidence import SecurityUrlEvidence
				return SecurityUrlEvidence.model_validate(data)
			if mapping_key == "#microsoft.graph.security.userEvidence":
				from .security_user_evidence import SecurityUserEvidence
				return SecurityUserEvidence.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .security_evidence_remediation_status import SecurityEvidenceRemediationStatus
from .security_evidence_role import SecurityEvidenceRole
from .security_evidence_verdict import SecurityEvidenceVerdict

