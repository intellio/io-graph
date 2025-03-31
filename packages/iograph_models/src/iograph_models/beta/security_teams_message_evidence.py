from __future__ import annotations
from uuid import UUID
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class SecurityTeamsMessageEvidence(BaseModel):
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	detailedRoles: Optional[list[str]] = Field(alias="detailedRoles", default=None,)
	remediationStatus: Optional[SecurityEvidenceRemediationStatus | str] = Field(alias="remediationStatus", default=None,)
	remediationStatusDetails: Optional[str] = Field(alias="remediationStatusDetails", default=None,)
	roles: Optional[list[SecurityEvidenceRole | str]] = Field(alias="roles", default=None,)
	tags: Optional[list[str]] = Field(alias="tags", default=None,)
	verdict: Optional[SecurityEvidenceVerdict | str] = Field(alias="verdict", default=None,)
	odata_type: Literal["#microsoft.graph.security.teamsMessageEvidence"] = Field(alias="@odata.type", default="#microsoft.graph.security.teamsMessageEvidence")
	campaignId: Optional[str] = Field(alias="campaignId", default=None,)
	channelId: Optional[str] = Field(alias="channelId", default=None,)
	deliveryAction: Optional[SecurityTeamsMessageDeliveryAction | str] = Field(alias="deliveryAction", default=None,)
	deliveryLocation: Optional[SecurityTeamsDeliveryLocation | str] = Field(alias="deliveryLocation", default=None,)
	files: Optional[list[SecurityFileEvidence]] = Field(alias="files", default=None,)
	groupId: Optional[str] = Field(alias="groupId", default=None,)
	isExternal: Optional[bool] = Field(alias="isExternal", default=None,)
	isOwned: Optional[bool] = Field(alias="isOwned", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	messageDirection: Optional[SecurityAntispamTeamsDirection | str] = Field(alias="messageDirection", default=None,)
	messageId: Optional[str] = Field(alias="messageId", default=None,)
	owningTenantId: Optional[UUID] = Field(alias="owningTenantId", default=None,)
	parentMessageId: Optional[str] = Field(alias="parentMessageId", default=None,)
	receivedDateTime: Optional[datetime] = Field(alias="receivedDateTime", default=None,)
	recipients: Optional[list[str]] = Field(alias="recipients", default=None,)
	senderFromAddress: Optional[str] = Field(alias="senderFromAddress", default=None,)
	senderIP: Optional[str] = Field(alias="senderIP", default=None,)
	sourceAppName: Optional[str] = Field(alias="sourceAppName", default=None,)
	sourceId: Optional[str] = Field(alias="sourceId", default=None,)
	subject: Optional[str] = Field(alias="subject", default=None,)
	suspiciousRecipients: Optional[list[str]] = Field(alias="suspiciousRecipients", default=None,)
	threadId: Optional[str] = Field(alias="threadId", default=None,)
	threadType: Optional[str] = Field(alias="threadType", default=None,)
	urls: Optional[list[SecurityUrlEvidence]] = Field(alias="urls", default=None,)

from .security_evidence_remediation_status import SecurityEvidenceRemediationStatus
from .security_evidence_role import SecurityEvidenceRole
from .security_evidence_verdict import SecurityEvidenceVerdict
from .security_teams_message_delivery_action import SecurityTeamsMessageDeliveryAction
from .security_teams_delivery_location import SecurityTeamsDeliveryLocation
from .security_file_evidence import SecurityFileEvidence
from .security_antispam_teams_direction import SecurityAntispamTeamsDirection
from .security_url_evidence import SecurityUrlEvidence
