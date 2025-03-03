from __future__ import annotations
from uuid import UUID
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class SecurityMailboxConfigurationEvidence(BaseModel):
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	detailedRoles: Optional[list[str]] = Field(default=None,alias="detailedRoles",)
	remediationStatus: Optional[SecurityEvidenceRemediationStatus] = Field(default=None,alias="remediationStatus",)
	remediationStatusDetails: Optional[str] = Field(default=None,alias="remediationStatusDetails",)
	roles: Optional[list[SecurityEvidenceRole]] = Field(default=None,alias="roles",)
	tags: Optional[list[str]] = Field(default=None,alias="tags",)
	verdict: Optional[SecurityEvidenceVerdict] = Field(default=None,alias="verdict",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	configurationId: Optional[str] = Field(default=None,alias="configurationId",)
	configurationType: Optional[SecurityMailboxConfigurationType] = Field(default=None,alias="configurationType",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	externalDirectoryObjectId: Optional[UUID] = Field(default=None,alias="externalDirectoryObjectId",)
	mailboxPrimaryAddress: Optional[str] = Field(default=None,alias="mailboxPrimaryAddress",)
	upn: Optional[str] = Field(default=None,alias="upn",)

from .security_evidence_remediation_status import SecurityEvidenceRemediationStatus
from .security_evidence_role import SecurityEvidenceRole
from .security_evidence_verdict import SecurityEvidenceVerdict
from .security_mailbox_configuration_type import SecurityMailboxConfigurationType

