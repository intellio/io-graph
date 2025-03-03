from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class SecurityDnsEvidence(BaseModel):
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	detailedRoles: Optional[list[str]] = Field(default=None,alias="detailedRoles",)
	remediationStatus: Optional[SecurityEvidenceRemediationStatus] = Field(default=None,alias="remediationStatus",)
	remediationStatusDetails: Optional[str] = Field(default=None,alias="remediationStatusDetails",)
	roles: Optional[list[SecurityEvidenceRole]] = Field(default=None,alias="roles",)
	tags: Optional[list[str]] = Field(default=None,alias="tags",)
	verdict: Optional[SecurityEvidenceVerdict] = Field(default=None,alias="verdict",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	dnsServerIp: Optional[SecurityIpEvidence] = Field(default=None,alias="dnsServerIp",)
	domainName: Optional[str] = Field(default=None,alias="domainName",)
	hostIpAddress: Optional[SecurityIpEvidence] = Field(default=None,alias="hostIpAddress",)
	ipAddresses: Optional[list[SecurityIpEvidence]] = Field(default=None,alias="ipAddresses",)

from .security_evidence_remediation_status import SecurityEvidenceRemediationStatus
from .security_evidence_role import SecurityEvidenceRole
from .security_evidence_verdict import SecurityEvidenceVerdict
from .security_ip_evidence import SecurityIpEvidence
from .security_ip_evidence import SecurityIpEvidence
from .security_ip_evidence import SecurityIpEvidence

