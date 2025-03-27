from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityHostLogonSessionEvidence(BaseModel):
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	detailedRoles: Optional[list[str]] = Field(alias="detailedRoles", default=None,)
	remediationStatus: Optional[SecurityEvidenceRemediationStatus | str] = Field(alias="remediationStatus", default=None,)
	remediationStatusDetails: Optional[str] = Field(alias="remediationStatusDetails", default=None,)
	roles: Optional[list[SecurityEvidenceRole | str]] = Field(alias="roles", default=None,)
	tags: Optional[list[str]] = Field(alias="tags", default=None,)
	verdict: Optional[SecurityEvidenceVerdict | str] = Field(alias="verdict", default=None,)
	odata_type: Literal["#microsoft.graph.security.hostLogonSessionEvidence"] = Field(alias="@odata.type", default="#microsoft.graph.security.hostLogonSessionEvidence")
	account: Optional[SecurityUserEvidence] = Field(alias="account", default=None,)
	endUtcDateTime: Optional[datetime] = Field(alias="endUtcDateTime", default=None,)
	host: Optional[SecurityDeviceEvidence] = Field(alias="host", default=None,)
	sessionId: Optional[str] = Field(alias="sessionId", default=None,)
	startUtcDateTime: Optional[datetime] = Field(alias="startUtcDateTime", default=None,)

from .security_evidence_remediation_status import SecurityEvidenceRemediationStatus
from .security_evidence_role import SecurityEvidenceRole
from .security_evidence_verdict import SecurityEvidenceVerdict
from .security_user_evidence import SecurityUserEvidence
from .security_device_evidence import SecurityDeviceEvidence

