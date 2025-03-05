from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityKubernetesClusterEvidence(BaseModel):
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	detailedRoles: Optional[list[str]] = Field(alias="detailedRoles",default=None,)
	remediationStatus: Optional[str | SecurityEvidenceRemediationStatus] = Field(alias="remediationStatus",default=None,)
	remediationStatusDetails: Optional[str] = Field(alias="remediationStatusDetails",default=None,)
	roles: Optional[list[str | SecurityEvidenceRole]] = Field(alias="roles",default=None,)
	tags: Optional[list[str]] = Field(alias="tags",default=None,)
	verdict: Optional[str | SecurityEvidenceVerdict] = Field(alias="verdict",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	cloudResource: SerializeAsAny[Optional[SecurityAlertEvidence]] = Field(alias="cloudResource",default=None,)
	distribution: Optional[str] = Field(alias="distribution",default=None,)
	name: Optional[str] = Field(alias="name",default=None,)
	platform: Optional[str | SecurityKubernetesPlatform] = Field(alias="platform",default=None,)
	version: Optional[str] = Field(alias="version",default=None,)

from .security_evidence_remediation_status import SecurityEvidenceRemediationStatus
from .security_evidence_role import SecurityEvidenceRole
from .security_evidence_verdict import SecurityEvidenceVerdict
from .security_alert_evidence import SecurityAlertEvidence
from .security_kubernetes_platform import SecurityKubernetesPlatform

