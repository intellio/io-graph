from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityCloudApplicationEvidence(BaseModel):
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	detailedRoles: Optional[list[str]] = Field(alias="detailedRoles", default=None,)
	remediationStatus: Optional[SecurityEvidenceRemediationStatus | str] = Field(alias="remediationStatus", default=None,)
	remediationStatusDetails: Optional[str] = Field(alias="remediationStatusDetails", default=None,)
	roles: Optional[list[SecurityEvidenceRole | str]] = Field(alias="roles", default=None,)
	tags: Optional[list[str]] = Field(alias="tags", default=None,)
	verdict: Optional[SecurityEvidenceVerdict | str] = Field(alias="verdict", default=None,)
	odata_type: Literal["#microsoft.graph.security.cloudApplicationEvidence"] = Field(alias="@odata.type", default="#microsoft.graph.security.cloudApplicationEvidence")
	appId: Optional[int] = Field(alias="appId", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	instanceId: Optional[int] = Field(alias="instanceId", default=None,)
	instanceName: Optional[str] = Field(alias="instanceName", default=None,)
	saasAppId: Optional[int] = Field(alias="saasAppId", default=None,)
	stream: Optional[SecurityStream] = Field(alias="stream", default=None,)

from .security_evidence_remediation_status import SecurityEvidenceRemediationStatus
from .security_evidence_role import SecurityEvidenceRole
from .security_evidence_verdict import SecurityEvidenceVerdict
from .security_stream import SecurityStream

