from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityMailClusterEvidence(BaseModel):
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	detailedRoles: Optional[list[str]] = Field(alias="detailedRoles", default=None,)
	remediationStatus: Optional[SecurityEvidenceRemediationStatus | str] = Field(alias="remediationStatus", default=None,)
	remediationStatusDetails: Optional[str] = Field(alias="remediationStatusDetails", default=None,)
	roles: Optional[list[SecurityEvidenceRole | str]] = Field(alias="roles", default=None,)
	tags: Optional[list[str]] = Field(alias="tags", default=None,)
	verdict: Optional[SecurityEvidenceVerdict | str] = Field(alias="verdict", default=None,)
	odata_type: Literal["#microsoft.graph.security.mailClusterEvidence"] = Field(alias="@odata.type", default="#microsoft.graph.security.mailClusterEvidence")
	clusterBy: Optional[str] = Field(alias="clusterBy", default=None,)
	clusterByValue: Optional[str] = Field(alias="clusterByValue", default=None,)
	emailCount: Optional[int] = Field(alias="emailCount", default=None,)
	networkMessageIds: Optional[list[str]] = Field(alias="networkMessageIds", default=None,)
	query: Optional[str] = Field(alias="query", default=None,)
	urn: Optional[str] = Field(alias="urn", default=None,)

from .security_evidence_remediation_status import SecurityEvidenceRemediationStatus
from .security_evidence_role import SecurityEvidenceRole
from .security_evidence_verdict import SecurityEvidenceVerdict

