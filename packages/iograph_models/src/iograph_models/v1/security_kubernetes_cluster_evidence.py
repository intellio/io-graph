from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityKubernetesClusterEvidence(BaseModel):
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	detailedRoles: Optional[list[str]] = Field(alias="detailedRoles", default=None,)
	remediationStatus: Optional[SecurityEvidenceRemediationStatus | str] = Field(alias="remediationStatus", default=None,)
	remediationStatusDetails: Optional[str] = Field(alias="remediationStatusDetails", default=None,)
	roles: Optional[list[SecurityEvidenceRole | str]] = Field(alias="roles", default=None,)
	tags: Optional[list[str]] = Field(alias="tags", default=None,)
	verdict: Optional[SecurityEvidenceVerdict | str] = Field(alias="verdict", default=None,)
	odata_type: Literal["#microsoft.graph.security.kubernetesClusterEvidence"] = Field(alias="@odata.type", default="#microsoft.graph.security.kubernetesClusterEvidence")
	cloudResource: Optional[Union[SecurityAmazonResourceEvidence, SecurityAnalyzedMessageEvidence, SecurityAzureResourceEvidence, SecurityBlobContainerEvidence, SecurityBlobEvidence, SecurityCloudApplicationEvidence, SecurityCloudLogonRequestEvidence, SecurityCloudLogonSessionEvidence, SecurityContainerEvidence, SecurityContainerImageEvidence, SecurityContainerRegistryEvidence, SecurityDeviceEvidence, SecurityDnsEvidence, SecurityFileEvidence, SecurityFileHashEvidence, SecurityGitHubOrganizationEvidence, SecurityGitHubRepoEvidence, SecurityGitHubUserEvidence, SecurityGoogleCloudResourceEvidence, SecurityHostLogonSessionEvidence, SecurityIoTDeviceEvidence, SecurityIpEvidence, SecurityKubernetesClusterEvidence, SecurityKubernetesControllerEvidence, SecurityKubernetesNamespaceEvidence, SecurityKubernetesPodEvidence, SecurityKubernetesSecretEvidence, SecurityKubernetesServiceAccountEvidence, SecurityKubernetesServiceEvidence, SecurityMailboxConfigurationEvidence, SecurityMailboxEvidence, SecurityMailClusterEvidence, SecurityMalwareEvidence, SecurityNetworkConnectionEvidence, SecurityNicEvidence, SecurityOauthApplicationEvidence, SecurityProcessEvidence, SecurityRegistryKeyEvidence, SecurityRegistryValueEvidence, SecuritySasTokenEvidence, SecuritySecurityGroupEvidence, SecurityServicePrincipalEvidence, SecuritySubmissionMailEvidence, SecurityUrlEvidence, SecurityUserEvidence]] = Field(alias="cloudResource", default=None,discriminator="odata_type", )
	distribution: Optional[str] = Field(alias="distribution", default=None,)
	name: Optional[str] = Field(alias="name", default=None,)
	platform: Optional[SecurityKubernetesPlatform | str] = Field(alias="platform", default=None,)
	version: Optional[str] = Field(alias="version", default=None,)

from .security_evidence_remediation_status import SecurityEvidenceRemediationStatus
from .security_evidence_role import SecurityEvidenceRole
from .security_evidence_verdict import SecurityEvidenceVerdict
from .security_amazon_resource_evidence import SecurityAmazonResourceEvidence
from .security_analyzed_message_evidence import SecurityAnalyzedMessageEvidence
from .security_azure_resource_evidence import SecurityAzureResourceEvidence
from .security_blob_container_evidence import SecurityBlobContainerEvidence
from .security_blob_evidence import SecurityBlobEvidence
from .security_cloud_application_evidence import SecurityCloudApplicationEvidence
from .security_cloud_logon_request_evidence import SecurityCloudLogonRequestEvidence
from .security_cloud_logon_session_evidence import SecurityCloudLogonSessionEvidence
from .security_container_evidence import SecurityContainerEvidence
from .security_container_image_evidence import SecurityContainerImageEvidence
from .security_container_registry_evidence import SecurityContainerRegistryEvidence
from .security_device_evidence import SecurityDeviceEvidence
from .security_dns_evidence import SecurityDnsEvidence
from .security_file_evidence import SecurityFileEvidence
from .security_file_hash_evidence import SecurityFileHashEvidence
from .security_git_hub_organization_evidence import SecurityGitHubOrganizationEvidence
from .security_git_hub_repo_evidence import SecurityGitHubRepoEvidence
from .security_git_hub_user_evidence import SecurityGitHubUserEvidence
from .security_google_cloud_resource_evidence import SecurityGoogleCloudResourceEvidence
from .security_host_logon_session_evidence import SecurityHostLogonSessionEvidence
from .security_io_t_device_evidence import SecurityIoTDeviceEvidence
from .security_ip_evidence import SecurityIpEvidence
from .security_kubernetes_controller_evidence import SecurityKubernetesControllerEvidence
from .security_kubernetes_namespace_evidence import SecurityKubernetesNamespaceEvidence
from .security_kubernetes_pod_evidence import SecurityKubernetesPodEvidence
from .security_kubernetes_secret_evidence import SecurityKubernetesSecretEvidence
from .security_kubernetes_service_account_evidence import SecurityKubernetesServiceAccountEvidence
from .security_kubernetes_service_evidence import SecurityKubernetesServiceEvidence
from .security_mailbox_configuration_evidence import SecurityMailboxConfigurationEvidence
from .security_mailbox_evidence import SecurityMailboxEvidence
from .security_mail_cluster_evidence import SecurityMailClusterEvidence
from .security_malware_evidence import SecurityMalwareEvidence
from .security_network_connection_evidence import SecurityNetworkConnectionEvidence
from .security_nic_evidence import SecurityNicEvidence
from .security_oauth_application_evidence import SecurityOauthApplicationEvidence
from .security_process_evidence import SecurityProcessEvidence
from .security_registry_key_evidence import SecurityRegistryKeyEvidence
from .security_registry_value_evidence import SecurityRegistryValueEvidence
from .security_sas_token_evidence import SecuritySasTokenEvidence
from .security_security_group_evidence import SecuritySecurityGroupEvidence
from .security_service_principal_evidence import SecurityServicePrincipalEvidence
from .security_submission_mail_evidence import SecuritySubmissionMailEvidence
from .security_url_evidence import SecurityUrlEvidence
from .security_user_evidence import SecurityUserEvidence
from .security_kubernetes_platform import SecurityKubernetesPlatform

