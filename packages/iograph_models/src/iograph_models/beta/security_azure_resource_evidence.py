from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class SecurityAzureResourceEvidence(BaseModel):
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	detailedRoles: Optional[list[str]] = Field(alias="detailedRoles", default=None,)
	remediationStatus: Optional[SecurityEvidenceRemediationStatus | str] = Field(alias="remediationStatus", default=None,)
	remediationStatusDetails: Optional[str] = Field(alias="remediationStatusDetails", default=None,)
	roles: Optional[list[SecurityEvidenceRole | str]] = Field(alias="roles", default=None,)
	tags: Optional[list[str]] = Field(alias="tags", default=None,)
	verdict: Optional[SecurityEvidenceVerdict | str] = Field(alias="verdict", default=None,)
	odata_type: Literal["#microsoft.graph.security.azureResourceEvidence"] = Field(alias="@odata.type", default="#microsoft.graph.security.azureResourceEvidence")
	resourceId: Optional[str] = Field(alias="resourceId", default=None,)
	resourceName: Optional[str] = Field(alias="resourceName", default=None,)
	resourceType: Optional[str] = Field(alias="resourceType", default=None,)

from .security_evidence_remediation_status import SecurityEvidenceRemediationStatus
from .security_evidence_role import SecurityEvidenceRole
from .security_evidence_verdict import SecurityEvidenceVerdict
