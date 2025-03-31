from __future__ import annotations
from uuid import UUID
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class SecurityMailboxConfigurationEvidence(BaseModel):
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	detailedRoles: Optional[list[str]] = Field(alias="detailedRoles", default=None,)
	remediationStatus: Optional[SecurityEvidenceRemediationStatus | str] = Field(alias="remediationStatus", default=None,)
	remediationStatusDetails: Optional[str] = Field(alias="remediationStatusDetails", default=None,)
	roles: Optional[list[SecurityEvidenceRole | str]] = Field(alias="roles", default=None,)
	tags: Optional[list[str]] = Field(alias="tags", default=None,)
	verdict: Optional[SecurityEvidenceVerdict | str] = Field(alias="verdict", default=None,)
	odata_type: Literal["#microsoft.graph.security.mailboxConfigurationEvidence"] = Field(alias="@odata.type", default="#microsoft.graph.security.mailboxConfigurationEvidence")
	configurationId: Optional[str] = Field(alias="configurationId", default=None,)
	configurationType: Optional[SecurityMailboxConfigurationType | str] = Field(alias="configurationType", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	externalDirectoryObjectId: Optional[UUID] = Field(alias="externalDirectoryObjectId", default=None,)
	mailboxPrimaryAddress: Optional[str] = Field(alias="mailboxPrimaryAddress", default=None,)
	upn: Optional[str] = Field(alias="upn", default=None,)

from .security_evidence_remediation_status import SecurityEvidenceRemediationStatus
from .security_evidence_role import SecurityEvidenceRole
from .security_evidence_verdict import SecurityEvidenceVerdict
from .security_mailbox_configuration_type import SecurityMailboxConfigurationType
