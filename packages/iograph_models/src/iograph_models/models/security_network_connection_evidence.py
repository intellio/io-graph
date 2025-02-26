from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class SecurityNetworkConnectionEvidence(BaseModel):
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	detailedRoles: list[Optional[str]] = Field(alias="detailedRoles",)
	remediationStatus: Optional[SecurityEvidenceRemediationStatus] = Field(default=None,alias="remediationStatus",)
	remediationStatusDetails: Optional[str] = Field(default=None,alias="remediationStatusDetails",)
	roles: list[SecurityEvidenceRole] = Field(alias="roles",)
	tags: list[Optional[str]] = Field(alias="tags",)
	verdict: Optional[SecurityEvidenceVerdict] = Field(default=None,alias="verdict",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	destinationAddress: Optional[SecurityIpEvidence] = Field(default=None,alias="destinationAddress",)
	destinationPort: Optional[int] = Field(default=None,alias="destinationPort",)
	protocol: Optional[SecurityProtocolType] = Field(default=None,alias="protocol",)
	sourceAddress: Optional[SecurityIpEvidence] = Field(default=None,alias="sourceAddress",)
	sourcePort: Optional[int] = Field(default=None,alias="sourcePort",)

from .security_evidence_remediation_status import SecurityEvidenceRemediationStatus
from .security_evidence_role import SecurityEvidenceRole
from .security_evidence_verdict import SecurityEvidenceVerdict
from .security_ip_evidence import SecurityIpEvidence
from .security_protocol_type import SecurityProtocolType
from .security_ip_evidence import SecurityIpEvidence

