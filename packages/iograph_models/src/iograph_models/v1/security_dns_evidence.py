from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class SecurityDnsEvidence(BaseModel):
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	detailedRoles: Optional[list[str]] = Field(alias="detailedRoles", default=None,)
	remediationStatus: Optional[SecurityEvidenceRemediationStatus | str] = Field(alias="remediationStatus", default=None,)
	remediationStatusDetails: Optional[str] = Field(alias="remediationStatusDetails", default=None,)
	roles: Optional[list[SecurityEvidenceRole | str]] = Field(alias="roles", default=None,)
	tags: Optional[list[str]] = Field(alias="tags", default=None,)
	verdict: Optional[SecurityEvidenceVerdict | str] = Field(alias="verdict", default=None,)
	odata_type: Literal["#microsoft.graph.security.dnsEvidence"] = Field(alias="@odata.type", default="#microsoft.graph.security.dnsEvidence")
	dnsServerIp: Optional[SecurityIpEvidence] = Field(alias="dnsServerIp", default=None,)
	domainName: Optional[str] = Field(alias="domainName", default=None,)
	hostIpAddress: Optional[SecurityIpEvidence] = Field(alias="hostIpAddress", default=None,)
	ipAddresses: Optional[list[SecurityIpEvidence]] = Field(alias="ipAddresses", default=None,)

from .security_evidence_remediation_status import SecurityEvidenceRemediationStatus
from .security_evidence_role import SecurityEvidenceRole
from .security_evidence_verdict import SecurityEvidenceVerdict
from .security_ip_evidence import SecurityIpEvidence
