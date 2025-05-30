from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class SecurityNetworkConnectionEvidence(BaseModel):
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	detailedRoles: Optional[list[str]] = Field(alias="detailedRoles", default=None,)
	remediationStatus: Optional[SecurityEvidenceRemediationStatus | str] = Field(alias="remediationStatus", default=None,)
	remediationStatusDetails: Optional[str] = Field(alias="remediationStatusDetails", default=None,)
	roles: Optional[list[SecurityEvidenceRole | str]] = Field(alias="roles", default=None,)
	tags: Optional[list[str]] = Field(alias="tags", default=None,)
	verdict: Optional[SecurityEvidenceVerdict | str] = Field(alias="verdict", default=None,)
	odata_type: Literal["#microsoft.graph.security.networkConnectionEvidence"] = Field(alias="@odata.type", default="#microsoft.graph.security.networkConnectionEvidence")
	destinationAddress: Optional[SecurityIpEvidence] = Field(alias="destinationAddress", default=None,)
	destinationPort: Optional[int] = Field(alias="destinationPort", default=None,)
	protocol: Optional[SecurityProtocolType | str] = Field(alias="protocol", default=None,)
	sourceAddress: Optional[SecurityIpEvidence] = Field(alias="sourceAddress", default=None,)
	sourcePort: Optional[int] = Field(alias="sourcePort", default=None,)

from .security_evidence_remediation_status import SecurityEvidenceRemediationStatus
from .security_evidence_role import SecurityEvidenceRole
from .security_evidence_verdict import SecurityEvidenceVerdict
from .security_ip_evidence import SecurityIpEvidence
from .security_protocol_type import SecurityProtocolType
