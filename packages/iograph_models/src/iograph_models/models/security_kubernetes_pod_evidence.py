from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityKubernetesPodEvidence(BaseModel):
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	detailedRoles: Optional[list[str]] = Field(default=None,alias="detailedRoles",)
	remediationStatus: Optional[SecurityEvidenceRemediationStatus] = Field(default=None,alias="remediationStatus",)
	remediationStatusDetails: Optional[str] = Field(default=None,alias="remediationStatusDetails",)
	roles: Optional[list[SecurityEvidenceRole]] = Field(default=None,alias="roles",)
	tags: Optional[list[str]] = Field(default=None,alias="tags",)
	verdict: Optional[SecurityEvidenceVerdict] = Field(default=None,alias="verdict",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	containers: Optional[list[SecurityContainerEvidence]] = Field(default=None,alias="containers",)
	controller: Optional[SecurityKubernetesControllerEvidence] = Field(default=None,alias="controller",)
	ephemeralContainers: Optional[list[SecurityContainerEvidence]] = Field(default=None,alias="ephemeralContainers",)
	initContainers: Optional[list[SecurityContainerEvidence]] = Field(default=None,alias="initContainers",)
	labels: Optional[SecurityDictionary] = Field(default=None,alias="labels",)
	name: Optional[str] = Field(default=None,alias="name",)
	namespace: Optional[SecurityKubernetesNamespaceEvidence] = Field(default=None,alias="namespace",)
	podIp: Optional[SecurityIpEvidence] = Field(default=None,alias="podIp",)
	serviceAccount: Optional[SecurityKubernetesServiceAccountEvidence] = Field(default=None,alias="serviceAccount",)

from .security_evidence_remediation_status import SecurityEvidenceRemediationStatus
from .security_evidence_role import SecurityEvidenceRole
from .security_evidence_verdict import SecurityEvidenceVerdict
from .security_container_evidence import SecurityContainerEvidence
from .security_kubernetes_controller_evidence import SecurityKubernetesControllerEvidence
from .security_container_evidence import SecurityContainerEvidence
from .security_container_evidence import SecurityContainerEvidence
from .security_dictionary import SecurityDictionary
from .security_kubernetes_namespace_evidence import SecurityKubernetesNamespaceEvidence
from .security_ip_evidence import SecurityIpEvidence
from .security_kubernetes_service_account_evidence import SecurityKubernetesServiceAccountEvidence

