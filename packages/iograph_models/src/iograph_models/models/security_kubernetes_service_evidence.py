from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class SecurityKubernetesServiceEvidence(BaseModel):
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	detailedRoles: list[Optional[str]] = Field(alias="detailedRoles",)
	remediationStatus: Optional[SecurityEvidenceRemediationStatus] = Field(default=None,alias="remediationStatus",)
	remediationStatusDetails: Optional[str] = Field(default=None,alias="remediationStatusDetails",)
	roles: list[SecurityEvidenceRole] = Field(alias="roles",)
	tags: list[Optional[str]] = Field(alias="tags",)
	verdict: Optional[SecurityEvidenceVerdict] = Field(default=None,alias="verdict",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	clusterIP: Optional[SecurityIpEvidence] = Field(default=None,alias="clusterIP",)
	externalIPs: list[SecurityIpEvidence] = Field(alias="externalIPs",)
	labels: Optional[SecurityDictionary] = Field(default=None,alias="labels",)
	name: Optional[str] = Field(default=None,alias="name",)
	namespace: Optional[SecurityKubernetesNamespaceEvidence] = Field(default=None,alias="namespace",)
	selector: Optional[SecurityDictionary] = Field(default=None,alias="selector",)
	servicePorts: list[SecurityKubernetesServicePort] = Field(alias="servicePorts",)
	serviceType: Optional[SecurityKubernetesServiceType] = Field(default=None,alias="serviceType",)

from .security_evidence_remediation_status import SecurityEvidenceRemediationStatus
from .security_evidence_role import SecurityEvidenceRole
from .security_evidence_verdict import SecurityEvidenceVerdict
from .security_ip_evidence import SecurityIpEvidence
from .security_ip_evidence import SecurityIpEvidence
from .security_dictionary import SecurityDictionary
from .security_kubernetes_namespace_evidence import SecurityKubernetesNamespaceEvidence
from .security_dictionary import SecurityDictionary
from .security_kubernetes_service_port import SecurityKubernetesServicePort
from .security_kubernetes_service_type import SecurityKubernetesServiceType

