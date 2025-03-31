from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class MailAssessmentRequest(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.mailAssessmentRequest"] = Field(alias="@odata.type", default="#microsoft.graph.mailAssessmentRequest")
	category: Optional[ThreatCategory | str] = Field(alias="category", default=None,)
	contentType: Optional[ThreatAssessmentContentType | str] = Field(alias="contentType", default=None,)
	createdBy: Optional[Union[AiInteractionMentionedIdentitySet, ApprovalIdentitySet, ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="createdBy", default=None,discriminator="odata_type", )
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	expectedAssessment: Optional[ThreatExpectedAssessment | str] = Field(alias="expectedAssessment", default=None,)
	requestSource: Optional[ThreatAssessmentRequestSource | str] = Field(alias="requestSource", default=None,)
	status: Optional[ThreatAssessmentStatus | str] = Field(alias="status", default=None,)
	results: Optional[list[ThreatAssessmentResult]] = Field(alias="results", default=None,)
	destinationRoutingReason: Optional[MailDestinationRoutingReason | str] = Field(alias="destinationRoutingReason", default=None,)
	messageUri: Optional[str] = Field(alias="messageUri", default=None,)
	recipientEmail: Optional[str] = Field(alias="recipientEmail", default=None,)

from .threat_category import ThreatCategory
from .threat_assessment_content_type import ThreatAssessmentContentType
from .ai_interaction_mentioned_identity_set import AiInteractionMentionedIdentitySet
from .approval_identity_set import ApprovalIdentitySet
from .chat_message_from_identity_set import ChatMessageFromIdentitySet
from .chat_message_mentioned_identity_set import ChatMessageMentionedIdentitySet
from .chat_message_reaction_identity_set import ChatMessageReactionIdentitySet
from .communications_identity_set import CommunicationsIdentitySet
from .share_point_identity_set import SharePointIdentitySet
from .threat_expected_assessment import ThreatExpectedAssessment
from .threat_assessment_request_source import ThreatAssessmentRequestSource
from .threat_assessment_status import ThreatAssessmentStatus
from .threat_assessment_result import ThreatAssessmentResult
from .mail_destination_routing_reason import MailDestinationRoutingReason
