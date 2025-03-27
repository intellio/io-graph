from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityAlert(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	actorDisplayName: Optional[str] = Field(alias="actorDisplayName", default=None,)
	additionalData: Optional[SecurityDictionary] = Field(alias="additionalData", default=None,)
	alertPolicyId: Optional[str] = Field(alias="alertPolicyId", default=None,)
	alertWebUrl: Optional[str] = Field(alias="alertWebUrl", default=None,)
	assignedTo: Optional[str] = Field(alias="assignedTo", default=None,)
	category: Optional[str] = Field(alias="category", default=None,)
	classification: Optional[SecurityAlertClassification | str] = Field(alias="classification", default=None,)
	comments: Optional[list[SecurityAlertComment]] = Field(alias="comments", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	detectionSource: Optional[SecurityDetectionSource | str] = Field(alias="detectionSource", default=None,)
	detectorId: Optional[str] = Field(alias="detectorId", default=None,)
	determination: Optional[SecurityAlertDetermination | str] = Field(alias="determination", default=None,)
	evidence: Optional[list[Annotated[Union[SecurityAmazonResourceEvidence, SecurityAnalyzedMessageEvidence, SecurityAzureResourceEvidence, SecurityBlobContainerEvidence, SecurityBlobEvidence, SecurityCloudApplicationEvidence, SecurityCloudLogonRequestEvidence, SecurityCloudLogonSessionEvidence, SecurityContainerEvidence, SecurityContainerImageEvidence, SecurityContainerRegistryEvidence, SecurityDeviceEvidence, SecurityDnsEvidence, SecurityFileEvidence, SecurityFileHashEvidence, SecurityGitHubOrganizationEvidence, SecurityGitHubRepoEvidence, SecurityGitHubUserEvidence, SecurityGoogleCloudResourceEvidence, SecurityHostLogonSessionEvidence, SecurityIoTDeviceEvidence, SecurityIpEvidence, SecurityKubernetesClusterEvidence, SecurityKubernetesControllerEvidence, SecurityKubernetesNamespaceEvidence, SecurityKubernetesPodEvidence, SecurityKubernetesSecretEvidence, SecurityKubernetesServiceAccountEvidence, SecurityKubernetesServiceEvidence, SecurityMailboxConfigurationEvidence, SecurityMailboxEvidence, SecurityMailClusterEvidence, SecurityMalwareEvidence, SecurityNetworkConnectionEvidence, SecurityNicEvidence, SecurityOauthApplicationEvidence, SecurityProcessEvidence, SecurityRegistryKeyEvidence, SecurityRegistryValueEvidence, SecuritySasTokenEvidence, SecuritySecurityGroupEvidence, SecurityServicePrincipalEvidence, SecuritySubmissionMailEvidence, SecurityTeamsMessageEvidence, SecurityUrlEvidence, SecurityUserEvidence]],Field(discriminator="odata_type")]]] = Field(alias="evidence", default=None,)
	firstActivityDateTime: Optional[datetime] = Field(alias="firstActivityDateTime", default=None,)
	incidentId: Optional[str] = Field(alias="incidentId", default=None,)
	incidentWebUrl: Optional[str] = Field(alias="incidentWebUrl", default=None,)
	lastActivityDateTime: Optional[datetime] = Field(alias="lastActivityDateTime", default=None,)
	lastUpdateDateTime: Optional[datetime] = Field(alias="lastUpdateDateTime", default=None,)
	mitreTechniques: Optional[list[str]] = Field(alias="mitreTechniques", default=None,)
	productName: Optional[str] = Field(alias="productName", default=None,)
	providerAlertId: Optional[str] = Field(alias="providerAlertId", default=None,)
	recommendedActions: Optional[str] = Field(alias="recommendedActions", default=None,)
	resolvedDateTime: Optional[datetime] = Field(alias="resolvedDateTime", default=None,)
	serviceSource: Optional[SecurityServiceSource | str] = Field(alias="serviceSource", default=None,)
	severity: Optional[SecurityAlertSeverity | str] = Field(alias="severity", default=None,)
	status: Optional[SecurityAlertStatus | str] = Field(alias="status", default=None,)
	systemTags: Optional[list[str]] = Field(alias="systemTags", default=None,)
	tenantId: Optional[str] = Field(alias="tenantId", default=None,)
	threatDisplayName: Optional[str] = Field(alias="threatDisplayName", default=None,)
	threatFamilyName: Optional[str] = Field(alias="threatFamilyName", default=None,)
	title: Optional[str] = Field(alias="title", default=None,)

from .security_dictionary import SecurityDictionary
from .security_alert_classification import SecurityAlertClassification
from .security_alert_comment import SecurityAlertComment
from .security_detection_source import SecurityDetectionSource
from .security_alert_determination import SecurityAlertDetermination
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
from .security_kubernetes_cluster_evidence import SecurityKubernetesClusterEvidence
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
from .security_teams_message_evidence import SecurityTeamsMessageEvidence
from .security_url_evidence import SecurityUrlEvidence
from .security_user_evidence import SecurityUserEvidence
from .security_service_source import SecurityServiceSource
from .security_alert_severity import SecurityAlertSeverity
from .security_alert_status import SecurityAlertStatus

