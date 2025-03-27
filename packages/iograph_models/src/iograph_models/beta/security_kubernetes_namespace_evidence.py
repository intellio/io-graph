from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityKubernetesNamespaceEvidence(BaseModel):
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	detailedRoles: Optional[list[str]] = Field(alias="detailedRoles", default=None,)
	remediationStatus: Optional[SecurityEvidenceRemediationStatus | str] = Field(alias="remediationStatus", default=None,)
	remediationStatusDetails: Optional[str] = Field(alias="remediationStatusDetails", default=None,)
	roles: Optional[list[SecurityEvidenceRole | str]] = Field(alias="roles", default=None,)
	tags: Optional[list[str]] = Field(alias="tags", default=None,)
	verdict: Optional[SecurityEvidenceVerdict | str] = Field(alias="verdict", default=None,)
	odata_type: Literal["#microsoft.graph.security.kubernetesNamespaceEvidence"] = Field(alias="@odata.type", default="#microsoft.graph.security.kubernetesNamespaceEvidence")
	cluster: Optional[SecurityKubernetesClusterEvidence] = Field(alias="cluster", default=None,)
	labels: Optional[SecurityDictionary] = Field(alias="labels", default=None,)
	name: Optional[str] = Field(alias="name", default=None,)

from .security_evidence_remediation_status import SecurityEvidenceRemediationStatus
from .security_evidence_role import SecurityEvidenceRole
from .security_evidence_verdict import SecurityEvidenceVerdict
from .security_kubernetes_cluster_evidence import SecurityKubernetesClusterEvidence
from .security_dictionary import SecurityDictionary

