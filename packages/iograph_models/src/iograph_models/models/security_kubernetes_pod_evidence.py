from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityKubernetesPodEvidence(BaseModel):
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	detailedRoles: Optional[list[str]] = Field(alias="detailedRoles",default=None,)
	remediationStatus: Optional[str | SecurityEvidenceRemediationStatus] = Field(alias="remediationStatus",default=None,)
	remediationStatusDetails: Optional[str] = Field(alias="remediationStatusDetails",default=None,)
	roles: Optional[list[str | SecurityEvidenceRole]] = Field(alias="roles",default=None,)
	tags: Optional[list[str]] = Field(alias="tags",default=None,)
	verdict: Optional[str | SecurityEvidenceVerdict] = Field(alias="verdict",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	containers: Optional[list[SecurityContainerEvidence]] = Field(alias="containers",default=None,)
	controller: Optional[SecurityKubernetesControllerEvidence] = Field(alias="controller",default=None,)
	ephemeralContainers: Optional[list[SecurityContainerEvidence]] = Field(alias="ephemeralContainers",default=None,)
	initContainers: Optional[list[SecurityContainerEvidence]] = Field(alias="initContainers",default=None,)
	labels: Optional[SecurityDictionary] = Field(alias="labels",default=None,)
	name: Optional[str] = Field(alias="name",default=None,)
	namespace: Optional[SecurityKubernetesNamespaceEvidence] = Field(alias="namespace",default=None,)
	podIp: Optional[SecurityIpEvidence] = Field(alias="podIp",default=None,)
	serviceAccount: Optional[SecurityKubernetesServiceAccountEvidence] = Field(alias="serviceAccount",default=None,)

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

