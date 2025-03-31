from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class SecurityKubernetesServiceEvidence(BaseModel):
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	detailedRoles: Optional[list[str]] = Field(alias="detailedRoles", default=None,)
	remediationStatus: Optional[SecurityEvidenceRemediationStatus | str] = Field(alias="remediationStatus", default=None,)
	remediationStatusDetails: Optional[str] = Field(alias="remediationStatusDetails", default=None,)
	roles: Optional[list[SecurityEvidenceRole | str]] = Field(alias="roles", default=None,)
	tags: Optional[list[str]] = Field(alias="tags", default=None,)
	verdict: Optional[SecurityEvidenceVerdict | str] = Field(alias="verdict", default=None,)
	odata_type: Literal["#microsoft.graph.security.kubernetesServiceEvidence"] = Field(alias="@odata.type", default="#microsoft.graph.security.kubernetesServiceEvidence")
	clusterIP: Optional[SecurityIpEvidence] = Field(alias="clusterIP", default=None,)
	externalIPs: Optional[list[SecurityIpEvidence]] = Field(alias="externalIPs", default=None,)
	labels: Optional[SecurityDictionary] = Field(alias="labels", default=None,)
	name: Optional[str] = Field(alias="name", default=None,)
	namespace: Optional[SecurityKubernetesNamespaceEvidence] = Field(alias="namespace", default=None,)
	selector: Optional[SecurityDictionary] = Field(alias="selector", default=None,)
	servicePorts: Optional[list[SecurityKubernetesServicePort]] = Field(alias="servicePorts", default=None,)
	serviceType: Optional[SecurityKubernetesServiceType | str] = Field(alias="serviceType", default=None,)

from .security_evidence_remediation_status import SecurityEvidenceRemediationStatus
from .security_evidence_role import SecurityEvidenceRole
from .security_evidence_verdict import SecurityEvidenceVerdict
from .security_ip_evidence import SecurityIpEvidence
from .security_dictionary import SecurityDictionary
from .security_kubernetes_namespace_evidence import SecurityKubernetesNamespaceEvidence
from .security_kubernetes_service_port import SecurityKubernetesServicePort
from .security_kubernetes_service_type import SecurityKubernetesServiceType
